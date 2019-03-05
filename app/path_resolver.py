from flask import request
from s3 import get_list_of_files, get_file
from constants import JSON_FILE
from iiif_serializer import collection_serializer


def get_path(path):
    if path.endswith(JSON_FILE):
        return get_file(path)

    path_parts = request.path.split('/')[1:]
    base_path = ''.join([request.host_url, path_parts[0]])
    return collection_serializer(
        base_path,
        request.url,
        get_list_of_files(path),
        version=path_parts[0]
    )
