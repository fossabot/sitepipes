from sitepipes.datasets.meta import MetaDataset


class Dataset(metaclass=MetaDataset):
    """ A parent class for all data that flows between components """

    def __init__(self):
        pass

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name)
