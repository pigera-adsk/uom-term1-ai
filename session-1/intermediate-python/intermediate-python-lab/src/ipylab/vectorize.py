from typing import Sequence
import numpy as np
import math

def python_rms(seq: Sequence[float]) -> float:
    """
    Pure-Python RMS implementation.
    """
    total = 0
    for value in seq:
      square = value * value
      total = total + square
    return math.sqrt(total / len(seq))


def numpy_rms(arr: np.ndarray) -> float:
    """
    NumPy-vectorized RMS implementation.
    """
    arr_squared = arr * arr
    mean_squared = np.mean(arr_squared)
    return float(np.sqrt(mean_squared))