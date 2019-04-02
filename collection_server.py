from flask import (
  Flask,
  request,
  jsonify,
)
import flask
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from iiif_collection_server.settings import BASE_FOLDER
from iiif_collection_server.constants import JSON_FILE
from iiif_collection_server.iiif_serializer import collection_serializer
from iiif_collection_server.manifest_processor import preprocess_manifest
from iiif_collection_server.s3 import write_file, get_list_of_files, get_file, delete_file


__version__ = "0.0.1"

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
CORS(app)

print('flask.__version__', flask.__version__)
print('Collection Server')


def first_url(request_url):
    '''
    if request url passed by a proxy as a coma separated list this 
    should handle the situation.
    Note: Unfortunately it is not tested because, I haven't been able to 
    reproduce this issue on my servers
    '''
    if type(request_url) in [list, tuple] and len(request_url) > 0:
        return request_url[0]
    elif type(request_url) == str:
        urls = request_url.split(', ')
        if len(urls) > 0:
            return urls[0]
        else:
            return request_url
    else:
        raise ValueError('invalid request url: ' + request_url)


def get_path(path):
    s3_location = '/'.join([BASE_FOLDER, path]) if path != '' else BASE_FOLDER
    version = request.path.replace(path,'').replace('/','')
    if path.endswith(JSON_FILE):
        if request.method in ['POST', 'PUT']:
            data = request.get_data()
            manifest = preprocess_manifest(request.url, path, data)
            write_file(s3_location, manifest)
        elif request.method == "DELETE":
            try: 
                delete_file(s3_location)
            except Exception as ex:
                return jsonify({ "error": str(ex) })
            return jsonify({ "message": "manifest deleted" })
        return jsonify(get_file(s3_location))

    s3_location_contents = get_list_of_files(s3_location)
    request_url = first_url(request.url)
    iiif_collection = collection_serializer(
        request_url.replace(path, ''),
        request_url,
        s3_location_contents,
        version=version
    )
    return jsonify(iiif_collection)


@app.errorhandler(404)
def requested_item_not_found(e):
    return jsonify(
        error=404,
        message="the requested item not found the root collection starts at " + ''.join([request.host_url, 'p3'])
    ), 404


@app.errorhandler(500)
def requested_item_not_found2(e):
    return jsonify(
        error=500,
        message="the requested item not found the root collection starts at " + ''.join([request.host_url, 'p3'])
    ), 500


@app.route('/p3/', methods=['GET'], defaults={'path': ''})
@app.route('/p3/<path:path>', methods=['GET', 'POST','PUT', 'DELETE'])
def get_presentation_v3_path(path):
    return get_path(path)


@app.route('/p2/', methods=['GET'], defaults={'path': ''})
@app.route('/p2/<path:path>', methods=['GET', 'POST','PUT', 'DELETE'])
def get_presentation_v2_path(path):
    return get_path(path)


# NOTE: This is only for local development
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 8181, app, use_reloader=True, use_debugger=True)
