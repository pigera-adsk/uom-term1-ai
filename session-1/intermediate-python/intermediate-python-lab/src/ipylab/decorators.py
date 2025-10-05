import time, logging, functools
from typing import Callable, TypeVar, Any, ParamSpec, Optional

P = ParamSpec("P")
T = TypeVar("T")

def timed(threshold_ms: Optional[float] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Decorator that logs runtime; if threshold_ms is set and runtime exceeds it,
    logs a WARNING, else INFO.
    """
    
    def decorate(fn: Callable[P, T]) -> Callable[P, T]:
        # TODO: implement
        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            end = time.perf_counter()
            elapsed_ms = (end - start) * 1000
            if threshold_ms is not None and elapsed_ms > threshold_ms:
                logging.warning(f"SLOW: {fn.__name__} took {elapsed_ms:.2f} ms")
            else:
                logging.info(f"{fn.__name__} took {elapsed_ms:.2f} ms")
            return result
        return wrapper
    return decorate