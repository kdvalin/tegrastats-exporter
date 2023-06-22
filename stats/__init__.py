from .base import *
from .ram import *
from .cpu import *
from .engines import *
from .temps import *

class StatContainer:
    def __init__(self):
        self.stats: List[NvidiaStat] = [
            ram.RamStat(),
            ram.SwapStat(),
            ram.IRamStat(),
            cpu.CPUUsageStat(),
            engines.ExtMemControllerFreqStat(),
            engines.GR3DFreqStat(),
            engines.APEStats(),
            temps.TemperatureStat()
        ]
    
    def find_stat(self, identifier) -> NvidiaStat | None:
        for stat in self.stats:
            if stat.matches(identifier):
                return stat
        return None
