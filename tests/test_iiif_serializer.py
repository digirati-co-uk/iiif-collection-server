import os
import json
import pytest
from iiif_collection_server.iiif_serializer import collection_serializer


FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'collection_serializer')


@pytest.fixture(autouse=True)
def files(request):
    result = dict()
    for filename in os.listdir(FIXTURE_PATH):
        with open(os.path.join(FIXTURE_PATH, filename)) as json_data:
            result[filename] = json.load(json_data)
    return result


def test_collection_serializer_p3(files):
    base_url = 'http://0.0.0.0:8181/p3/'
    url = 'http://0.0.0.0:8181/p3/'
    items = files['input.json']
    version = 'p3'
    result = collection_serializer(base_url, url, items, version)
    assert json.dumps(result, sort_keys=True) == json.dumps(files['p3_output.json'], sort_keys=True)


def test_collection_serializer_p2(files):
    base_url = 'http://0.0.0.0:8181/p2/'
    url = 'http://0.0.0.0:8181/p2/'
    items = files['input.json']
    version = 'p2'
    result = collection_serializer(base_url, url, items, version)
    assert json.dumps(result, sort_keys=True) == json.dumps(files['p2_output.json'], sort_keys=True)
