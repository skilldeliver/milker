from dataclasses import dataclass, field


@dataclass
class Track:
    """
    Represents a Spotfy track.

    More information:
    https://developer.spotify.com/documentation/web-api/reference/tracks/get-track/
    """

    track_id: str = str()
    track_name: str = str()

    popularity: int = int()
    date: int = int()

    artists: list = field(default_factory=list)
    audio_features: dict = field(default_factory=dict)

    def __iter__(self):
        """Creates an iterator of the object for the dict built-in."""
        attributes = [
            "track_id",
            "track_name",
            "popularity",
            "date",
            "artists",
            "audio_features",
        ]

        for attr in attributes:
            # yield a tuple for key and value pair
            yield (attr, eval(f"self.{attr}"))
