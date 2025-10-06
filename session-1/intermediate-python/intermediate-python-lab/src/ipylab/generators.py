from collections import deque
from statistics import median
from typing import Iterable, Iterator, TypeVar, Deque, Optional

T = TypeVar("T", int, float)

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """
    Yield lists of length `size` from `iterable`. Last chunk may be shorter.
    """

    buffer : list[T] = []
    for item in iterable:
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer


def moving_average(window: int):
    """
    Stateful GENERATOR that yields the moving average each time a new value is sent.
    Usage:
        gen = moving_average(5); next(gen)
        out = gen.send(3.0)  # returns current average
    """

    values = deque(maxlen=window)
    average = None
    while True:
        new_value = yield average
        values.append(new_value)
        average = sum(values) / len(values)
  

def moving_median(window: int):
    """
    Stateful GENERATOR that yields the moving median each time a new value is sent.
    """
    
    values = deque(maxlen=window)
    med = None
    while True:
        new_value = yield med
        values.append(new_value)
        med = median(values)
