import os

import shutil
import random
import glob


def main():
    foldername = 'd-s'

    inputdirs = [os.path.join('Fonts', foldername, 'Train', str(n).zfill(2)) + os.sep for n in range(10)]
    outputdirsv = [os.path.join('Fonts', foldername, 'Validation', str(n).zfill(2)) + os.sep for n in range(10)]
    outputdirst = [os.path.join('Fonts', foldername, 'Test', str(n).zfill(2)) + os.sep for n in range(10)]

    N = 16
    N2 = 8

    for ix in range(10):
        file_list = glob.glob(inputdirs[ix] + '*.jpg')
        for counter in range(N):
            fe = random.choice(file_list)
            file_list.remove(fe)
            shutil.move(fe, outputdirsv[ix])
        for counter in range(N2):
            fe = random.choice(file_list)
            file_list.remove(fe)
            shutil.move(fe, outputdirst[ix])

    print("Done!")


if __name__ == '__main__':
    main()
