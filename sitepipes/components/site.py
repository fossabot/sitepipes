from sitepipes.components.component import Component


class Site(Component):
    """
    A machine with zero or more datasets and/or models

    :param host: str - The IP address of the host machine with data / models
    :param port: int - The port for inbound communication
    """

    def __init__(self, host=None, port=None):
        super().__init__(host, port)
        self.host = host
        self.port = port
        self.datasets = []
        self.models = []

    def add_dataset(self, dataset):
        self.datasets.append(dataset)

    def remove_dataset(self, dataset):
        self.datasets = [d for d in self.datasets if d != dataset]

    def add_model(self):
        pass

    def remove_model(self, model):
        self.models = [m for m in self.models if m.name != model.name]


class MobileSite(Site):
    def __init__(self, host=None, port=None):
        super().__init__()
        self.host = host
        self.port = port


class ServerSite(Site):
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port