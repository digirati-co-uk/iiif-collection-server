# IIIF Collection Server

This is a reference implementation for a IIIF Collection server outputting IIIF Presentation v3 collections.

## Installing for local development

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

Install the the python packages required for the porject.

```
(venv)$ cd app
(venv)$ pip install -r requirements.txt
```

See the configuration section for detailed configuration.

Run the app locally:

```
(venv)$ python collection_server.py
```

The app will run at:

[http://127.0.0.1:8181/p3/](http://127.0.0.1:8181/p3/)


## Configuration

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

