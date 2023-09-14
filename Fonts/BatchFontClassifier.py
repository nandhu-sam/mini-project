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


def ClassifyFont(neurons, letter, bz, e, spe, vs):
    # Initialising the CNN
    classifier = Sequential()

    # Step 1 - Convolution and pooling
    classifier.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # Adding a second convolutional layer
    classifier.add(Conv2D(32, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # Step 2 - Flattening
    classifier.add(Flatten())

    # Step 3 - Full connection
    classifier.add(Dense(units=neurons, activation='relu'))
    # classifier.add(Dense(units = neurons, activation = 'relu'))
    # classifier.add(Dense(units = neurons, activation = 'relu'))
    classifier.add(Dense(units=10, activation='softmax'))

    # Compiling the CNN
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Fitting the CNN to the images
    train_datagen = ImageDataGenerator(rescale=1.0/255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1.0/255)

    history = History()
    training_set = train_datagen.flow_from_directory(os.path.join('Fonts', letter, 'Train') + os.sep,
                                                     target_size=(32, 32),
                                                     batch_size=bz,
                                                     class_mode='categorical')

    test_set = test_datagen.flow_from_directory(os.path.join('Fonts', letter, 'Validation') + os.sep,
                                                target_size=(32, 32),
                                                batch_size=bz,
                                                class_mode='categorical')

    classifier.fit_generator(training_set,
                             steps_per_epoch=spe,
                             epochs=e,
                             validation_data=test_set,
                             validation_steps=vs,
                             shuffle=True,
                             callbacks=[history])

    # saving the model

    clf_params_str = ('_ne=' + str(neurons) +
                      '_bz=' + str(bz) +
                      '_e=' + str(e) +
                      '_spe=' + str(spe) +
                      '_vs=' + str(vs))

    classifier.save(os.path.join('Fonts', letter, 'Results', letter + clf_params_str + '.h5'))
    file1 = open(os.path.join('Fonts', letter, 'Results', letter + clf_params_str + '.h5'), "w")
    file1.write(str(history.history) + '\n')

    # Accuracy & loss in different epochs
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, e), history.history["loss"], label="train_loss")
    plt.plot(np.arange(0, e), history.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, e), history.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, e), history.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy on Dataset")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig(os.path.join('Fonts', letter, 'Results', letter + clf_params_str + '.png'))

    # Making predictions

    file_list = glob.glob(os.path.join('Fonts', letter, 'Test', '**', '*.jpg'), recursive=True)

    for testFile in file_list:
        test_image = image.load_img(testFile, target_size=(32, 32))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)
        print(testFile[50:62], end=" : ")
        file1.write(testFile[50:62] + ' : ')

        rec = False
        for n in range(10):
            if result[0][n] == 1:
                rec = True
                sn = str(n).zfill(2)
                print(sn)
                file1.write(sn + '\n')
                break
        if not rec:
            print('Not Recognized')
            file1.write('Not Recognized\n')

    file1.close()
    del classifier


def main():
    Alphabets1 = ['a-s', 'b-s', 'd-s', 'e-s', 'f-s', 'g-s', 'h-s', 'i-s', 'j-s', 'l-s', 'm-s', 'n-s', 'q-s', 'r-s',
                  't-s', 'u-s', 'y-s']
    Alphabets2 = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'Q', 'R', 'T', 'U', 'Y']
    Alphabets3 = ['Cc', 'Kk', 'Oo', 'Pp', 'Ss', 'Vv', 'Ww', 'Xx', 'Zz']
    Alphabets = Alphabets1 + Alphabets2 + Alphabets3
    DifferentNeurons = [128]
    DifferentEpochs = [500]

    for alphabet in Alphabets:
        for Neurons in DifferentNeurons:
            for epochs in DifferentEpochs:
                ClassifyFont(Neurons, alphabet, 32, epochs, 70, 14)
                gc.collect()


if __name__ == '__main__':
    main()
