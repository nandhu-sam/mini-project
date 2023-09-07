import shutil
import os

# Nandhu: Moves images from validation, test, and train folders to a temp folder

Alphabets1 = ['a-s', 'b-s', 'd-s' , 'e-s' , 'f-s', 'g-s' , 'h-s', 'i-s', 'j-s',  'l-s','m-s','n-s', 'q-s' , 'r-s' , 't-s', 'u-s', 'y-s']
Alphabets2 = ['A', 'B', 'D' , 'E' , 'F', 'G' , 'H', 'I', 'J', 'L','M','N', 'Q' , 'R' , 'T', 'U', 'Y']
Alphabets3 = ['Cc', 'Kk', 'Oo' , 'Pp' , 'Ss', 'Vv' , 'Ww', 'Xx', 'Zz']
Alphabets = Alphabets1 + Alphabets2 + Alphabets3;

fontnames = ['00','01','02','03','04', '05', '06','07','08','09']

for alphabet in Alphabets:
    for fontname in fontnames:
        Validation_folder = 'Fonts/'+ alphabet + '/Validation/' + fontname + '/'
        Test_folder = 'Fonts/'+ alphabet + '/Test/' + fontname + '/'
        Train_folder = 'Fonts/'+ alphabet + '/Train/' + fontname + '/'
        Temp_folder = 'Fonts/Temp/'
 
        for dirname, dirnames, filenames in os.walk(Validation_folder):
            for filename in filenames:
                if "_sg_" in filename:
                    if "Vir" in filename:
                        if ("20" in filename) :
                            shutil.move(Validation_folder+ filename, Temp_folder)
                            
        for dirname, dirnames, filenames in os.walk(Test_folder):
            for filename in filenames:
                if "_sg_" in filename:
                    if "Vir" in filename:
                        if ("20" in filename) :
                            shutil.move(Test_folder+ filename, Temp_folder)
                            
        for dirname, dirnames, filenames in os.walk(Train_folder):
            for filename in filenames:
                if "_sg_" in filename:
                    if "Vir" in filename:
                        if ("20" in filename):
                            shutil.move(Train_folder+ filename, Temp_folder)
