import logging
from pathlib import PurePath

LOG_LEVEL = logging.DEBUG

PATH_PROJECT = PurePath(__file__).parent.parent

PATH_DATA = PurePath(PATH_PROJECT).joinpath("data")
PATH_APP = PurePath(PATH_PROJECT).joinpath("app")

PATH_YT_CREDENTIALS = PurePath(PATH_APP).joinpath("client_yt_secret.json")
PATH_SP_CREDENTIALS = PurePath(PATH_APP).joinpath("client_sp_secret.json")

PATH_NOT_MATCHED = PurePath(PATH_DATA).joinpath("not_matched.txt")

PATH_YT_PAYNER_TRACKS = PurePath(PATH_DATA).joinpath("youtube_payner_tracks.json")
PATH_SP_PAYNER_TRACKS = PurePath(PATH_DATA).joinpath("tracks_payner.json")


PAYNER_REGEX = r"^(?P<artist>.*?)\s(.*?)-(?P<song>.*)/\s(?P<bgartist>.*?)\s(.*?)-(?P<bgsong>.*),(.*)$"
QUERIES = "artist", "song"
BG_QUERIES = "bgartist", "bgsong"

YOUTUBE_PAYNER_PLAYLISTS = [
    "PLWhONodvbQndWEqRr7GyxWfRQjmBqKSxI",  # 2014
    "PLWhONodvbQnfluSVfbagq23nL2MT8QXpw",  # 2015
    "PLWhONodvbQnerDDqcQ2O-78Dh0wZzX-c3",  # 2016
    "PLWhONodvbQnfLXFqUnUjGNOGZxUVpPMZz",  # 2017
    "PLWhONodvbQnc743n4eZjT-q-Ws254zFqQ",  # 2018
    "PLWhONodvbQnegRSv-BDWuLaL5zgsH5jyu",  # 2019
    "PLWhONodvbQncO-swvOqapo2vXF7xIDiG-"   # 2020
]
