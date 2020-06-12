import re
import logging

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from app.models.youtube import Video
from app.constants import PATH_NOT_MATCHED


logger = logging.getLogger(__name__)


class YouTube:  
    """
    Represents a class for using the YouTube API.

    There is an OAuthlib HTTPS verification for running this Client.
    More information about setting up project and credentials:
    https://developers.google.com/youtube/v3/quickstart/python
    """

    api_service: str = "youtube"
    api_version: str = "v3"

    scopes: list = ["https://www.googleapis.com/auth/youtube.readonly"]

    def __init__(self, path_credentials: str):
        flow = InstalledAppFlow.from_client_secrets_file(
                                         path_credentials,
                                         self.scopes
                                         )
        # YouTube APi object
        self.search = build(
            self.api_service,
            self.api_version,
            credentials=flow.run_local_server()
        )

        self.next_page: str = "nextPageToken"
        self.parts: str = "snippet,contentDetails"
        self.private_video: str = "Private video"

        # file to write down the titles which don't match the regex
        self.not_mached_file = open(PATH_NOT_MATCHED, "w", encoding="utf-8")

    def tracks_from_playlists(
        self, playlists: list, regex: str, queries: tuple, queries_bg: tuple
    ) -> list:
        """
        Iterates all playlists and returns a list of Video objects.

        The list contains objects of app.models.youtube.Video class.
        More about playlist items from the YouTube API:
        https://developers.google.com/youtube/v3/docs/playlistItems
        """
        self.tracks = list()

        # Regex for extracting search query and year
        self.regex: str = regex
        self.queries: int = queries
        self.queries_bg: int = queries_bg

        logger.info(f"{len(playlists)} playlists loaded for extraction.")

        for self.playlist_id in playlists:
            self.__iterate_all_items()

        logger.info(f"{len(self.tracks)} matched the regex for search query.")
        return self.tracks

    def __iterate_all_items(self) -> None:
        """
        Iterates all items in the playlist and adds them to a list.

        Moves through every playlist page while next page token is present.
        Extracts the needed information from the items.
        """
        self.response = self.next_page
        self.page_token: str = str()

        # iterate while there are no more pages left
        while self.next_page in self.response:
            self.request = self.search.playlistItems().list(
                part=self.parts,
                playlistId=self.playlist_id,
                pageToken=self.page_token
            )

            self.response = self.request.execute()
            self.page_token = self.response.get(self.next_page)

            # iterate every item in current response
            for self.item in self.response["items"]:
                new_video = self.__create_video_object()

                if new_video and new_video.video_id not in [
                    i.video_id for i in self.tracks
                ]:
                    self.tracks.append(new_video)

    def __create_video_object(self) -> Video:
        """
        Filters data and fills app.models.youtube.Video object
        from YouTube returned data.
        """
        # get title and make empty video object
        self.title = self.item["snippet"]["title"]
        video = Video()

        # assert that the video is not private
        if self.title != self.private_video:
            # match search query in the video title
            match = re.match(self.regex, self.title)

            if match:
                # get and set playlist and video id
                video.playlist_id = self.playlist_id
                video.video_id = self.item["contentDetails"]["videoId"]
                # if there is a match take the search query group

                # get date and set date and set
                video.name = self.title

                matches = (
                    match.group(self.queries[0]).strip(),
                    match.group(self.queries[1]).strip(),
                )

                bg_matches = (
                    match.group(self.queries_bg[0]).strip(),
                    match.group(self.queries_bg[1]).strip(),
                )

                video.search_query = "{} {}".format(*matches).lower()
                video.search_query_bg = "{} {}".format(*bg_matches).lower()

                video.date = self.item["contentDetails"]["videoPublishedAt"]
            else:
                # write down the title which don't match the regex
                self.not_mached_file.write(self.title + "\n")
                return False

            return video
        return False
