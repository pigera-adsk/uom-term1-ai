from contextlib import contextmanager
import time
import logging
from typing import Iterator

@contextmanager
def timer(label: str) -> Iterator[None]:
    """
    Context manager that logs how long the block took (in ms).
    """

    start_time = time.time()
    try:
        yield
    finally:
        elapsed_time = (time.time() - start_time) * 1000
        logging.info(f"{label}: {elapsed_time:.2f} ms")   
  

@contextmanager
def suppress_and_log(*exc_types: type[BaseException]) -> Iterator[None]:
    """
    Context manager that suppresses given exception types and logs the exception.
    """

    try:
        yield
    except exc_types as e:
        logging.exception(f"Suppressed exception: {e}")