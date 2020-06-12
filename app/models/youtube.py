from dataclasses import dataclass


@dataclass
class Video:
    """Represents an YouTube video."""

    playlist_id: int = int()
    video_id: int = int()
    name: str = str()
    search_query: str = str()
    search_query_bg: str = str()
    date: int = int()

    def __iter__(self):
        """Creates an iterator of the object for the dict built-in."""
        attributes = [
            "playlist_id",
            "video_id",
            "name",
            "search_query",
            "search_query_bg",
            "date",
        ]

        for attr in attributes:
            # yield a tuple for key and value pair
            yield (attr, eval(f"self.{attr}"))
