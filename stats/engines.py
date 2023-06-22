from typing import List, Tuple

from .base import NvidiaStat

class ExtMemControllerFreqStat(NvidiaStat):
    _identifier = "EMC_FREQ"
    _num_args = 2

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []

        return [
            ("EMC Frequency (MHz)", args[1][1:])
        ]

class GR3DFreqStat(NvidiaStat):
    _identifier = "GR3D_FREQ"
    _num_args = 2
    
    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []
        
        details = args[1].split('@')
        gpu_usage = details[1][1:-1]

        output = [
            ("GPU Activation time (%)", details[0][:-1])
        ]

        for (idx, gpu_clock) in enumerate(gpu_usage.split(',')):
            output.append(
                (f"GPU{idx} Clock (MHz)", gpu_clock)
            )

        return output

class APEStats(NvidiaStat):
    _identifier = "APE"
    _num_args = 2

    def parse(self, args: List[str]) -> List[Tuple[str, str]]:
        if not self.arg_length_matches(args):
            return []
        
        return [
            ("APE Frequency (MHz)", args[1])
        ]
