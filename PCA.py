import os
import cv2
import numpy as np

# Train dir
def load_images_from_folder(folder):
    images = []
    labels = []
    for dir_name in os.listdir(folder):
        dir_path = os.path.join(folder, dir_name)
        if os.path.isdir(dir_path):
            for filename in os.listdir(dir_path):
                img_path = os.path.join(dir_path, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    img_flattened = img.flatten()
                    images.append(img_flattened)
                    labels.append(dir_name)
    return np.array(images), np.array(labels)

# Train dir
train_folder = '/path/to/train/dir'
train_images, train_labels = load_images_from_folder(train_folder)

# Test dir
test_folder = '/path/to/test/dir'
test_images, test_labels = load_images_from_folder(test_folder)

# For each dir in the train dir
# For each file in the dir
# Grayscale the image, flatten the image into a 1D array, and make the name of the dir the label

# Test dir
# do the same thing as above