from sitepipes.models.schedulers import Scheduler

from abc import abstractmethod


class TFScheduler(Scheduler):
    """ A learning rate scheduler for Tensorflow """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
