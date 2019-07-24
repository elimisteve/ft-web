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

    curl -X POST -F text='Hello, Noisebridge!' http://pegasus.noise/api/text

    curl -X POST -F image=@my_image_goes_here.png http://pegasus.noise/api/image

    curl -X POST -F video=@my_video.mp4 http://pegasus.noise/api/video

For full API docs, run

    curl http://pegasus.noise:4444/api

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
