import glob
import shutil

import os


def main():
    folder_name = "D"

    input_dir = os.path.join('Train-Back up', folder_name) + os.sep

    outputdirs = [os.path.join('Fonts', folder_name, 'Train', str(n).zfill(2)) + os.sep for n in range(10)]

    file_list = glob.glob(input_dir + "*.jpg")
    for Image in file_list:
        text = (str(Image))
        for i, num in enumerate([str(n).zfill(2) for n in range(10)]):
            if num in text:
                shutil.copy(Image, outputdirs[i])


if __name__ == '__main__':
    main()
