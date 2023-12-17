# 64Bit_LED_Matrix_Stripes

SSH Pi login
sasch // sasch

# Running the demo:
Put this into the ssh terminal:
sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D0 --led-rows=64 --led-cols=64 --led-slowdown-gpio=1
sudo ./rpi-rgb-led-matrix/examples-api-use/ledcat -D0 --led-rows=64 --led-cols=64 --led-slowdown-gpio=1

sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D1 ./Pictures/Glurak.bmp --led-rows=64 --led-cols=64 --led-slowdown-gpio=1
sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D1 ./Pictures/Glurak.ppm --led-rows=64 --led-cols=64 --led-slowdown-gpio=1
sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D1 ./rpi-rgb-led-matrix/examples-api-use/runtext.ppm --led-rows=64 --led-cols=64 --led-slowdown-gpio=1

sudo ./rpi-rgb-led-matrix/examples-api-use/demo -D1 ./rpi-rgb-led-matrix/examples-api-use/Glurak.ppm --led-rows=64 --led-cols=64 --led-slowdown-gpio=1

sudo led-image-viewer –led-pixel-mapper=”U-mapper;Rotate:180″ –led-gpio-mapping=adafruit-hat –led-cols=64 –led-rows=64 ./Pictures/Glurak.bmp

sudo ./led-image-viewer  --led-gpio-mapping=adafruit-hat --led-rows=64 --led-cols=64 --led-slowdown-gpio=1 Glurak.bmp

