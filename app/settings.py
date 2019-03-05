import os

BUCKET_NAME =  str.split(os.environ.get('COLLECTION_SERVER_S3_BUCKET'))
BASE_FOLDER = str.split(os.environ.get('COLLECTION_SERVER_S3_BASE_PREFIX'))
ACCESS_KEY = str.split(os.environ.get('COLLECTION_SERVER_S3_ACCESS_KEY')) 
SECRET_KEY = str.split(os.environ.get('COLLECTION_SERVER_S3_SECRET_KEY'))