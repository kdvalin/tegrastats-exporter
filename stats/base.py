import abc
import logging
from typing import List, Tuple

class NvidiaStat:
    _logger = logging.getLogger(__package__)
    _identifier = ""
    _num_args = 0

    def matches(self, arg: str) -> bool:
        return self._identifier == arg

    def header(self) -> str:
        return self._identifier

    def get_num_args(self) -> int:
        return self._num_args

    @abc.abstractclassmethod
    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        return []

    def arg_length_matches(self, args: List[str]) -> bool:
        len_matches = abs(self._num_args) == len(args)
        if not len_matches:
            self._logger.warn(f"[{self._identifier}] Passed length {len(args)} does not match expected {abs(self._num_args)}, skipping {args}")
        return len_matches
