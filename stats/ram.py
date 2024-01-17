from typing import List, Tuple

from .base import NvidiaStat

class RamStat(NvidiaStat):
    _identifier = "RAM"
    _num_args = 4

    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        if not self.arg_length_matches(args):
            return []
        usage = args[1].split('/')
        return [
            ("Used Memory (MB)", int(usage[0])),
            ("Total Memory (MB)", int(usage[1][:-2]))
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
            ("Used Swap (MB)", int(usage[0])),
            ("Total Swap (MB)", int(usage[1][:-2])),
            ("Cached Swap (MB)", int(cached))
        ]

class IRamStat(NvidiaStat):
    _identifier = "IRAM"
    _num_args = 3

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []

        current = args[1].split('(')[0]
        usage = current.split('/')

        return [
            ("Used IRAM (kB)", int(usage[0])),
            ("Available IRAM (kB)", int(usage[1][:-2]))
        ]
