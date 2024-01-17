from typing import List, Tuple
import re

from .base import NvidiaStat


class Timestamp(NvidiaStat):
    _identifier = "TIME"
    _num_args = 2

    _args_regex = [
        r"([0-9]{2}(:)?){3}"
    ]

    def matches(self, arg: str) -> bool:
        print(arg)
        target_regex = r'[0-9]{2}-[0-9]{2}-[0-9]+'

        return re.match(target_regex, arg) is not None
    
    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        return [
            (f"Datetime", ' '.join(args))
        ]
