from . import NvidiaStat

from typing import List, Tuple
import re

class PowerStat(NvidiaStat):
    _identifier = "POWER"
    _regex = r"^([0-9]+)mW/([0-9]+)mW$"
    _num_args = -2 # Go back 1 and fetch the previous arg

    def matches(self, arg: str) -> bool:
        return re.match(self._regex, arg) is not None

    def parse(self, args: List[str]) -> List[Tuple[str, float]]:
        if not self.arg_length_matches(args):
            return []
        
        self._logger.debug(args)
        rail = args[0]
        usage_re = re.search(self._regex, args[1])
        current_usage, avg_usage = usage_re.groups()
        
        return [
            (f"{rail} Power Usage (mW)", float(current_usage)),
            (f"{rail} Avg Power Usage (mW)", float(avg_usage))
        ]
