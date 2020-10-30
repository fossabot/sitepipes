from abc import abstractmethod


class Model:
    """ A base model class """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def train(self):
        """ Logic for model training """
        pass

    @abstractmethod
    def infer(self):
        """ Logic for model inference """
        pass


class Optimizer:
    """ A base optimizer class """

    def __init__(self):
        pass

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass


class Scheduler:
    """ A base learning rate scheduler class """

    def __init__(self):
        pass

    @abstractmethod
    def set_params(self):
        """ Sets parameters """
        pass
