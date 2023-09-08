import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import sys

import time

from random import randint

font_dir = 'font-resources'

numbers = ['0', '1', '2']

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

test_sentence = ['S', 'i', 'n', 'g', 'a', 'p', 'o', 'r', 'i', 's', 'v', 'r', 'y', 'c', 'l', 'e', 'a', 'n', 'a', 'n',
                 'd', 's', 'a', 'f', 'e']

characters = input("Please Enter you sentence. I convert it into 32x32 jpg letters"
                   "(example: This is a beautiful morning. Isn't it?):")

white_colors = 255
black_colors = (0, 10, 20, 30)
gray_colors = (135, 145, 155)

background_colors = white_colors
background_color = white_colors

small_sizes = (16, 20, 24)
medium_sizes = (20, 24, 28)
large_sizes = (32, 36, 40)

font_size = int(input("Please input the desired font size [recommended range:14~28] (example: 20): "))
font_index = int(input(
    "--------------Font Map --------------\n[0]: Helvetica\n[1]: Baskerville\n[2]: Times New Roman\n[3]: Bodoni72\n\
    [4]: Didot\n[5]: Futura\n[6]: Gill Sans\n[7]: Bembo\n[8]: Rockwell\n[9]: Franklin Gothic\
    \n----------------------------\n What is your desired font index (example:2)? "))
rotation_value = int(input("How much rotation do you wish to add? [recommended range -15 ~ 15] (example: -5): "))

rawsentence = ''.join([c for c in characters if c.isalpha() and (not c.isspace())])

out_dir = os.path.join("outputsentences",
                       rawsentence + "_fnt=" + str(font_index) + "_fntsz=" + str(font_size) + "_rotval=" +
                       str(rotation_value))
try:
    os.makedirs(out_dir)
except OSError as e:
    print(e, file=sys.stderr)
    pass
else:
    pass
out_dir = out_dir + os.sep

image_size = 32


def cleanup():
    if os.path.isfile(os.path.join(font_dir, '.DS_Store')):
        os.unlink(os.path.join(font_dir, '.DS_Store'))
    for file in os.listdir(out_dir):
        file_path = os.path.join(out_dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    return


def generateCharacters():
    k = 1
    for dirname, dirnames, filenames in os.walk(font_dir):
        for filename in filenames:
            if str(font_index).zfill(2) in filename:
                font_resource_file = os.path.join(dirname, filename)

                for c in characters:
                    if not (c.isalpha()):
                        continue
                    if c.isspace():
                        continue
                    character = str(c)

                    char_image = Image.new('L', (image_size, image_size), background_color)

                    draw = ImageDraw.Draw(char_image)

                    font = ImageFont.truetype(font_resource_file, font_size)

                    (font_width, font_height) = font.getbbox(character)[-2:]

                    x = (image_size - font_width) / 2

                    y = (image_size - font_height) / 2

                    draw.text((x, y), character, (245 - background_color) +
                              randint(0, 10), font=font)

                    file_name = out_dir + str(k).zfill(3) + character + filename + str(font_size) + '.jpg'

                    char_image.save(file_name)
                    time.sleep(0.01)
                    img = cv2.imread(file_name)
                    rows = img.shape[0]
                    cols = img.shape[1]

                    img_center = (cols / 2, rows / 2)
                    M = cv2.getRotationMatrix2D(img_center, rotation_value, 1)

                    rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))

                    cv2.imwrite(file_name, rotated)

                    print(file_name)

                    k = k + 1
    return


generateCharacters()
