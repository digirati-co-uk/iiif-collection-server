# IIIF Collection Server

[![Build Status](https://travis-ci.com/digirati-co-uk/iiif-collection-server.svg?token=Jte42dszspRtC2NURDp5&branch=master)](https://travis-ci.com/digirati-co-uk/iiif-collection-server)


This is a reference implementation for a IIIF Collection server outputting IIIF Presentation v3 collections.

**Demo:**

[https://iiif-collection.ch.digtest.co.uk/](https://iiif-collection.ch.digtest.co.uk/)


## Installing for local development

**Pre-requirements:** 

- python 3.4+
- pip 18+
- virtualenv 15+

**Installation steps:**

Clone the git repository to your local machine:

```
$ git clone git@github.com:digirati-co-uk/iiif-collection-server.git
```

Change directory to the cloned repository.

```
$ cd iiif-collection-server
```

Create a virtual environment using python 3:

```
$ which python3
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
$ virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 venv
```

*NOTE:* you need pass the path, from output of the first command, to the second command -p argument.

Activate the virtual environment:

```
$ source venv/bin/activate
```

Install the the python packages required for the project.

```
(venv)$ cd iiif-collection-server
(venv)$ pip install -r requirements.txt
```

See the configuration section for environment variable requirements.

To run the app locally:

```
(venv)$ python collection_server.py
```

The app will run at:

[http://127.0.0.1:8181/p3/](http://127.0.0.1:8181/p3/)


## Configuration

| Environment Variable | Description |
|-----|----|
| COLLECTION_SERVER_S3_BUCKET | Amazon S3 bucket used for persistance |
| COLLECTION_SERVER_S3_BASE_PREFIX | The service can start from a subfolder/prefix |
| COLLECTION_SERVER_S3_ACCESS_KEY | Amazon S3 access key|
| COLLECTION_SERVER_S3_SECRET_KEY | Amazon S3 secret key|

Use export on linux based systems for example :

```
export COLLECTION_SERVER_S3_BUCKET=dlcs-dlcservices-test-ingest
```

On windows based systems:

```
set COLLECTION_SERVER_S3_BUCKET=dlcs-dlcservices-test-ingest
```

## API

**Get collection or manifest**:

GET **/p3/\<path>**

Example response for a collection:

```json
{
  "@context": [
    "http://iiif.io/api/presentation/3/context.json"
  ],
  "id": "http://iiif-collection.ch.digtest.co.uk/p3/",
  "items": [
    {
      "id": "http://iiif-collection.ch.digtest.co.uk/p3/live/",
      "label": {
        "en": [
          "live"
        ]
      },
      "type": "Collection"
    },
    {
      "id": "http://iiif-collection.ch.digtest.co.uk/p3/manifest.json",
      "label": {
        "en": [
          "manifest.json"
        ]
      },
      "type": "Manifest"
    },
    {
      "id": "http://iiif-collection.ch.digtest.co.uk/p3/qa/",
      "label": {
        "en": [
          "qa"
        ]
      },
      "type": "Collection"
    },
    {
      "id": "http://iiif-collection.ch.digtest.co.uk/p3/staging/",
      "label": {
        "en": [
          "staging"
        ]
      },
      "type": "Collection"
    }
  ],
  "label": {
    "en": [
      "p3"
    ]
  },
  "type": "Collection"
}
```


**Add or update a manifest**:

POST **/p3/\<path>/\<manifest>.{json|json-ld|jsonld}**

request body is the manifest jsonld
Content-Type: application/json

**Delete a manifest**:

DELETE **/p3/\<path>/\<manifest>.{json|json-ld|jsonld}**



# References

[IIIF Presentation v3](https://iiif.io/api/presentation/3.0/)
