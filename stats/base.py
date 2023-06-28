import abc
from typing import List, Tuple

class NvidiaStat:
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
        len_matches = self._num_args == len(args)
        if not len_matches:
            print(f"[{self._identifier}] Passed length does not match, skipping")
        return len_matches
