from sitepipes.util.helper import gen_id


def test_gen_id():
    unique_id = gen_id()
    assert type(unique_id) == int
