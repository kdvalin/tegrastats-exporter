from typing import List, Tuple

from .base import NvidiaStat

class RamStat(NvidiaStat):
    _identifier = "RAM"
    _num_args = 4

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []
        usage = args[1].split('/')
        return [
            ("Used Memory (MB)", usage[0]),
            ("Total Memory (MB)", usage[1][:-2])
        ]

class SwapStat(NvidiaStat):
    _identifier = "SWAP"
    _num_args = 4

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []
        usage = args[1].split('/')
        cached = args[-1][:-3]

        return [
            ("Used Swap (MB)", usage[0]),
            ("Total Swap (MB)", usage[1][:-2]),
            ("Cached Swap (MB)", cached)
        ]

class IRamStat(NvidiaStat):
    _identifier = "IRAM"
    _num_args = 4

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []

        usage = args[1].split('/')

        return [
            ("Used IRAM (kB)", usage[0]),
            ("Available IRAM (kB)", usage[1][:-2])
        ]
