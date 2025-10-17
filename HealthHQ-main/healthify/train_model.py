import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from .dataPreprocessing import preprocessData


def train():
    # Load and preprocess data
    data_dir = 'D:/DjangoProjects/HealthHQ/healthify/MLmodels/data/train' #change your training path accordingly
    X_train, X_test, y_train, y_test = preprocessData(data_dir)

    # Encode labels to categorical values
    label_encoder = LabelEncoder()
    y_train_encoded = tf.keras.utils.to_categorical(label_encoder.fit_transform(y_train))
    y_test_encoded = tf.keras.utils.to_categorical(label_encoder.transform(y_test))

    # Define the number of output classes
    num_classes = len(np.unique(y_train))  # Assuming y_train contains the labels

    # Define your neural network architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')  # Replace num_classes with the number of output classes
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train_encoded, epochs=10, validation_data=(X_test, y_test_encoded))

    # Save the trained model
    model.save('skin_disease_model.h5')
