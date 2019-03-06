from iiif_collection_server.constants import JSON_FILE, DEFAULT_PROPS


def test_constants_json_file_types():
    assert '.json' in JSON_FILE
    assert '.json-ld' in JSON_FILE
    assert '.jsonld' in JSON_FILE


def test_presentation_version_2_constants():
    assert DEFAULT_PROPS["p2"]["@context"] == "http://iiif.io/api/presentation/2/context.json"
    assert DEFAULT_PROPS["p2"]["id"] == "@id"
    assert DEFAULT_PROPS["p2"]["type"] == "@type"
    assert DEFAULT_PROPS["p2"]["manifest"] == "sc:Manifest"
    assert DEFAULT_PROPS["p2"]["collection"] == "sc:Collection"
    assert DEFAULT_PROPS["p2"]["collections"] == "collections"
    assert DEFAULT_PROPS["p2"]["manifests"] == "manifests"
    assert DEFAULT_PROPS["p2"]["labelFn"]('test label') == 'test label'
    

def test_presentation_version_3_constants():
    assert type(DEFAULT_PROPS["p3"]["@context"]) == list
    assert len(DEFAULT_PROPS["p3"]["@context"]) == 1
    assert DEFAULT_PROPS["p3"]["@context"][0] == "http://iiif.io/api/presentation/3/context.json"
    assert DEFAULT_PROPS["p3"]["id"] == "id"
    assert DEFAULT_PROPS["p3"]["type"] == "type"
    assert DEFAULT_PROPS["p3"]["manifest"] == "Manifest"
    assert DEFAULT_PROPS["p3"]["collection"] == "Collection"
    assert DEFAULT_PROPS["p3"]["collections"] == "items"
    assert DEFAULT_PROPS["p3"]["manifests"] == "items"
    assert type(DEFAULT_PROPS["p3"]["labelFn"]('test label')) == dict
    assert 'en' in DEFAULT_PROPS["p3"]["labelFn"]('test label')
    assert type(DEFAULT_PROPS["p3"]["labelFn"]('test label')['en']) == list
