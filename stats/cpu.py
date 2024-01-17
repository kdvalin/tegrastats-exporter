from typing import List, Tuple
from .base import NvidiaStat

class CPUUsageStat(NvidiaStat):
    _identifier = "CPU"
    _num_args = 2
    
    _args_regex = [
        r"^\[((([0-9]+%@[0-9]+)|off)(,)?)+\]$"
    ]

    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        if not self.arg_length_matches(args):
            return []
        
        usage = args[1][1:-1]

        output = []
        for (idx, cpu) in enumerate(usage.split(',')):
            if cpu == "off":
                output.extend([
                    (f"CPU{idx} Usage (%)", 0),
                    (f"CPU{idx} Clock (MHz)", 0)
                ])
            else:
                cpu_info = cpu.split('@')

                output.extend([
                    (f"CPU{idx} Usage (%)", int(cpu_info[0][:-1])),
                    (f"CPU{idx} Clock (MHz)", int(cpu_info[1]))
                ])
        return output
