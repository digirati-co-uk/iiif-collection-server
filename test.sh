#!/bin/bash

[[ -d venv ]] || python3 -m venv ./venv

source venv/bin/activate

pip install -r requirements.txt -r requirements.test.txt

export COLLECTION_SERVER_S3_BUCKET=test-bucket
export COLLECTION_SERVER_S3_BASE_PREFIX=test-collection
export COLLECTION_SERVER_S3_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxx
export COLLECTION_SERVER_S3_SECRET_KEY=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

pytest --capture=sys -vv --cov=iiif_collection_server tests/

deactivate
