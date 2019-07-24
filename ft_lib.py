from __future__ import print_function

import datetime
import subprocess


def run_cmd(cmd):
    if '<' in cmd:
        out = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    else:
        out = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    stdout, _ = out.communicate()
    return stdout


def _write_to_file(contents, ext, perms='wb'):
    filename = '{:%Y-%m-%d-%H-%M--%s}.{}'.format(datetime.datetime.today(), ext)
    f = open(filename, perms)
    f.write(contents)
    f.close()
    return filename


def send_text(txt):
    filename = _write_to_file(txt, 'txt', perms='w')
    return run_cmd('./bin/send-text -O -f./fonts/6x10.bdf - < ' + filename)


def send_image(img):
    filename = _write_to_file(img, 'img')
    return run_cmd('./bin/send-image -g10x20+15+7 ' + filename)


def send_video(vid):
    filename = _write_to_file(vid, 'vid')
    return run_cmd('./bin/send-video ' + filename)
