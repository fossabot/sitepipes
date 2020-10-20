from sitepipes.models.optimizers import Optimizer

from abc import abstractmethod


class PTOptimizer(Optimizer):
    """ An optimizer in PyTorch """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
