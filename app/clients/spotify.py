import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from transliterate import translit

from app.models.spotify import Track
from app.utils.data import read_from_json


class Spotify:
    """
    Represents a class for using the Spotify API wrapper (Spotipy).

    More information about setting up project and credentials with Spotipy:
    https://spotipy.readthedocs.io/en/latest/#
    """

    def __init__(self, path_credentials: str):
        self.path_credentials = path_credentials
        self.__set_credentials()

        clm = SpotifyClientCredentials()
        self.sp = spotipy.Spotify(client_credentials_manager=clm)

    def from_youtube_tracks(self, youtube_tracks: dict):
        """Gets tracks information using YouTube queries."""
        self.tracks = list()

        for self.track in youtube_tracks["tracks"]:

            self.query = self.track["search_query"]
            self.query_bg = self.track["search_query_bg"]
            self.query_bg_trans = translit(
                self.track["search_query_bg"], "bg", reversed=True
            )

            for query in (self.query, self.query_bg, self.query_bg_trans):
                items = self.sp.search(query,
                                       limit=1,
                                       type="track")["tracks"]["items"]
                if items:
                    self.__append_track(items)
                    break

        return self.tracks

    def __append_track(self, items):
        """Append track to the tracks list if it is not already in the list."""
        self.item = items[0]
        new_track = self.__create_track_object()

        if new_track.track_id not in [t.track_id for t in self.tracks]:
            self.tracks.append(new_track)

    def __create_track_object(self):
        """
        Parses Spotify raw data into an object
        with the data which is needed.
        """
        new_track = Track()

        new_track.track_id = self.item["id"]
        new_track.track_name = self.item["name"]

        new_track.popularity = self.item["popularity"]
        new_track.date = self.track["date"]

        new_track.artists = [a["name"] for a in self.item["artists"]]
        new_track.audio_features = self.__get_audio_feautres(self.item["id"])

        return new_track

    def __get_audio_feautres(self, s_id: int) -> dict:
        """
        Returns the audio features of the song.
        Calculated by Echonest's algorithms and provided
        from the Spotify API.

        More info what are audio features:
        https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
        """
        data = self.sp.audio_features(tracks=[s_id])[0]
        items_to_remove = ["type", "id", "uri", "track_href", "analysis_url"]

        try:
            for item in items_to_remove:
                del data[item]
            return data
        except Exception:
            return None

    def __set_credentials(self) -> None:
        """"Sets Spotify credentials for the Client instance."""
        credentials_dict = read_from_json(self.path_credentials)

        os.environ["SPOTIPY_CLIENT_ID"] = credentials_dict["client_id"]
        os.environ["SPOTIPY_CLIENT_SECRET"] = credentials_dict["client_secret"]
        os.environ["SPOTIPY_REDIRECT_URI"] = credentials_dict["redirect_uri"]
