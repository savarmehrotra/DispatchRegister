from functools import singledispatch
from typing import Callable


# Implementation 1: Using Wrappers on singledispatch
@singledispatch
def dispatch_wrapper(arg):
    raise TypeError(f"No function registered for argument of type {type(arg)}")

def register_wrapper(func: Callable) -> Callable:
    dispatch_wrapper.register(func.__annotations__['x'], func)
    return func
