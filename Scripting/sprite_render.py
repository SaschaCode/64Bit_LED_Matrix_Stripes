#!/usr/bin/env python
"""
     This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import time
from PIL import Image
import time
import os
import sys
import glob

from rgbmatrix import RGBMatrix, RGBMatrixOptions

#definitions
sprite_y = 0
matrix_height = 32

# How many times to repeat the animation
animations_repeats = 3

# We can customize the durations of each animation
# individually here. 
# animations durations
# based on the filename
# image-name: animation_time
animation_times = {
       "parrot.bmp": 0.08,
       "mario_punch.bmp": 0.1,
       "nyancat.bmp": 0.1,
       "mario_frog.bmp": 0.1,
       "megaman.bmp": 0.1,
       "sonic.bmp": 0.1
}

#directory with images location
images_location = "images"

#configuring the matrix options
options = RGBMatrixOptions()

options.rows = 32
options.cols = 32
options.hardware_mapping = 'adafruit-hat-pwm'
options.multiplexing = 6
options.led_rgb_sequence = 'BGR'

matrix = RGBMatrix(options = options)

matrix.Clear()

try:
   while True:
       # first loop - all images inside images location
       # sort through directory search for files
       images_sprites = glob.glob(images_location + '/*.bmp')
       for images in images_sprites:
           image = Image.open(images).convert('RGB')
           width, height = image.size
           for cur_anim in range (animations_repeats):
               #print ("Curr anim: {}".format(cur_anim))
               for sprite_y in range (0, height, 32):
                   cur_sprite = image.crop((0,sprite_y, 32, (sprite_y + 32)))
                   #cur_sprite.thumbnail((32,32), Image.ANTIALIAS)
                   matrix.SetImage(cur_sprite)
                   # wait the defined time in dictionary
                   # for current image
                   # The following line will match the image name
                   # to the time in the dictionary
                   # string slice to remove word images/ from location and will match
                   # the name in the dictionary
                   time.sleep(animation_times[images[7:]])

except KeyboardInterrupt:
   matrix.Clear()
   sys.exit(0)