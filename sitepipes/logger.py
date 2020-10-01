from types import MethodType

import logging

class Logger:
    """
    Decorator class for automatic logging of function calls

    :param fn: object -
    """

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):

        result = self.fn(*args, **kwargs)
        logging.info(f'Ran {self.fn.__qualname__}(args={args}, kwargs={kwargs}) = {result}...')

        return result

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return MethodType(self, instance)