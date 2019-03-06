import json
import pytest
import boto3
from botocore.exceptions import ClientError
from moto import mock_s3


def test_delete_file():
    with mock_s3():
        bucket = 'test-bucket'
        path = 'test-collection/test-file.json'
        test_manifest_file_content = json.dumps({})

        conn = boto3.resource('s3', region_name='eu-west-1')
        conn.create_bucket(Bucket=bucket)
        
        conn.Object(bucket, path).put(Body=test_manifest_file_content)

        assert test_manifest_file_content == conn.Object(bucket, path).get()['Body'].read().decode('utf-8')

        from iiif_collection_server.s3 import delete_file
        
        delete_file(path)

        with pytest.raises(ClientError):
            conn.Object(bucket, path).get()['Body'].read().decode('utf-8')


def test_write_file():
    with mock_s3():
        bucket = 'test-bucket'
        path = 'test-collection/test-file.json'
        test_manifest_content = json.dumps({})

        conn = boto3.resource('s3', region_name='eu-west-1')
        conn.create_bucket(Bucket=bucket)
        
        with pytest.raises(ClientError):
            conn.Object(bucket, path).get()['Body'].read().decode('utf-8')
        
        from iiif_collection_server.s3 import write_file
        write_file(path, test_manifest_content)

        assert test_manifest_content == conn.Object(bucket, path).get()['Body'].read().decode('utf-8')


def test_write_file_json():
    with mock_s3():
        bucket = 'test-bucket'
        path = 'test-collection/test-file.json'
        test_manifest__bucket_content = json.dumps({})
        test_manifest_content = {}

        conn = boto3.resource('s3', region_name='eu-west-1')
        conn.create_bucket(Bucket=bucket)
        
        with pytest.raises(ClientError):
            conn.Object(bucket, path).get()['Body'].read().decode('utf-8')
        
        from iiif_collection_server.s3 import write_file
        write_file(path, test_manifest_content)

        assert test_manifest__bucket_content == conn.Object(bucket, path).get()['Body'].read().decode('utf-8')


def test_get_file():
    with mock_s3():
        bucket = 'test-bucket'
        path = 'test-collection/test-file.json'
        test_manifest_file_content = json.dumps({})

        conn = boto3.resource('s3', region_name='eu-west-1')
        conn.create_bucket(Bucket=bucket)
        
        conn.Object(bucket, path).put(Body=test_manifest_file_content)

        assert test_manifest_file_content == conn.Object(bucket, path).get()['Body'].read().decode('utf-8')

        from iiif_collection_server.s3 import get_file
        
        assert {} == get_file(path)


def test_get_list_of_files():
    with mock_s3():
        bucket = 'test-bucket'
        path = 'test-collection/'
        path1 = 'test-collection/test-file.json'
        path2 = 'test-collection/test-folder/test-file.json'
        test_manifest_file_content = json.dumps({})
        expected_result = [
            'test-collection/test-file.json',
            'test-collection/test-folder/'
        ]
        
        conn = boto3.resource('s3', region_name='eu-west-1')
        conn.create_bucket(Bucket=bucket)
        
        conn.Object(bucket, path1).put(Body=test_manifest_file_content)
        conn.Object(bucket, path2).put(Body=test_manifest_file_content)

        assert test_manifest_file_content == conn.Object(bucket, path1).get()['Body'].read().decode('utf-8')
        assert test_manifest_file_content == conn.Object(bucket, path2).get()['Body'].read().decode('utf-8')

        from iiif_collection_server.s3 import get_list_of_files
        
        assert expected_result == get_list_of_files(path)