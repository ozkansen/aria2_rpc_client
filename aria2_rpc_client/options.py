from pathlib import Path
from typing import Dict
from typing import List
from typing import Union

_OptionsStorage = Dict[str, Union[List[str], str]]


class Options:
    def __init__(self) -> None:
        self._options: _OptionsStorage = {}

    def export(self) -> _OptionsStorage:
        return self._options


class FileDownloadOptions(Options):
    def add_dir(self, path: Union[Path, str]) -> None:
        """Set download folder"""

        if isinstance(path, str):
            path = Path(path)

        self._options["dir"] = path.as_posix()

    def add_filename(self, name: str) -> None:
        """Set filename name='abc.zip'"""
        self._options["out"] = name

    def add_header(self, key: str, value: str) -> None:
        """Add new header"""

        header = self._options.get("header")
        if not isinstance(header, list):
            header = []
            self._options["header"] = header

        header.append(f"{key}: {value}")
