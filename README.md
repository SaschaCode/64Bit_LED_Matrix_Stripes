# 64Bit_LED_Matrix_Stripes

SSH Pi login
sasch // sasch

## Running the demo:

Put this into the ssh terminal:
sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D0 --led-rows=64 --led-cols=64 --led-slowdown-gpio=1

## Display a single image

sudo ./led-image-viewer  --led-gpio-mapping=adafruit-hat --led-rows=64 --led-cols=64 --led-slowdown-gpio=1 Glurak.bmp
sudo /home/sasch/rpi-rgb-led-matrix/utils/led-image-viewer  --led-gpio-mapping=adafruit-hat --led-rows=64 --led-cols=64 --led-slowdown-gpio=1 Glurak.bmp

## Dipslay all images in a folder in shuffle

Runs the imageviewer and displays all images (bmp) in /home/Sasch/Pictures/ in a shuffle loop. Every picture is displayed for 3 seconds
'sudo /home/sasch/rpi-rgb-led-matrix/utils/led-image-viewer -f -s -w3 --led-gpio-mapping=adafruit-hat --led-rows=64 --led-cols=64 --led-slowdown-gpio=1 /home/sasch/Pictures/*.bmp'

## Auto Execution

We run the '/home/sasch/Documents/led_shuffle_all_bmps.sh on startup. This means, the Pi will be locked with this script and SSH is not working
To exit thise mode connect with the filezila and rename the script. Afterwards restart the PI by KL30. SSH should be up again.

## Download sides =)

https://pokemondb.net/sprites
