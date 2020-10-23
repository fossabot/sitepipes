from abc import abstractmethod

from sitepipes.models.optimizers import Optimizer


class PTOptimizer(Optimizer):
    """ An optimizer in PyTorch """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
