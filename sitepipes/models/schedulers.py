from abc import abstractmethod


class Scheduler:
    """ A base learning rate scheduler class """

    def __init__(self):
        pass

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
