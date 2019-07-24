from __future__ import print_function

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.url_map.strict_slashes = False

import ft_lib  # ./ft_lib.py
import subprocess


DEFAULT_BASE_URL = 'http://pegasus.noise:4444'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['OPTIONS'])
@app.route('/api', methods=['GET', 'OPTIONS'])
def api_options():
    return app.response_class(
        mimetype='text/plain',
        response='''How to use the /api/text, /api/image, and /api/video API endpoints:

    $ curl -X POST -F text='Hello, Noisebridge!' {base_url}/api/text

    $ curl -X POST -F image=@my_image.png {base_url}/api/image

    $ curl -X POST -F video=@my_video.mp4 {base_url}/api/video

Or send JSON rather than form-encoded data:

    $ curl -X POST -H 'Content-Type: application/json' -d '{"text": "Hello, Noisebridge!"}' {base_url}/api/text

    $ curl -X POST -H 'Content-Type: application/json' -d '{"image": "'$(base64 my_image.png | tr -d '\n')'"}' {base_url}/api/image

    $ (echo -n '{"video": "'; base64 my_video.mp4; echo '"}' ) | curl -X POST -H 'Content-Type: application/json' -d @- {base_url}/api/video
'''.format(base_url=DEFAULT_BASE_URL)
    )


@app.route('/api/<data_type>', methods=['POST'])
def api(data_type):
    try:
        output = ft_lib.send(data_type, request)
    except Exception as e:
        print('Error:', e)
        return jsonify({"error": str(e)})

    return jsonify({"output": output.decode('utf-8')})


if __name__ == '__main__':
    app.run('0.0.0.0', 4444)
