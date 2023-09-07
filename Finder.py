import glob
import shutil

import os


def main():
    folder_name = "D"
    # input_dir = 'Train-Back up/' + folder_name + '/'
    input_dir = os.path.join('Train-Back up', folder_name) + os.sep

    # output_dir0 = 'Fonts/' + folder_name + '/' + 'Train/00/'
    # output_dir1 = 'Fonts/' + folder_name + '/' + 'Train/01/'
    # output_dir2 = 'Fonts/' + folder_name + '/' + 'Train/02/'
    # output_dir3 = 'Fonts/' + folder_name + '/' + 'Train/03/'
    # output_dir4 = 'Fonts/' + folder_name + '/' + 'Train/04/'
    # output_dir5 = 'Fonts/' + folder_name + '/' + 'Train/05/'
    # output_dir6 = 'Fonts/' + folder_name + '/' + 'Train/06/'
    # output_dir7 = 'Fonts/' + folder_name + '/' + 'Train/07/'
    # output_dir8 = 'Fonts/' + folder_name + '/' + 'Train/08/'
    # output_dir9 = 'Fonts/' + folder_name + '/' + 'Train/09/'

    output_dir0 = os.path.join('Fonts', folder_name, 'Train', '00') + os.sep
    output_dir1 = os.path.join('Fonts', folder_name, 'Train', '01') + os.sep
    output_dir2 = os.path.join('Fonts', folder_name, 'Train', '02') + os.sep
    output_dir3 = os.path.join('Fonts', folder_name, 'Train', '03') + os.sep
    output_dir4 = os.path.join('Fonts', folder_name, 'Train', '04') + os.sep
    output_dir5 = os.path.join('Fonts', folder_name, 'Train', '05') + os.sep
    output_dir6 = os.path.join('Fonts', folder_name, 'Train', '06') + os.sep
    output_dir7 = os.path.join('Fonts', folder_name, 'Train', '07') + os.sep
    output_dir8 = os.path.join('Fonts', folder_name, 'Train', '08') + os.sep
    output_dir9 = os.path.join('Fonts', folder_name, 'Train', '09') + os.sep

    file_list = glob.glob(input_dir + "*.jpg")
    for Image in file_list:
        text = (str(Image))

        if '00' in text:
            shutil.copy(Image, output_dir0)
        elif '01' in text:
            shutil.copy(Image, output_dir1)
        elif '02' in text:
            shutil.copy(Image, output_dir2)
        elif '03' in text:
            shutil.copy(Image, output_dir3)
        elif '04' in text:
            shutil.copy(Image, output_dir4)
        elif '05' in text:
            shutil.copy(Image, output_dir5)
        elif '06' in text:
            shutil.copy(Image, output_dir6)
        elif '07' in text:
            shutil.copy(Image, output_dir7)
        elif '08' in text:
            shutil.copy(Image, output_dir8)
        elif '09' in text:
            shutil.copy(Image, output_dir9)


if __name__ == '__main__':
    main()
