
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
# Load the Iris dataset
iris = load_iris()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

from keras.utils import to_categorical

# One-hot encode the target labels
y_train_onehot = to_categorical(y_train)
y_test_onehot = to_categorical(y_test)

# Define the ANN model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(iris.data.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))  # Change the output layer to have 3 units

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_onehot, epochs=5, batch_size=32)

# Evaluate the model
model_loss, model_accuracy = model.evaluate(X_test, y_test_onehot)
print('Model loss:', model_loss)
print('Model accuracy:', model_accuracy)