# Importing the Keras libraries and packages
import numpy as np
import glob
import gc
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import History
import matplotlib.pyplot as plt

    
def ClassifyFont(neurons,letter,bz,e,spe,vs):

    
    # Initialising the CNN
    classifier = Sequential()
    
    # Step 1 - Convolution
    classifier.add(Conv2D(32, (3, 3), input_shape = (32,32,3), activation = 'relu'))
    
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    # Adding a second convolutional layer
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    # Step 3 - Flattening
    classifier.add(Flatten())
    
    # Step 4 - Full connection
    classifier.add(Dense(units = neurons, activation = 'relu'))
    #classifier.add(Dense(units = neurons, activation = 'relu'))
    #classifier.add(Dense(units = neurons, activation = 'relu'))
    classifier.add(Dense(units = 10, activation = 'softmax'))
    
    # Compiling the CNN
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    
    
    #Fitting the CNN to the images
    train_datagen = ImageDataGenerator(rescale = 1./255,
                                       shear_range = 0.2,
                                       zoom_range = 0.2,
                                       horizontal_flip = True)
    
    test_datagen = ImageDataGenerator(rescale = 1./255)
    
    
    
    history = History()
 #   training_set = train_datagen.flow_from_directory('D:\\classifierfiles\\Fonts\\'+letter+'\\Train\\' ,
    training_set = train_datagen.flow_from_directory('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Train/' ,
                                                     target_size = (32, 32),
                                                     batch_size = bz,
                                                     class_mode = 'categorical')
    
#   test_set = test_datagen.flow_from_directory('D:\\classifierfiles\\Fonts\\'+letter+'\\Validation\\',
    test_set = test_datagen.flow_from_directory('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Validation/',
                                                target_size = (32, 32),
                                                batch_size = bz,
                                                class_mode = 'categorical')
    
    classifier.fit_generator(training_set,
                             steps_per_epoch = spe,
                             epochs = e, 
                             validation_data = test_set,
                             validation_steps = vs,
                             shuffle         = True,
                             callbacks=[history])
    
    # saving the model 
    classifier.save('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Results/'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.h5')
 #   classifier.save('D:\\classifierfiles\\Fonts\\'+letter+'\\Results\\'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.h5')
    
    # Making predictions
    
    #input("Press Enter to continue...")
    
    file1 = open('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Results/'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.txt',"w") 
#    file1 = open('D:\\classifierfiles\\Fonts\\'+letter+'\\Results\\'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.txt',"w") 
    file1.write(str(history.history)+'\n') 
    
    #Accuracy & loss in different epochs
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, e), history.history["loss"], label="train_loss")
    plt.plot(np.arange(0, e), history.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, e), history.history["acc"], label="train_acc")
    plt.plot(np.arange(0, e), history.history["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy on Dataset")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Results/'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.png')
#    plt.savefig('D:\\classifierfiles\\Fonts\\'+letter+'\\Results\\'+letter+'_ne='+str(neurons)+'_bz='+ str(bz)+'_e='+str(e)+'_spe='+str(spe)+ '_vs='+str(vs)+'.png')
    
    
    #Making predictions 
    file_list = glob.glob('/Users/saeedeh/Desktop/Alphabet pics/Fonts/'+letter+'/Test/**/*.jpg', recursive=True)
 #   file_list = glob.glob('D:\\classifierfiles\\Fonts\\'+letter+'\\Test\\**\\*.jpg', recursive=True)
    for testFile in file_list:
        test_image = image.load_img(testFile, target_size = (32,32))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)
        print(testFile[50:62],end=" : ")
        file1.write(testFile[50:62]+' : ') 
        if result[0][0] == 1:
            print('00')
            file1.write('00\n')
        elif result[0][1] == 1:
            print('01')
            file1.write('01\n')
        elif result[0][2] == 1:
            print('02')
            file1.write('02\n')
        elif result[0][3] == 1:
            print('03')
            file1.write('03\n')
        elif result[0][4] == 1:
            print('04')
            file1.write('04\n')
        elif result[0][5] == 1:
            print('05')
            file1.write('05\n')
        elif result[0][6] == 1:
            print('06')
            file1.write('06\n')
        elif result[0][7] == 1:
            print('07')
            file1.write('07\n')
        elif result[0][8] == 1:
            print('08')
            file1.write('08\n')
        elif result[0][9] == 1:
            print('09')
            file1.write('09\n')
        else:
            print('Not Recognized')
            file1.write('Not Recognized\n')
    file1.close()
    del classifier

def main():
    #
    Alphabets1 = [ 'a-s', 'b-s', 'd-s' , 'e-s' , 'f-s', 'g-s' ,'h-s', 'i-s', 'j-s',  'l-s','m-s','n-s', 'q-s' , 'r-s' , 't-s', 'u-s', 'y-s']
    Alphabets2 = ['A', 'B', 'D' , 'E' , 'F', 'G' , 'H', 'I', 'J', 'L','M','N', 'Q' , 'R' , 'T', 'U', 'Y']
    Alphabets3 = ['Cc', 'Kk', 'Oo' , 'Pp' , 'Ss', 'Vv' , 'Ww', 'Xx', 'Zz']
    Alphabets = Alphabets1 + Alphabets2 + Alphabets3;
    DifferentNeurons = [128]
    DifferentEpochs = [500]
    
    for alphabet in Alphabets:
        for Neurons in DifferentNeurons:
            for epochs in DifferentEpochs:
                ClassifyFont(Neurons,alphabet,32,epochs,70,14)
                gc.collect()
            
if __name__ == '__main__':
    main()
    