from typing import List, Tuple

from .base import NvidiaStat

class ExtMemControllerFreqStat(NvidiaStat):
    _identifier = "EMC_FREQ"
    _num_args = 2

    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        if not self.arg_length_matches(args):
            return []

        (usage, _, freq) = args[1].partition('@')

        output = []

        if freq != "":
            output.append(
                ("EMC Frequency (MHz)", int(freq)),
            )

        if usage != "":
            output.append(
                ("EMC % Usage", int(usage[:-1]))
            )

        return output

class GR3DFreqStat(NvidiaStat):
    _identifier = "GR3D_FREQ"
    _num_args = 2
    
    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        if not self.arg_length_matches(args):
            return []
        
        (percent, _, freq) = args[1].partition('@')
        output = []

        if percent != "":
            percent = percent.replace("%", "")
            output = [
                ("GPU Activation time (%)", int(percent))
            ]

        if freq != "":
            if '[' not in freq:
                output.append(
                    ("GPU Clock (MHz)", int(freq))
                )
            else:
                for (idx, gpu_clock) in enumerate(freq[1:-1].split(',')):
                    output.append(
                        (f"GPU{idx} Clock (MHz)", int(gpu_clock))
                    )

        return output

class APEStats(NvidiaStat):
    _identifier = "APE"
    _num_args = 2

    def parse(self, args: List[str]) -> List[Tuple[str, int]]:
        if not self.arg_length_matches(args):
            return []
        
        return [
            ("APE Frequency (MHz)", int(args[1]))
        ]
