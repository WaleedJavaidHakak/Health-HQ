import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split


def load_data(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        print(f"Checking directory: {label_dir}")  # Debugging line
        if os.path.isdir(label_dir):
            for img_file in os.listdir(label_dir):
                img_path = os.path.join(label_dir, img_file)
                print(f"Reading image: {img_path}")  # Debugging line
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, (128, 128))  # Resize images to 128x128
                    images.append(img)
                    labels.append(label)
                else:
                    print(f"Failed to read image: {img_path}")  # Debugging line
    images = np.array(images)
    labels = np.array(labels)
    return images, labels

def preprocessData(data_dir):
    images, labels = load_data(data_dir)
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
    X_train = X_train / 255.0  # Normalize pixel values
    X_test = X_test / 255.0
    return X_train, X_test, y_train, y_test
