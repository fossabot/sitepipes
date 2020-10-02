from types import MethodType
from functools import wraps

import logging
import inspect


def func_logger(obj):
    """ Decorator to automatically log function calls and results """

    @wraps(obj)
    def inner(*args, **kwargs):
        result = obj(*args, **kwargs)

        print('\n\n')
        print(f'DEBUG Called object = {obj.__qualname__}')
        print(f'DEBUG args = {args}')
        print(f'DEBUG kwargs = {kwargs}')
        print(f'DEBUG result = {result}')
        print('\n\n')

        return result

    return inner


def logger(cls, decorate_static=True, decorate_class=True,
           decorate_property=True, decorate_routine=True):
    """
    A class decorator for automatic logging of various methods

    :param cls: object - The class definition to decorate
    :param decorate_static: bool - Whether to decorate static methods
    :param decorate_class: bool - Whether to decorate class methods
    :param decorate_property: bool - Whether to decorate properties
    :param decorate_routine: bool - Whether to decorate all other routines
    """

    logging.info(f'Creating loggers for methods of {type(cls).__name__}...')

    for name, obj in vars(cls).items():

        if decorate_static and isinstance(obj, staticmethod):
            decorated_fn = func_logger(obj.__func__)
            setattr(obj, name, staticmethod(decorated_fn))

        elif decorate_class and isinstance(obj, classmethod):
            decorated_fn = func_logger(obj.__func__)
            setattr(obj, name, classmethod(decorated_fn))

        elif decorate_property and isinstance(obj, property):
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fget:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fget:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)

        elif decorate_routine and inspect.isroutine(obj):
            setattr(cls, name, func_logger(obj))


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
