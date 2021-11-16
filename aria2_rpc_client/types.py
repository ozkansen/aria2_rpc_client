from dataclasses import dataclass
from typing import List
from typing import NewType

GID = NewType("GID", str)


@dataclass(frozen=True)
class GlobalStat:
    downloadSpeed: str
    numActive: str
    numStopped: str
    numStoppedTotal: str
    numWaiting: str
    uploadSpeed: str


@dataclass(frozen=True)
class Version:
    enabledFeatures: List[str]
    version: str
