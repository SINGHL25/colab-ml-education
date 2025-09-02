import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

def build_model(input_dim, num_classes):
    m = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    m.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return m

def train_iris(epochs=5, verbose=0):
    X, y = load_iris(return_X_y=True)
    X = (X - X.mean(0)) / X.std(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_model(X.shape[1], len(np.unique(y)))
    hist = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, verbose=verbose)
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    return model, acc, hist.history
