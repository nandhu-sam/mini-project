#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:29:41 2019

@author: saeedeh
"""
from keras.models import load_model
import glob
import numpy as np
from keras.preprocessing import image
import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import gc

Counter_Font_00 = 0
Counter_Font_01 = 0
Counter_Font_02 = 0
Counter_Font_03 = 0
Counter_Font_04 = 0
Counter_Font_05 = 0
Counter_Font_06 = 0
Counter_Font_07 = 0
Counter_Font_08 = 0
Counter_Font_09 = 0


def Font_prediction(char, fontResult):
    global Counter_Font_00
    global Counter_Font_01
    global Counter_Font_02
    global Counter_Font_03
    global Counter_Font_04
    global Counter_Font_05
    global Counter_Font_06
    global Counter_Font_07
    global Counter_Font_08
    global Counter_Font_09
    if fontResult[0][0] == 1:
        Counter_Font_00 = Counter_Font_00 + 1
        print('Char ' + char + ', Font 00')
    elif fontResult[0][1] == 1:
        Counter_Font_01 = Counter_Font_01 + 1
        print('Char ' + char + ', Font 01')
    elif fontResult[0][2] == 1:
        Counter_Font_02 = Counter_Font_02 + 1
        print('Char ' + char + ', Font 02')
    elif fontResult[0][3] == 1:
        Counter_Font_03 = Counter_Font_03 + 1
        print('Char ' + char + ', Font 03')
    elif fontResult[0][4] == 1:
        Counter_Font_04 = Counter_Font_04 + 1
        print('Char ' + char + ', Font 04')
    elif fontResult[0][5] == 1:
        Counter_Font_05 = Counter_Font_05 + 1
        print('Char ' + char + ', Font 05')
    elif fontResult[0][6] == 1:
        Counter_Font_06 = Counter_Font_06 + 1
        print('Char ' + char + ', Font 06')
    elif fontResult[0][7] == 1:
        Counter_Font_07 = Counter_Font_07 + 1
        print('Char ' + char + ', Font 07')
    elif fontResult[0][8] == 1:
        Counter_Font_08 = Counter_Font_08 + 1
        print('Char ' + char + ', Font 08')
    elif fontResult[0][9] == 1:
        Counter_Font_09 = Counter_Font_09 + 1
        print('Char' + char + ', Font 09')


def main():
    global Counter_Font_00
    global Counter_Font_01
    global Counter_Font_02
    global Counter_Font_03
    global Counter_Font_04
    global Counter_Font_05
    global Counter_Font_06
    global Counter_Font_07
    global Counter_Font_08
    global Counter_Font_09
    print("Loading (1/44), Please wait... ")
    Char_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Alphabets/AlphabetResults/Good_Alphabet_bz=32_e=500_spe=700_vs=140.h5')
    print("Loading (2/44), Please wait... ")
    Font_A_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/A/Results/Good_A_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (3/44), Please wait... ")
    Font_a_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/a-s/Results/Good_a-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (4/44), Please wait... ")
    Font_B_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/B/Results/Good_B_ne=32_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (5/44), Please wait... ")
    Font_b_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/b-s/Results/Good_b-s_ne=64_bz=32_e=30_spe=50_vs=14.h5')
    print("Loading (6/44), Please wait... ")
    Font_Cc_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Cc/Results/Good_Cc_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (7/44), Please wait... ")
    Font_D_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/D/Results/Good_D_ne=128_bz=32_e=20_spe=70_vs=14.h5')
    print("Loading (8/44), Please wait... ")
    Font_d_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/d-s/Results/Good_d-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (9/44), Please wait... ")
    Font_E_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/E/Results/Good_E_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (10/44), Please wait... ")
    Font_e_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/e-s/Results/Good_e-s_ne=64_bz=32_e=20_spe=70_vs=15.h5')
    print("Loading (11/44), Please wait... ")
    Font_F_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/F/Results/Good_F_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (12/44), Please wait... ")
    Font_f_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/f-s/Results/Good_f-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (13/44), Please wait... ")
    Font_G_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/G/Results/Good_G_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (14/44), Please wait... ")
    Font_g_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/g-s/Results/Good_g-s_ne=128_bz=32_e=50_spe=70_vs=15.h5')
    print("Loading (15/44), Please wait... ")
    Font_H_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/H/Results/Good_H_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (16/44), Please wait... ")
    Font_h_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/h-s/Results/Good_h-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (17/44), Please wait... ")
    Font_I_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/I/Results/Good_I_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (18/44), Please wait... ")
    Font_i_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/i-s/Results/Good_i-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (19/44), Please wait... ")
    Font_J_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/J/Results/Good_J_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (20/44), Please wait... ")
    Font_j_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/j-s/Results/Good_j-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (21/44), Please wait... ")
    Font_Kk_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Kk/Results/Good_Kk_ne=32_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (22/44), Please wait... ")
    Font_L_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/L/Results/Good_L_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (23/44), Please wait... ")
    Font_l_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/l-s/Results/Good_l-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (24/44), Please wait... ")
    Font_M_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/M/Results/Good_M_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (25/44), Please wait... ")
    Font_m_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/m-s/Results/Good_m-s_ne=32_bz=32_e=50_spe=70_vs=14.h5')
    print("Loading (26/44), Please wait... ")
    Font_N_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/N/Results/Good_N_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (27/44), Please wait... ")
    Font_n_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/n-s/Results/Good_n-s_ne=128_bz=32_e=20_spe=50_vs=14.h5')
    print("Loading (28/44), Please wait... ")
    Font_Oo_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Oo/Results/Good_Oo_ne=128_bz=32_e=50_spe=70_vs=14.h5')
    print("Loading (29/44), Please wait... ")
    Font_Pp_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Pp/Results/Good_Pp_ne=64_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (30/44), Please wait... ")
    Font_Q_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Q/Results/Good_Q_ne=64_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (31/44), Please wait... ")
    Font_q_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/q-s/Results/Good_q-s_ne=128_bz=32_e=50_spe=50_vs=14.h5')
    print("Loading (32/44), Please wait... ")
    Font_R_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/R/Results/Good_R_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (33/44), Please wait... ")
    Font_r_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/r-s/Results/Good_r-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (34/44), Please wait... ")
    Font_Ss_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Ss/Results/Good_Ss_ne=64_bz=32_e=50_spe=70_vs=14.h5')
    print("Loading (35/44), Please wait... ")
    Font_T_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/T/Results/Good_T_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (36/44), Please wait... ")
    Font_t_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/t-s/Results/Good_t-s_ne=128_bz=32_e=50_spe=70_vs=14.h5')
    print("Loading (37/44), Please wait... ")
    Font_U_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/U/Results/Good_U_ne=128_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (38/44), Please wait... ")
    Font_u_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/u-s/Results/Good_u-s_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (39/44), Please wait... ")
    Font_Vv_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Vv/Results/Good_Vv_ne=128_bz=32_e=50_spe=50_vs=14.h5')
    print("Loading (40/44), Please wait... ")
    Font_Ww_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Ww/Results/Good_Ww_ne=128_bz=32_e=50_spe=50_vs=14.h5')
    print("Loading (41/44), Please wait... ")
    Font_Xx_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Xx/Results/Good_Xx_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (42/44), Please wait... ")
    Font_Y_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Y/Results/Good_Y_ne=128_bz=32_e=500_spe=70_vs=14.h5')
    print("Loading (43/44), Please wait... ")
    Font_y_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/y-s/Results/Good_y-s_ne=128_bz=32_e=30_spe=70_vs=14.h5')
    print("Loading (44/44), Please wait... ")
    Font_Zz_Model = load_model(
        '/Users/saeedeh/Desktop/Alphabet pics/Fonts/Zz/Results/Good_Zz_ne=128_bz=32_e=30_spe=70_vs=14.h5')

    file1 = open('/Users/saeedeh/Desktop/fontrecognizeroutputs.txt', "w")

    while True:
        gc.collect()
        ''' --------------- '''
        font_dir = '../font-resources'
        characters = input("Please Enter you sentence. I convert it into 32x32 jpg letters"
                           "(example: This is a beautiful morning. Isn't it?):")
        background_color = 255
        font_size = int(input("Please input the desired font size [recommended range:14~28] (example: 20): "))
        font_index = int(input("--------------Font Map --------------\n"
                               "[0]: Helvetica\n"
                               "[1]: Baskerville\n"
                               "[2]: Times New Roman\n"
                               "[3]: Bodoni72\n"
                               "[4]: Didot\n"
                               "[5]: Futura\n"
                               "[6]: Gill Sans\n"
                               "[7]: Bembo\n"
                               "[8]: Rockwell\n"
                               "[9]: Franklin Gothic\n"
                               "----------------------------\n"
                               " What is your desired font index (example:2)? "))
        rotation_value = int(
            input("How much rotation do you wish to add? [recommended range -15 ~ 15] (example: -5): "))

        rawsentence = ''.join([c for c in characters if c.isalpha() and (not c.isspace())])[0:15]

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

        file1.write(str(characters) + '\t')
        file1.write(str(font_size) + '\t')
        file1.write(str(font_index) + '\t')
        file1.write(str(rotation_value) + '\t')

        image_size = 32

        k = 1
        for dirname, dirnames, filenames in os.walk(font_dir):
            for filename in filenames:
                if str(font_index).zfill(2) in filename:
                    font_resource_file = os.path.join(dirname, filename)
                    # For each character do
                    for char in characters:
                        if not (char.isalpha()):
                            continue
                        if char.isspace():
                            continue
                        character = str(char)
                        char_image = Image.new('L', (32, 32), background_color)
                        draw = ImageDraw.Draw(char_image)
                        font = ImageFont.truetype(font_resource_file, font_size)
                        (font_width, font_height) = font.getbbox(character)[-2:]
                        x = (image_size - font_width) / 2
                        y = (image_size - font_height) / 2
                        draw.text((x, y), character, 0, font=font)
                        file_name = out_dir + str(k).zfill(3) + character + filename + str(font_size) + '.jpg'
                        char_image.save(file_name)
                        img = cv2.imread(file_name)
                        rows = img.shape[0]
                        cols = img.shape[1]
                        img_center = (cols / 2, rows / 2)
                        M = cv2.getRotationMatrix2D(img_center, rotation_value, 1)
                        rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
                        cv2.imwrite(file_name, rotated)
                        print(file_name)
                        k = k + 1

        ''' -------------- '''
        if characters == 'q':
            break
        else:
            # letter_list=glob.glob('/Users/saeedeh/Desktop/Futura/*.jpg')
            letter_list = glob.glob(out_dir + '/*.jpg')
            if len(letter_list) == 0:
                print("Invalid address or address contains no file.")
                continue

            Counter_Font_00 = 0
            Counter_Font_01 = 0
            Counter_Font_02 = 0
            Counter_Font_03 = 0
            Counter_Font_04 = 0
            Counter_Font_05 = 0
            Counter_Font_06 = 0
            Counter_Font_07 = 0
            Counter_Font_08 = 0
            Counter_Font_09 = 0
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("--------------Result --------------")
            for img in letter_list:
                test_image = image.load_img(img, target_size=(32, 32))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                result = Char_Model.predict(test_image)
                if result[0][0] == 1:
                    char = 'A'
                    fontResult = Font_A_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][1] == 1:
                    char = 'a'
                    fontResult = Font_a_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][2] == 1:
                    char = 'B'
                    fontResult = Font_B_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][3] == 1:
                    char = 'b'
                    fontResult = Font_b_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][4] == 1:
                    char = 'Cc'
                    fontResult = Font_Cc_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][5] == 1:
                    char = 'D'
                    fontResult = Font_D_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][6] == 1:
                    char = 'd'
                    fontResult = Font_d_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][7] == 1:
                    char = 'E'
                    fontResult = Font_E_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][8] == 1:
                    char = 'e'
                    fontResult = Font_e_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][9] == 1:
                    char = 'F'
                    fontResult = Font_F_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][10] == 1:
                    char = 'f'
                    fontResult = Font_f_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][11] == 1:
                    char = 'G'
                    fontResult = Font_G_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][12] == 1:
                    char = 'g'
                    fontResult = Font_g_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][13] == 1:
                    char = 'H'
                    fontResult = Font_H_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][14] == 1:
                    char = 'h'
                    fontResult = Font_h_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][15] == 1:
                    char = 'I'
                    fontResult = Font_I_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][16] == 1:
                    char = 'i'
                    fontResult = Font_i_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][17] == 1:
                    char = 'J'
                    fontResult = Font_J_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][18] == 1:
                    char = 'j'
                    fontResult = Font_j_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][19] == 1:
                    char = 'Kk'
                    fontResult = Font_Kk_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][20] == 1:
                    char = 'L'
                    fontResult = Font_L_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][21] == 1:
                    char = 'l'
                    fontResult = Font_l_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][22] == 1:
                    char = 'M'
                    fontResult = Font_M_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][23] == 1:
                    char = 'm'
                    fontResult = Font_m_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][24] == 1:
                    char = 'N'
                    fontResult = Font_N_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][25] == 1:
                    char = 'n'
                    fontResult = Font_n_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][26] == 1:
                    char = 'Oo'
                    fontResult = Font_Oo_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][27] == 1:
                    char = 'Pp'
                    fontResult = Font_Pp_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][28] == 1:
                    char = 'Q'
                    fontResult = Font_Q_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][29] == 1:
                    char = 'q'
                    fontResult = Font_q_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][30] == 1:
                    char = 'R'
                    fontResult = Font_R_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][31] == 1:
                    char = 'r'
                    fontResult = Font_r_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][32] == 1:
                    char = 'Ss'
                    fontResult = Font_Ss_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][33] == 1:
                    char = 'T'
                    fontResult = Font_T_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][34] == 1:
                    char = 't'
                    fontResult = Font_t_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][35] == 1:
                    char = 'U'
                    fontResult = Font_U_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][36] == 1:
                    char = 'u'
                    fontResult = Font_u_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][37] == 1:
                    char = 'Vv'
                    fontResult = Font_Vv_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][38] == 1:
                    char = 'Ww'
                    fontResult = Font_Ww_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][39] == 1:
                    char = 'Xx'
                    fontResult = Font_Xx_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][40] == 1:
                    char = 'Y'
                    fontResult = Font_Y_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][41] == 1:
                    char = 'y'
                    fontResult = Font_y_Model.predict(test_image)
                    Font_prediction(char, fontResult)
                elif result[0][42] == 1:
                    char = 'Zz'
                    fontResult = Font_Zz_Model.predict(test_image)
                    Font_prediction(char, fontResult)

            values = [Counter_Font_00,
                      Counter_Font_01,
                      Counter_Font_02,
                      Counter_Font_03,
                      Counter_Font_04,
                      Counter_Font_05,
                      Counter_Font_06,
                      Counter_Font_07,
                      Counter_Font_08,
                      Counter_Font_09]
            print("The Font is : " + str([i for i, x in enumerate(values) if x == max(values)]) + ",since " + str(
                max(values)) + " out of total " + str(sum(values)) + " characters are recognized to have this font!")
            print("--------------Font Map --------------\n"
                  "[0]: Helvetica\n"
                  "[1]: Baskerville\n"
                  "[2]: Times New Roman\n"
                  "[3]: Bodoni72\n"
                  "[4]: Didot\n"
                  "[5]: Futura\n"
                  "[6]: Gill Sans\n"
                  "[7]: Bembo\n"
                  "[8]: Rockwell\n"
                  "[9]: Franklin Gothic\n"
                  "----------------------------")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            file1.write(str([i for i, x in enumerate(values) if x == max(values)]) + '\t')
            file1.write(str(max(values)) + '\t')
            file1.write(str(sum(values)) + '\n')

    file1.close()


if __name__ == '__main__':
    main()
    exit()
