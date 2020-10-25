import uuid


def remove_id(iterable, obj_id):
    """
    Removes any entry from iterable with matching ID

    :param iterable: list - A collection of objects (ie. Dataset, Model)
    :param obj_id: int - The ID matching the objects contained in iterable
    :return: The iterable without an entry for the filter ID
    """
    return [x for x in iterable if x.id != obj_id]


def gen_id():
    """ Generates a unique ID """
    return uuid.uuid4()
