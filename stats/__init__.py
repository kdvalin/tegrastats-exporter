from typing import Union
import logging

from .base import *
from .ram import *
from .cpu import *
from .engines import *
from .temps import *
from .power import *

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
            temps.TemperatureStat(),
            power.PowerStat()
        ]
    
    def find_stat(self, identifier) -> NvidiaStat:
        logger = logging.getLogger(__package__)
        for stat in self.stats:
            if stat.matches(identifier):
                logger.info(f"Found match for identifier {stat.header()}: {identifier}")
                yield stat
