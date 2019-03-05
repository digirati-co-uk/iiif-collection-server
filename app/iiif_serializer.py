from settings import BASE_FOLDER
from constants import DEFAULT_PROPS, JSON_FILE

def collection_serializer(basePath, path,  items, version='p3'):
  '''
  Serialises the contents of a folder 
  '''
  pathParts = path.split('/')
  props = DEFAULT_PROPS[version]
  id_property = props['id']
  type_property = props['type']
  collection_label = pathParts[-1] if pathParts[-1] != '' else pathParts[-2]
  result = {
    '@context': props['@context'],
    "label": props['labelFn'](collection_label),
  }
  
  result[id_property] = path
  result[type_property] = props['collection']
  
  if version != 'p3':
    result.update({
      "manifests": [],
      "collections": []
    })
  else:
    result.update({
      "items":[]
    })

  for item in items:
    child_id = basePath + item.replace(BASE_FOLDER, '');
    if child_id == path:
      continue
    child_label = item.rstrip('/').split('/')[-1] # item.replace('/',' ').strip()
    if item.endswith(JSON_FILE):
      manifest = {
        "label": props['labelFn'](child_label),
      }
      manifest[id_property] = child_id
      manifest[type_property] =  props['manifest']
      result[props['manifests']].append(manifest)
    else:
      sub_collection = {
        "label": props['labelFn'](child_label),
      }
      sub_collection[id_property] = child_id
      sub_collection[type_property] = props['collection']
      result[props['collections']].append(sub_collection)
  return result
