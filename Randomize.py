import shutil
import random
import glob

# Nandhu: Moves N items from train to validation and N2 items to test folders

def main():
    foldername = 'd-s'
    input_dir0='Fonts/' + foldername + '/Train/00/'
    input_dir1='Fonts/' + foldername + '/Train/01/'
    input_dir2='Fonts/' + foldername + '/Train/02/'
    input_dir3='Fonts/' + foldername + '/Train/03/'
    input_dir4='Fonts/' + foldername + '/Train/04/'
    input_dir5='Fonts/' + foldername + '/Train/05/'
    input_dir6='Fonts/' + foldername + '/Train/06/'
    input_dir7='Fonts/' + foldername + '/Train/07/'
    input_dir8='Fonts/' + foldername + '/Train/08/'
    input_dir9='Fonts/' + foldername + '/Train/09/'
    
    output_dirv0='Fonts/' + foldername + '/Validation/00/'
    output_dirv1='Fonts/' + foldername + '/Validation/01/'
    output_dirv2='Fonts/' + foldername + '/Validation/02/'
    output_dirv3='Fonts/' + foldername + '/Validation/03/'
    output_dirv4='Fonts/' + foldername + '/Validation/04/'
    output_dirv5='Fonts/' + foldername + '/Validation/05/'
    output_dirv6='Fonts/' + foldername + '/Validation/06/'
    output_dirv7='Fonts/' + foldername + '/Validation/07/'
    output_dirv8='Fonts/' + foldername + '/Validation/08/'
    output_dirv9='Fonts/' + foldername + '/Validation/09/'

    output_dirt0='Fonts/' + foldername + '/Test/00/'
    output_dirt1='Fonts/' + foldername + '/Test/01/'
    output_dirt2='Fonts/' + foldername + '/Test/02/'
    output_dirt3='Fonts/' + foldername + '/Test/03/'
    output_dirt4='Fonts/' + foldername + '/Test/04/'
    output_dirt5='Fonts/' + foldername + '/Test/05/'
    output_dirt6='Fonts/' + foldername + '/Test/06/'
    output_dirt7='Fonts/' + foldername + '/Test/07/'
    output_dirt8='Fonts/' + foldername + '/Test/08/'
    output_dirt9='Fonts/' + foldername + '/Test/09/'
     

    N=16
    N2=8
    
    file_list = glob.glob(input_dir0+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv0)
    file_list = glob.glob(input_dir0+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt0)
    
    
    file_list = glob.glob(input_dir1+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv1)
    file_list = glob.glob(input_dir1+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt1)
    
    
    file_list = glob.glob(input_dir2+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv2)
    file_list = glob.glob(input_dir2+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt2)
   
    
    file_list = glob.glob(input_dir3+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv3)
    file_list = glob.glob(input_dir3+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt3)
    
    
    file_list = glob.glob(input_dir4+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv4)
    file_list = glob.glob(input_dir4+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt4)
    
    
    file_list = glob.glob(input_dir5+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv5)
    file_list = glob.glob(input_dir5+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt5)
    
    
    file_list = glob.glob(input_dir6+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv6)
    file_list = glob.glob(input_dir6+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt6)
    
    
    file_list = glob.glob(input_dir7+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv7)
    file_list = glob.glob(input_dir7+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt7)
    
    
    file_list = glob.glob(input_dir8+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv8)
    file_list = glob.glob(input_dir8+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt8)
    
    
    file_list = glob.glob(input_dir9+"*.jpg")
    for counter in range(N):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirv9)
    file_list = glob.glob(input_dir9+"*.jpg")
    for counter2 in range(N2):
        fe = random.choice(file_list)
        file_list.remove(fe)
        shutil.move(fe,output_dirt9)
        
    print ("Done!")
if __name__ == '__main__':
    main()
