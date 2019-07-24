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
@app.route('/api')
def api_options():
    return app.response_class(
        mimetype='text/plain',
        response='''How to use the /api/text, /api/image, and /api/video API endpoints:

$ curl -X POST -d 'Hello, Noisebridge!' {base_url}/api/text

$ curl -X POST -d @my_image.png {base_url}/api/image

$ curl -X POST -d @my_video.mp4 {base_url}/api/video
'''.format(base_url=DEFAULT_BASE_URL)
    )


@app.route('/api/<data_type>', methods=['POST'])
def api(data_type):
    assert data_type in ('txt', 'text', 'img', 'image', 'video')

    if data_type in ('txt', 'text'):
        try:
            output = ft_lib.send_text('FAKE DEMO TEXT\n')
        except Exception as e:
            return jsonify({"error": str(e)})
        return jsonify({"output": output.decode('utf-8')})


if __name__ == '__main__':
    app.run('0.0.0.0', 4444)
