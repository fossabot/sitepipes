from sitepipes.models.schedulers import Scheduler

from abc import abstractmethod


class PTScheduler(Scheduler):
    """ A learning rate scheduler for PyTorch"""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
