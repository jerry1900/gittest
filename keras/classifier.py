#-*-coding:utf8-*-
__author__ = '万壑'

import numpy as np

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import RMSprop

# X_train (60000, 28*28), y_train (60000,), x_test (10000,28*28), y_test (10000,)
(X_train,y_train),(X_test,y_test) = mnist.load_data()
# print(type(X_train))
# print(X_train.shape)

# data pre-processing
X_train = X_train.reshape(X_train.shape[0],-1)/255.0
X_test = X_test.reshape(X_test.shape[0],-1)/255.0

y_train = np_utils.to_categorical(y_train,num_classes = 10)
y_test = np_utils.to_categorical(y_test,num_classes = 10)


# build neural network
model = Sequential([
    Dense(48,input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

# build the optimizer
# rmsprop = RMSprop(lr=0.001,rho=0.9,epsilon=1e-08,decay=0.0)

# we add metrics to get more results
model.compile(
    optimizer='adagrad',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

print('Training-----------------')
model.fit(X_train,y_train,batch_size=32,epochs=2)

print('\nTesting---------------')
loss,accuracy = model.evaluate(X_test,y_test)

print('test loss;',loss)
print('test accuracy:',accuracy)
