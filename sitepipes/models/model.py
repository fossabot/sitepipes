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
