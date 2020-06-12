"""
Operations with data which is going to be used in the programm.

Includes:
    RW(reading and writing) from .json files.
    - Loading input data (for search queries).
    - Saving the raw data (from the YouTube and Spotify API's).
"""

from json import dump, load


def read_from_json(file_path: str) -> dict:
    """Reads dictionary from given .json file."""
    with open(file_path, "r", encoding="utf-8") as f:
        adict = load(f)
    return adict


def write_to_json(adict: dict, file_path: str) -> None:
    """Writes dictionary to given .json file."""
    with open(file_path, "w", encoding="utf-8") as f:
        dump(adict, f, ensure_ascii=False)
