from .base import *
from .ram import *

class StatContainer:
    def __init__(self):
        self.stats: List[NvidiaStat] = [
            ram.RamStat(),
            ram.SwapStat()
        ]
    
    def find_stat(self, identifier) -> NvidiaStat | None:
        for stat in self.stats:
            if stat.matches(identifier):
                return stat
        return None
