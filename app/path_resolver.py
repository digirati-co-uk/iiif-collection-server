from flask import request
from s3 import get_list_of_files, get_file
from constants import JSON_FILE
from iiif_serializer import collection_serializer

def get_path(path):
  if path.endswith(JSON_FILE):
    return get_file(path)

  pathParts = request.path.split('/')[1:]
  basePath = ''.join([request.host_url, pathParts[0]])
  return collection_serializer(
    basePath, 
    request.url,
    get_list_of_files(path), 
    version=pathParts[0]
  )