# Importing the Keras libraries and packages
import numpy as np
import glob
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import History
import matplotlib.pyplot as plt

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=43, activation='softmax'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fitting the CNN to the images
train_datagen = ImageDataGenerator(rescale=1.0/ 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

bz = 32
e = 500
spe = 700
vs = 140

history = History()

training_set = train_datagen.flow_from_directory(os.path.join('Alphabet pics', 'Alphabets', 'Train'),
                                                 target_size=(32, 32),
                                                 batch_size=32,
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory(os.path.join('Alphabet pics', 'Alphabets', 'Train'),
                                            target_size=(32, 32),
                                            batch_size=bz,
                                            class_mode='categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch=spe,
                         epochs=e,
                         validation_data=test_set,
                         validation_steps=vs,
                         callbacks=[history])

# saving the model 
classifier.save(os.path.join('Alphabet pics', 'Alphabets', 'AlphabetResults', 'Alphabet_bz=' + str(bz) + '_e=' + str(
    e) + '_spe=' + str(spe) + '_vs=' + str(vs) + '.h5'))
input("Press Enter to continue...")

file1 = open(os.path.join('Alphabet pics', 'Alphabets', 'AlphabetResults', 'Alphabet_bz=' + str(bz) + '_e=' + str(
    e) + '_spe=' + str(spe) + '_vs=' + str(vs) + '.txt'), "w")

file1.write(str(history.history) + '\n')

# plotting accuracy & loss in different epochs
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
plt.savefig('/Users/saeedeh/Desktop/Alphabet pics/Alphabets/AlphabetResults/Alphabet_bz=' + str(bz) + '_e=' + str(
    e) + '_spe=' + str(spe) + '_vs=' + str(vs) + '.png')

# Making predictions
file_list = glob.glob('/Users/saeedeh/Desktop/Alphabet pics/Alphabets/Test/**/*.jpg', recursive=True)
for testFile in file_list:
    test_image = image.load_img(testFile, target_size=(32, 32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    print(testFile[42:62], end=" : ")
    file1.write(testFile[42:62] + ' : ')
    if result[0][0] == 1:
        print('A')
        file1.write('A\n')
    elif result[0][1] == 1:
        print('a')
        file1.write('a\n')
    elif result[0][2] == 1:
        print('B')
        file1.write('B\n')
    elif result[0][3] == 1:
        print('b')
        file1.write('b\n')
    elif result[0][4] == 1:
        print('Cc')
        file1.write('Cc\n')
    elif result[0][5] == 1:
        print('D')
        file1.write('D\n')
    elif result[0][6] == 1:
        print('d')
        file1.write('d\n')
    elif result[0][7] == 1:
        print('E')
        file1.write('E\n')
    elif result[0][8] == 1:
        print('e')
        file1.write('e\n')
    elif result[0][9] == 1:
        print('F')
        file1.write('F\n')
    elif result[0][10] == 1:
        print('f')
        file1.write('f\n')
    elif result[0][11] == 1:
        print('G')
        file1.write('G\n')
    elif result[0][12] == 1:
        print('g')
        file1.write('g\n')
    elif result[0][13] == 1:
        print('H')
        file1.write('H\n')
    elif result[0][14] == 1:
        print('h')
        file1.write('h\n')
    elif result[0][15] == 1:
        print('I')
        file1.write('I\n')
    elif result[0][16] == 1:
        print('i')
        file1.write('i\n')
    elif result[0][17] == 1:
        print('J')
        file1.write('J\n')
    elif result[0][18] == 1:
        print('j')
        file1.write('j\n')
    elif result[0][19] == 1:
        print('Kk')
        file1.write('Kk\n')
    elif result[0][20] == 1:
        print('L')
        file1.write('L\n')
    elif result[0][21] == 1:
        print('l')
        file1.write('l\n')
    elif result[0][22] == 1:
        print('M')
        file1.write('M\n')
    elif result[0][23] == 1:
        print('m')
        file1.write('m\n')
    elif result[0][24] == 1:
        print('N')
        file1.write('N\n')
    elif result[0][25] == 1:
        print('n')
        file1.write('n\n')
    elif result[0][26] == 1:
        print('Oo')
        file1.write('Oo\n')
    elif result[0][27] == 1:
        print('Pp')
        file1.write('Pp\n')
    elif result[0][28] == 1:
        print('Q')
        file1.write('Q\n')
    elif result[0][29] == 1:
        print('q')
        file1.write('q\n')
    elif result[0][30] == 1:
        print('R')
        file1.write('R\n')
    elif result[0][31] == 1:
        print('r')
        file1.write('r\n')
    elif result[0][32] == 1:
        print('Ss')
        file1.write('Ss\n')
    elif result[0][33] == 1:
        print('T')
        file1.write('T\n')
    elif result[0][34] == 1:
        print('t')
        file1.write('t\n')
    elif result[0][35] == 1:
        print('U')
        file1.write('U\n')
    elif result[0][36] == 1:
        print('u')
        file1.write('u\n')
    elif result[0][37] == 1:
        print('Vv')
        file1.write('Vv\n')
    elif result[0][38] == 1:
        print('Ww')
        file1.write('Ww\n')
    elif result[0][39] == 1:
        print('Xx')
        file1.write('Xx\n')
    elif result[0][40] == 1:
        print('Y')
        file1.write('Y\n')
    elif result[0][41] == 1:
        print('y')
        file1.write('y\n')
    elif result[0][42] == 1:
        print('Zz')
        file1.write('Zz\n')
    else:
        print('Not Recognized')
        file1.write('Not Recognized\n')
file1.close()
