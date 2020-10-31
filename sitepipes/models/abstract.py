from sitepipes.util.helper import obj_to_module_name

from abc import abstractmethod

import tensorflow as tf

import logging
import pickle
import inspect


class Model:
    """ A base model class """

    model = None
    name = None

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

    def save_model(self, path, pickle_model=False):
        """
        Saves a model to disk

        :param path: str - The path to save the model
        :param pickle_model: bool - Save using the pickle format

        >>> model = Model(...)
            model.train(...)
            model.save_model('~/Documents')

        """

        if self.model:

            model_type = obj_to_module_name(self.model)

            if pickle_model:
                with open(self.model, 'wb'):
                    pickle.dump(self.model, path)
                logging.info(f'Saved pickled {self.model.__name__} model to path={path}...')

            elif model_type == 'tensorflow':
                if tf.__version__ > '2':
                    pass
                else:
                    pass
                logging.info(f'Saved Tensorflow {tf.__version__} model to path={path}...')

            else:
                logging.error('Either pickle_model must be True or must be a Tensorflow model!')

        else:
            logging.error(f'Model with name = {{model.name}} has no model!')

    def load_model(self, path, pickle_model=False):
        """
        Loads a model from disk

        :param path: str - The path to load the model
        :param pickle_model: bool - Load using the pickle format

        >>> model = Model(...)
            model.train(...)
            model.save_model('~/Documents')

        """

        model_type = obj_to_module_name(self.model)

        if pickle_model:
            with open(self.model, 'rb'):
                self.model = pickle.load(path)
            logging.info(f'Loaded pickled {self.model.__name__} model from path={path}...')

        elif model_type == 'tensorflow':
            if tf.__version__ > '2':
                pass
            else:
                pass
            logging.info(f'Loaded Tensorflow {tf.__version__} model from path={path}...')

        else:
            logging.error('Either pickle_model must be True or must be a Tensorflow model!')


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

