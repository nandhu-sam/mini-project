# Importing the Keras libraries and packages

import os
import glob

import numpy as np

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
train_datagen = ImageDataGenerator(rescale=1.0/255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1.0/255)

bz = 32
e = 500
spe = 700
vs = 140

history = History()

training_set = train_datagen.flow_from_directory(os.path.join('Alphabet pics', 'Alphabets', 'Train') + os.sep,
                                                 target_size=(32, 32),
                                                 batch_size=32,
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory(os.path.join('Alphabet pics', 'Alphabets', 'Validation') + os.sep,
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
classifier.save(os.path.join('Alphabet pics', 'Alphabets', 'AlphabetResults',
                             'Alphabet_bz=' + str(bz) +
                             '_e=' + str(e) +
                             '_spe=' + str(spe) +
                             '_vs=' + str(vs) + '.h5'))

input("Press Enter to continue...")

file1 = open(os.path.join('Alphabet pics', 'Alphabets', 'AlphabetResults',
                          'Alphabet_bz=' + str(bz) +
                          '_e=' + str(e) +
                          '_spe=' + str(spe) +
                          '_vs=' + str(vs) + '.txt'), "w")

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
plt.savefig(os.path.join('Alphabet pics', 'Alphabets', 'AlphabetResults',
                         'Alphabet_bz=' + str(bz) +
                         '_e=' + str(e) +
                         '_spe=' + str(spe) +
                         '_vs=' + str(vs) + '.png'))

letters = ['A', 'a', 'B', 'b', 'Cc', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'Kk', 'L',
           'l', 'M', 'm', 'N', 'n', 'Oo', 'Pp', 'Q', 'q', 'R', 'r', 'Ss', 'T', 't', 'U', 'u', 'Vv', 'Ww', 'Xx', 'Y',
           'y', 'Zz']
# Making predictions
file_list = glob.glob(os.path.join('Alphabet pics', 'Alphabets', 'Test', '**', '*.jpg'), recursive=True)

for testFile in file_list:
    test_image = image.load_img(testFile, target_size=(32, 32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    print(testFile[42:62], end=" : ")
    file1.write(testFile[42:62] + ' : ')

    rec = False
    for c in range(len(letters)):
        if result[0][c] == 1:
            print(letters[c])
            file1.write(letters[c]+'\n')
            rec = True
            break

    if not rec:
        print('Not Recognized')
        file1.write('Not Recognized\n')

file1.close()
