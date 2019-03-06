from iiif_collection_server.settings import BASE_FOLDER
from iiif_collection_server.constants import DEFAULT_PROPS, JSON_FILE


def collection_serializer(base_path, path,  items, version='p3'):
    """
    Serialises the contents of a folder
    """
    print(base_path, path)
    path_parts = path.split('/')
    props = DEFAULT_PROPS[version]
    id_property = props['id']
    type_property = props['type']
    collection_label = path_parts[-1] if path_parts[-1] != '' else path_parts[-2]
    result = dict()
    result["@context"] = props['@context']
    result["label"] = props['labelFn'](collection_label)
    result[id_property] = path
    result[type_property] = props['collection']

    if version != 'p3':
        result.update({
            "manifests": [],
            "collections": []
        })
    else:
        result.update({
            "items": []
        })

    for item in items:
        child_id = base_path + item.replace(BASE_FOLDER + '/', '')
        if child_id == path:
            continue
        child_label = item.rstrip('/').split('/')[-1]
        if item.endswith(JSON_FILE):
            manifest = dict()
            manifest["label"] = props['labelFn'](child_label)
            manifest[id_property] = child_id
            manifest[type_property] = props['manifest']
            result[props['manifests']].append(manifest)
        else:
            sub_collection = dict()
            sub_collection["label"] = props['labelFn'](child_label)
            sub_collection[id_property] = child_id
            sub_collection[type_property] = props['collection']
            result[props['collections']].append(sub_collection)
    return result
