from typing import List, Tuple
import re

from .base import NvidiaStat


class TemperatureStat(NvidiaStat):
    _identifier = "TEMP"
    _num_args = 1

    def matches(self, arg: str) -> bool:
        target_regex = '[A-Za-z0-9]+@[0-9]+\.[0-9]+C'

        return re.match(target_regex, arg)
    
    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []
        
        data = args[0].split('@')

        return [
            (f"{data[0]} Temperature (C)", data[1][:-1])
        ]
