from __future__ import print_function

import datetime
import os
import subprocess

VALID_EXTENSIONS = ('txt', 'text', 'img', 'image', 'vid', 'video')
THIS_DIR = os.path.dirname(os.path.realpath(__file__))


def run_cmd(cmd):
    if '<' in cmd:
        out = subprocess.Popen(cmd.split(),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    else:
        out = subprocess.Popen(cmd.split(),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    stdout, _ = out.communicate()
    return stdout


def _abs_path(path):
    return os.path.join(THIS_DIR, path)


def _write_to_file(contents, ext, perms='wb'):
    filename = '{:%Y-%m-%d-%H-%M--%s}.{}'.format(datetime.datetime.today(), ext)
    f = open(_abs_path(filename), perms)
    f.write(contents)
    f.close()
    return filename


def send(type_str, request):
    if type_str in ('txt', 'text'):
        data = request.form.get('txt') or request.form.get('text')
        return send_text(data)

    elif type_str in ('img', 'image'):
        data = request.files.get('img') or request.files.get('image')
        if data:
            return send_image(data.read())
        raise Exception('Got no image data! See /api for docs.')

    elif type_str in ('vid', 'video',):
        data = request.files.get('vid') or request.files.get('video')
        if data:
            return send_video(data.read())
        raise Exception('Got no video data! See /api for docs.')

    raise Exception('type_str not in ' + ', '.join(VALID_EXTENSIONS))


def send_text(txt):
    filename = _write_to_file(txt, 'txt', perms='w')
    return run_cmd('./bin/send-text -h ft.noise:1337 -O -f./fonts/6x10.bdf ' +
                   _abs_path(filename))


def send_image(img):
    filename = _write_to_file(img, 'img')
    return run_cmd('./bin/send-image -h ft.noise:1337 -g10x20+15+7 ' +
                   _abs_path(filename))


def send_video(vid):
    filename = _write_to_file(vid, 'vid')
    return run_cmd('./bin/send-video -h ft.noise:1337 ' +
                   _abs_path(filename))
