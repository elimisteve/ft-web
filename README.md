# FT Web

FT Web is a user-friendly web app and API for
[Noisebridge](https://www.noisebridge.net)'s
[Flaschen-Taschen](https://www.noisebridge.net/wiki/Flaschen_Taschen)!


## End-user usage

### Web UI

If you are physically at Noisebridge...

1. Visit <http://pegasus.noise:4444/> in your favorite web browser

2. Type/upload the text, image (including GIFs), or video you want to see displayed on the FT

3. Look at the Flaschen-Taschen to watch your upload come to life! :tada:


### CLI

    export FT_WEB_BASE=http://pegasus.noise:4444

(When testing locally, use `http://127.0.0.1:4444` instead.)

Form POSTs:

    curl -X POST -F text='Hello, Noisebridge!' ${FT_WEB_BASE}/api/text

    curl -X POST -F image=@my_image_goes_here.png ${FT_WEB_BASE}/api/image

    curl -X POST -F video=@my_video.mp4 ${FT_WEB_BASE}/api/video

JSON POSTs:

    curl -X POST -H 'Content-Type: application/json' -d '{"text": "Hello, Noisebridge!"}' ${FT_WEB_BASE}/api/text

    curl -X POST -H 'Content-Type: application/json' -d '{"image": "'$(base64 my_image_goes_here.png | tr -d '\n')'"}' ${FT_WEB_BASE}/api/image

    (echo -n '{"video": "'; base64 example_video.mp4; echo '"}' ) | curl -X POST -H 'Content-Type: application/json' -d @- ${FT_WEB_BASE}/api/video

For full API docs, run

    curl ${FT_WEB_BASE}/api

To use CLI tools to speak the FT-specific UDP protocol directly (and
thus side-stepping this web UI and API), see
<https://www.noisebridge.net/wiki/Flaschen_Taschen#Network_protocol_and_Utilities_to_send_content>


### Building this app

On Debian-based Linux distros:

```
git clone https://github.com/hzeller/flaschen-taschen
cd flaschen-taschen/client
bash debian_make_all.sh

cd ../../

git clone https://github.com/elimisteve/ft-web ft-web
cd ft-web
mkdir bin
cp ../flaschen-taschen/client/send-{text,image,video} bin/

sudo apt-get install python3-pip
mkvirtualenv -p `which python3` ft-web  # requires virtualenvwrapper
pip3 install -r requirements.txt
python app.py
```

Now visit <http://127.0.0.1:4444/> .
