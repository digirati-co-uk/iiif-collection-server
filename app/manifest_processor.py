import json
from flask import request
from constants import JSON_FILE


def check_extension_is_valid(path):
  '''
  The uploaded files can only have certain extensions in order to keep compatibility with most of the readers.

  :param: path - the location where the file will be accessable after upload
  :raise: ValueError - if the path doesn't ends with the json file endings defined in constants.JSON_FILE
  '''
  if not path.endswith(JSON_FILE):
    raise ValueError('path must end with any of ' + ', '.join(JSON_FILE) )


def check_is_jsonld(manifest):
  '''
  Checks that the '@context' is available on the manifest passed as a parameter
  :param: manifest - the manifest needs to be checked
  :raise: TypeError - if the passed IIIF Manifest doesn't have a context
  '''
  if '@context' not in manifest:
    raise TypeError('The input IIIF Manifest needs to have a @context attribute (JSON-LD)')


def get_normalised_context(manifest):
  '''
  normalises context as a list
  :param: manifest - IIIF Manifest 
  :return: normalised @context always return an `list`
  '''
  context = manifest['@context']
  return [context] if type(context) == str else context
  

def get_presentation_version(jsonld_context):
  '''
  TODO: somehow simplify this, the repeated urls looking a little bit crowded and ugly.
  :param: jsonld_context
  :return: the presentation api version
  :raise: TypeError if the context type is not vaild.
  '''
  if "http://iiif.io/api/presentation/2/context.json" in jsonld_context or "https://iiif.io/api/presentation/2/context.json" in jsonld_context:
    return 2
  elif "http://iiif.io/api/presentation/3/context.json" in jsonld_context or "https://iiif.io/api/presentation/3/context.json" in jsonld_context:
    return 3
  elif "http://www.shared-canvas.org/ns/context.json" in jsonld_context or "https://www.shared-canvas.org/ns/context.json" in jsonld_context:
    return 1
  else:
    raise TypeError('JSON-LD @context desn\'t match any known IIIF presentation type')
   
    
def preprocess_manifest(path, raw_json_str):
  '''
  Basic jsonld validity check and top level id updating at the moment.
  :params: path - the path without the 
  :params: raw_json_str - input json
  :return: validated manifest
  '''
  check_extension_is_valid(path)
  manifest = json.loads(raw_json_str)
  check_is_jsonld(manifest)
  json_ld_context = get_normalised_context(manifest)
  presentation_version = get_presentation_version(json_ld_context)
  
  # TODO: use upgrader(https://github.com/IIIF/prezi-2-to-3) when it will be available through pip
  # for the moment we just assume everything is in presentation v3 format
  if presentation_version < 3:
    pass

  id_property = '@id' if presentation_version < 3 else 'id'
  manifest[id_property] = request.url
  return manifest
