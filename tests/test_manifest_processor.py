from iiif_collection_server.manifest_processor import (
    check_extension_is_valid,
    check_is_jsonld,
    get_normalised_context,
    get_presentation_version,
    preprocess_manifest,
)
import pytest


def test_check_extension_is_valid():
    assert check_extension_is_valid('/some/test/path.json') is None
    assert check_extension_is_valid('/some/test/path.json-ld') is None
    assert check_extension_is_valid('/some/test/path.jsonld') is None
    with pytest.raises(ValueError):
        check_extension_is_valid('/some/test/path.with.not.valid.extension')


def test_check_is_jsonld():
    json_ld_with_context = {"@context": "http://test.context.com/asd.json"}
    json_without_context = {}
    assert check_is_jsonld(json_ld_with_context) is None
    with pytest.raises(TypeError):
        check_is_jsonld(json_without_context)


def test_get_normalised_context():
    manifest_with_context_str = {"@context": "http://test.context.com/asd.json"}
    manifest_with_context_array = {"@context": ["http://test.context.com/asd.json"]}
    assert type(get_normalised_context(manifest_with_context_str)) == list
    assert len(get_normalised_context(manifest_with_context_str)) == 1
    assert get_normalised_context(manifest_with_context_str)[0] == "http://test.context.com/asd.json"
    assert type(get_normalised_context(manifest_with_context_array)) == list
    assert len(get_normalised_context(manifest_with_context_array)) == 1
    assert get_normalised_context(manifest_with_context_array)[0] == "http://test.context.com/asd.json"


def test_get_presentation_version():
    manifest_presentation_version_1 = "http://www.shared-canvas.org/ns/context.json"
    manifest_presentation_version_1_v2 = "https://www.shared-canvas.org/ns/context.json"
    manifest_presentation_version_2 = "http://iiif.io/api/presentation/2/context.json"
    manifest_presentation_version_2_v2 = "https://iiif.io/api/presentation/2/context.json"
    manifest_presentation_version_3 = "http://iiif.io/api/presentation/3/context.json"
    manifest_presentation_version_3_v2 = "https://iiif.io/api/presentation/3/context.json"
    assert get_presentation_version(manifest_presentation_version_1) == 1
    assert get_presentation_version(manifest_presentation_version_1_v2) == 1
    assert get_presentation_version(manifest_presentation_version_2) == 2
    assert get_presentation_version(manifest_presentation_version_2_v2) == 2
    assert get_presentation_version(manifest_presentation_version_3) == 3
    assert get_presentation_version(manifest_presentation_version_3_v2) == 3


def test_preprocess_manifest():
    minimal_manifest_str = """
    {
        "@context": [
            "http://iiif.io/api/presentation/3/context.json"
        ],
        "id": "http://example.com/iiif/maniests/example1.json",
        "type": "Manifest",
        "items": []
    }
    """
    minimal_manifest_path = '/iiif/maniests/example1.json'
    minimal_manifest_url = 'http://example.com/iiif/maniests/example1.json-ld'
    result_manifest = preprocess_manifest(minimal_manifest_url, minimal_manifest_path, minimal_manifest_str)
    assert result_manifest ['id'] == minimal_manifest_url
