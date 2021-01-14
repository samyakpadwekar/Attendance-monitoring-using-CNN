import split_folders

#Split with a ratio.
#To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.

split_folders.ratio(r'D:\College\sem7\attendance\cropped_dataset', output="divided", seed=1337, ratio=(.8, .2)) # default values

#Part 1 - Building the CNN



# Importing the Keras libraries and packages



from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense



from keras.applications.vgg16 import VGG16
classifier = VGG16()

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (256, 256, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
#classifier.add(Dense(units = 128, activation = "relu"))
#classifier.add(Dense(units = 5, activation = "sigmoid"))
classifier.add(Dense(24, activation='softmax'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

classifier.summary()

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(r'C:\Users\lenovo\divided\train',
                                                 target_size = (256, 256),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')
#
test_set = test_datagen.flow_from_directory(r'C:\Users\lenovo\divided\val',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 600,
                         nb_epoch = 3,
                         validation_data = None,
                         nb_val_samples = 21032)

classifier.summary()