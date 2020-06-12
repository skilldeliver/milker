import sys
import logging

from app.clients.youtube import YouTube
from app.clients.spotify import Spotify
from app.constants import (
    PATH_SP_CREDENTIALS,
    PATH_YT_CREDENTIALS,
    PATH_SP_PAYNER_TRACKS,
    PATH_YT_PAYNER_TRACKS,
    YOUTUBE_PAYNER_PLAYLISTS,
    PAYNER_REGEX,
    QUERIES,
    BG_QUERIES,
)
from app.utils.data import read_from_json, write_to_json

logger = logging.getLogger(__name__)


def get_youtube_videos(
    playlists: list,
    regex: str,
    queries: tuple,
    queries_bg: tuple,
    save_file: str
) -> None:
    """
    Gets an information about every
    YouTube video in all app.constants.YOUTUBE_PLAYLISTS.

    Information of every video consist of:
        video_id (not important but helpful)
        playlist_id (not important but helpful)
        name (the title of the video)
        search_query (the extracted name for searching with Spotify)
        date (the extracted date from the video title)

    Saves the information in a .json file.
    """
    youtube = YouTube(PATH_YT_CREDENTIALS)

    tracks = youtube.tracks_from_playlists(playlists,
                                           regex,
                                           queries,
                                           queries_bg)
    tracks_dict = {"tracks": [dict(track) for track in tracks]}

    write_to_json(tracks_dict, save_file)


def get_spotify_data(youtube_tracks_file: str, spotify_tracks: str):
    """
    Gets an information about every
    query from YouTube video.

    Information of every video consist of:
        track_id (helps for filtering the unique ones)
        track_name (the Spotfy name of the track)
        popularity (the popularity of the song calculated by Spotify)
        date (the extracted date from the video title)

        artists (list of the artists names)
        audio_features (the characteristics of the song)
    Saves the information in a .json file.
    """
    spotify = Spotify(PATH_SP_CREDENTIALS)

    youtube_tracks = read_from_json(youtube_tracks_file)

    tracks = spotify.from_youtube_tracks(youtube_tracks)
    tracks_dict = {"tracks": [dict(track) for track in tracks]}

    write_to_json(tracks_dict, spotify_tracks)


def main():

    if "yt" in sys.argv:
        logger.info(f"Executing YouTube videos extracting")
        get_youtube_videos(
            YOUTUBE_PAYNER_PLAYLISTS,
            PAYNER_REGEX,
            QUERIES,
            BG_QUERIES,
            PATH_YT_PAYNER_TRACKS,
        )

    if "sp" in sys.argv:
        logger.info(f"Executing Spotfy tracks extracting")
        get_spotify_data(PATH_YT_PAYNER_TRACKS, PATH_SP_PAYNER_TRACKS)

    if len(sys.argv) < 2:
        logger.info(f"Executing YouTube and Spotfy extracting")
        get_youtube_videos(
            YOUTUBE_PAYNER_PLAYLISTS,
            PAYNER_REGEX,
            QUERIES,
            BG_QUERIES,
            PATH_YT_PAYNER_TRACKS,
        )
        get_spotify_data(PATH_YT_PAYNER_TRACKS, PATH_SP_PAYNER_TRACKS)


if __name__ == "__main__":
    main()
