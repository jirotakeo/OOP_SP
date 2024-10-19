from src.utils import read_json, create_obj_from_json


def test_read_json(data):
    assert read_json("../data/products.json") == data


def test_create_obj_from_json(data):
    raw_data = create_obj_from_json(data)
    assert len(raw_data) == 2
