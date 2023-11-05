
from dataclasses import dataclass


@dataclass
class SongDto:
    id: int
    name: str
    album: str
