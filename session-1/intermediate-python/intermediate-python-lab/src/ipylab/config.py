from dataclasses import dataclass

@dataclass(frozen=True)
class LabConfig:
    """
    Configuration for the lab.
    """
    sample_rate: int = 1000
    duration_s: float = 2.0
    noise_std: float = 0.15
    median_window: int = 11
    cache_size: int = 256 
