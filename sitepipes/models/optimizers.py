from abc import abstractmethod


class Optimizer:
    """ A base optimizer class """

    def __init__(self):
        pass

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
