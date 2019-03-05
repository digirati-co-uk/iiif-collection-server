
JSON_FILE = ('.json', '.jsonld', '.json-ld')
DEFAULT_PROPS = {
  "p2": {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "id": "@id",
    "type": "@type",
    "manifest": "sc:Manifest",
    "collection": "sc:Collection",
    "collections": "collections",
    "manifests": "manifests",
    "labelFn": lambda label : label,
  },
  "p3": {
    "@context": [
      "http://iiif.io/api/presentation/3/context.json",
    ],
    "id": "id",
    "type": "type",
    "manifest": "Manifest",
    "collection": "Collection",
    "collections": "items",
    "manifests": "items",
    "labelFn": lambda label : { "en": [label]},
  }
}