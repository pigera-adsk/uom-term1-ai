import numpy as np
from typing import Sequence

def feature_vector(x: np.ndarray) -> list[float]:
    """
    Compute basic features for 1D signal x:
      - RMS
      - zero-crossings (count)
      - peak-to-peak (max - min)
      - mean absolute diff (MAD)
    Return as [rms, zc, p2p, mad].
    """

    arr_squared = x * x
    mean_squared = np.mean(arr_squared)
    rms = float(np.sqrt(mean_squared))

    signs = np.sign(x)
    sign_diff = np.diff(signs)
    zc = np.count_nonzero(sign_diff)

    p2p = x.max() - x.min()

    mad = (np.abs(x-float(x.mean()))).mean()

    return [rms, zc, p2p, mad]