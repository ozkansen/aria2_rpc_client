from dataclasses import dataclass
from typing import List


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


@dataclass(frozen=True)
class SessionInfo:
    sessionId: str
