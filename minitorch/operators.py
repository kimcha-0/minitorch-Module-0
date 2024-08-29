"""
Collection of the core mathematical operators used throughout the code base.
"""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    return a * b


def id(a: any) -> any:
    return a


def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def lt(a: float, b: float) -> float:
    return a < b


def eq(a: float, b: float) -> float:
    return a == b


def max(a: float, b: float) -> float:
    return a if a > b else b


def is_close(a: float, b: float) -> float:
    return abs(a - b) < .01


def sigmoid(a: float) -> float:
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    else:
        return math.exp(a) / (1 + math.exp(a))


def relu(a: float) -> float:
    return a if a >= 0 else 0


def log(a: float) -> float:
    return math.log(a)


def exp(a: float) -> float:
    return math.exp(a)


def inv(a: float) -> float:
    return 1 / a


def log_back(a: float, b: float) -> float:
    return b / a


def inv_back(a: float, b: float) -> float:
    return -b / a ** 2


def relu_back(a: float, b: float) -> float:
    return b if a >= 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
