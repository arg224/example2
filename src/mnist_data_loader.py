# src/mnist_data_loader.py
import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np

def load_mnist_data():
    # Load MNIST dataset
    (x_train, y_train), _ = mnist.load_data()

    # Normalize pixel values to between 0 and 1
    x_train = x_train / 255.0

    # Flatten the images and convert labels to int64
    x_train = x_train.reshape((-1, 28 * 28)).astype(np.float32)
    y_train = y_train.astype(np.int64)

    # Combine image and label into tuples
    mnist_data = list(zip(x_train, y_train))

    return mnist_data
