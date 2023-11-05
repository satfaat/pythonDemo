from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int
    z: int = field(default=0)
