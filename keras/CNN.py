#-*-coding:utf8-*-
__author__ = '万壑'

import numpy as np

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,Conv2D,MaxPooling2D,Flatten
from keras.optimizers import RMSprop

#  load mnist dataset
(X_train,y_train),(X_test,y_test) = mnist.load_data()

#pre-processing
X_train = X_train.reshape(-1,1,28,28)
X_test  = X_test.reshape(-1,1,28,28)
y_train = np_utils.to_categorical(y_train,num_classes = 10)
y_test = np_utils.to_categorical(y_test,num_classes = 10)

# Build CNN, first layer(conv+activation+maxpooling)
model = Sequential()
model.add(
    Conv2D(
     padding = 'same',
     kernel_size = (5, 5),
     input_shape = (1, 28, 28)
    )
)

filters = 32,


dim_ordering = 'th',


model.add(Activation('relu'))
model.add(
    MaxPooling2D(
        pool_size=(2,2),
        strides=(2,2),
        border_mode='same'
    )
)

#second layer
model.add(Convolution2D(64,5,5,border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2),border_mode='same'))

#third layer,flattern && dense && activation
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

#fourth layer
model.add(Dense(10))
model.add(Activation('softmax'))

# compile,optimize
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])


#train
model.fit(X_train,y_train,nb_epoch=1,batch_size=64)

#test






