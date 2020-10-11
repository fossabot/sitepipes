from sitepipes.exceptions import ProtectedDatasetError
from sitepipes.logger import logger

from abc import abstractmethod


class Assembly:
    """ A collection of Component objects """


class MetaComponent(type):
    """ A type for pipeline components """

    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        cls = logger(cls)
        setattr(cls, 'pump_data', mcs.pump_data)
        return cls

    def __getattr__(self, item):
        err_msg = f'{type(self).__name__} has no attribute "{item}"...'
        print(err_msg)
        raise AttributeError(err_msg)

    def __setattr__(self, key, value):
        pass


class Component(metaclass=MetaComponent):
    """
    A general purpose parent class for all pipeline components

    :param inlets: list - Objects that send data to the component
    :param outlets: list - Objects that receive data from the component
    """

    inlets = []
    outlets = []

    def __init__(self, inlets=None, outlets=None):
        if inlets is not None:
            self.inlets = inlets
        if outlets is not None:
            self.outlets = outlets

    def __call__(self):

        return self.flow()

    def push_outlets(self, comp, outlets=None):
        """
        Pushes data to all outlets

        :param comp: CompositeDataset - With one or more datasets
        :param outlets:
        :return:
        """
        if outlets is None:
            outlets = self.outlets

        if len(outlets) < 1:
            raise ValueError(f'"{outlets}" must be greater than length 1,'
                             f'found length = {len(outlets)}')

        for outlet in outlets:
            comp.send(outlet)


class Fluid(metaclass=MetaComponent):
    """ A parent class for all data that flows between components """


class Connector():
    """ A component for connecting to an external environment """


class DatabaseConnector(Connector):
    """ A component for connecting to a database """


class Pipe(Component):
    """
    A component for moving data from Point A to Point B

    :param point_a: str - Path for the data source
    :param point_b: str - Path for the data destination
    """

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def check_integrity(self):
        """ Checks the data integrity of a data flow """


class Fitting(Component):
    """
    A component for connecting two or more pipes into one or more flows. Will
    randomly split data flowing out into "pipes_out" pieces

    :param pipes_in: int - The number of pipes coming in
    :param pipes_out: int - The number of pipes coming out
    """

    def __init__(self, pipes_in, pipes_out=1):
        self.pipes_in = pipes_in
        self.pipes_out = pipes_out


class Valve(Component):
    """ A component for controlling the flow of data """


class Queue(Valve):
    """ A component for queueing a data flow"""


class Filter(Component):
    """ A component for removing data from the pipeline """


class Reservoir(Component):
    """ A component for storing data on disk (long-term) """


class Tank(Component):
    """
    A component for storing data in-memory (short-term)

    The contents of each tank are cleared when memory loses power. DO NOT store
    any data that cannot be lost here
    """

    def __init__(self):
        pass

    def __call__(self, model, instructions):
        pass

    def pump_data(self, dataset_id, location):
        """
        Selects a dataset by ID and sends it to a location.

        :param dataset_id: int - ID of the dataset
        :param location: str - Path to the data receiver
        """

        if self.dataset_id in self.protected_ids:
            raise ProtectedDatasetError


class ProtectedTank(Tank):
    """
    A tank with data that cannot leave the tank

    :param protected_names: list - The names of variables that cannot be sent
    """

    def __init__(self, protected_ids):
        super.__init__()
        self.protected_ids = protected_ids

    def __call__(self, model, instructions):
        pass

    def pump_data(self, dataset_id, location):
        """
        Selects a dataset by ID and sends it to a location.

        :param dataset_id: int - ID of the dataset
        :param location: str - Path to the data receiver
        """

        if self.dataset_id in self.protected_ids:
            raise ProtectedDatasetError

class DataTank(Tank):
    """ A type of tank used to store Dataset instances in short-term memory """
    pass


class ProtectedDataTank(DataTank, ProtectedTank):
    """ A type of tank with Dataset instances that cannot leave the tank """
    pass


class ModelTank(DataTank):
    """ A type of tank used to store Model instances in-memory """
    pass


class ProtectedModelTank(ModelTank, ProtectedDataTank):
    """ A type of tank with Model instances that cannot leave the tank """
    pass


class Screen(Component):
    """ A component for viewing the state of another component """


class Hose(Component):
    """ A component for portable and flexible data moving """


class Processor(Component):
    """ A component for running computations on data """


class Controller(Component):
    """ A component for controlling a collection of components """


class MainController(Controller):
    """
    A component for controlling a federated network """

    def add_host(self, host):
        self.hosts.append(host)


class Host(Component):
    """
    A machine with zero or more datasets and/or models

    :param ip_address: str - The IP address of the host machine with data / models
    :param port: int - The port for inbound communication
    """

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.datasets = []
        self.models = []

    def add_dataset(self):
        pass

    def remove_dataset(self):
        pass

    def add_model(self):
        pass

    def remove_model(self):
        pass


class TrainingPlan:
    pass