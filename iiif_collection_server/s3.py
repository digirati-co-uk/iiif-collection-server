import os
import json
from operator import attrgetter
from collections import namedtuple
from boto3.session import Session

from iiif_collection_server.settings import (
    BUCKET_NAME,
    BASE_FOLDER,
    ACCESS_KEY,
    SECRET_KEY,
)

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)

client = session.client('s3')


def get_list_of_files(path):
    kwargs = dict()
    kwargs.update(Delimiter='/')
    if not path.endswith('/'):
        path += '/'
    kwargs.update(Prefix=path)
    paginator = client.get_paginator('list_objects')
    result = []
    for resp in paginator.paginate(Bucket=BUCKET_NAME, **kwargs):
        q = []
        if 'CommonPrefixes' in resp:
            q = [f['Prefix'] for f in resp['CommonPrefixes']]
        if 'Contents' in resp:
            q += [f['Key'] for f in resp['Contents']]
        result = sorted(q)
    return result


def get_file(path):
    obj = client.get_object(Bucket=BUCKET_NAME, Key=path)
    return json.loads(obj['Body'].read().decode('utf-8'))


def write_file(path, body):
    body = body if type(body) == str else json.dumps(body)
    client.put_object(Bucket=BUCKET_NAME, Key=path, Body=body)


def delete_file(path):
    client.delete_object(Bucket=BUCKET_NAME, Key=path)
