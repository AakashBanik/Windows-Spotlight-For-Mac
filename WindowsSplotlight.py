import requests
import json
import subprocess
from appscript import app, mactypes
from PIL import Image, ImageDraw
import os

url = 'https://arc.msn.com/v3/Delivery/Placement?pid=209567&fmt=json&rafb=0&ua=WindowsShellClient%2F0&cdm=1&disphorzres=9999&dispvertres=9999&lo=80217&pl=en-US&lc=en-US&ctry=us%22;'

resp = requests.get(url)
j = json.loads(resp.json()['batchrsp']['items'][0]['item'])
link = j['ad']['image_fullscreen_001_landscape']['u']

img_data = requests.get(link).content
with open('spotlight-org.jpg', 'wb') as img:
    img.write(img_data)

img = Image.open('spotlight-org.jpg').convert('RGB')
tint = Image.new("RGB", (img.size), color=(0,0,0))
new_image = Image.blend(img, tint, 0.3)

new_image.save('spotlight.jpg')

os.remove('spotlight-org.jpg')

app('Finder').desktop_picture.set(mactypes.File('spotlight.jpg'))