from flask import (
  Flask,
  request,
  jsonify,
  json, 
  current_app
)
import flask
from flask_cors import CORS
from path_resolver import get_path
from manifest_processor import preprocess_manifest
from s3 import write_file
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
CORS(app)

print('flask.__version__', flask.__version__)
print('Collection Server')


@app.errorhandler(404)
def requested_item_not_found(e):
  return jsonify(
    error=404,
    message= "the requested item not found the root collection starts at " + ''.join([request.host_url, 'p3'])
  ), 404

@app.errorhandler(500)
def requested_item_not_found2(e):
  return jsonify(
    error=500,
    message= "the requested item not found the root collection starts at " + ''.join([request.host_url, 'p3'])
  ), 500


@app.route('/p3/', methods=['GET', 'POST'])
def display_root_collection():
  return jsonify(get_path(''))


@app.route('/p3/<path:path>', methods=['GET', 'POST','PUT'])
def display_collection(path):
  if request.method in ['POST', 'PUT']:
    data = request.get_data()
    manifest = preprocess_manifest(path, data)
    write_file(path, manifest)
  return jsonify(get_path(path))


# TODO
# @app.route('/p2/', methods=['GET', 'POST'])
# def display_root_collection_p2():
#   return jsonify(get_path(''))


# @app.route('/p2/<path:path>', methods=['GET', 'POST'])
# def display_collection_p2(path):
#   return jsonify(get_path(path))


# NOTE: This is only for local development
if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('0.0.0.0', 8181, app, use_reloader=True, use_debugger=True)
