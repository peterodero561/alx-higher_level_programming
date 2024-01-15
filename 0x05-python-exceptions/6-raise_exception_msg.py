#!/usr/bin/py
def raise_exception_msg(message=""):
    try:
        result = undefined_variable
    except NameError as e:
        raise NameError(message) from e

