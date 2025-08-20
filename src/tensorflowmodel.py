## EXPANSION KIT ##
## TEAM REGOC ##
import os  # For file and directory operations
import numpy as np  # For numerical operations and arrays
import tensorflow as tf  # For building and training neural networks
from tensorflow.keras.models import Sequential  # Sequential model for stacking layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # Common layers for CNN
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # For image augmentation and preprocessing
from sklearn.model_selection import train_test_split  # For splitting dataset into train and test sets
from sklearn.utils import shuffle  # For shuffling the dataset

tf.random.set_seed(42)  # Set random seed for reproducibility

dataset_dir = r'C:\Users\Vedran\Desktop\datasetnew\dataset'  # Path to the dataset directory
red_dir = os.path.join(dataset_dir, 'red')  # Path to red images
green_dir = os.path.join(dataset_dir, 'green')  # Path to green images

IMG_SIZE = (128, 96)  # Image size for resizing (width, height)
BATCH_SIZE = 32  # Number of samples per batch
EPOCHS = 30  # Number of training epochs

def load_dataset():
    images = []  # List to store image data
    labels = []  # List to store labels (0 for red, 1 for green)
    for img_file in os.listdir(red_dir):  # Loop through red images
        img_path = os.path.join(red_dir, img_file)  # Get full path to image
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=IMG_SIZE)  # Load and resize image
        img_array = tf.keras.preprocessing.image.img_to_array(img)  # Convert image to numpy array
        images.append(img_array)  # Add image array to list
        labels.append(0)  # Label 0 for red
    for img_file in os.listdir(green_dir):  # Loop through green images
        img_path = os.path.join(green_dir, img_file)  # Get full path to image
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=IMG_SIZE)  # Load and resize image
        img_array = tf.keras.preprocessing.image.img_to_array(img)  # Convert image to numpy array
        images.append(img_array)  # Add image array to list
        labels.append(1)  # Label 1 for green
    return np.array(images), np.array(labels)  # Return images and labels as numpy arrays

X, y = load_dataset()  # Load images and labels
X, y = shuffle(X, y, random_state=42)  # Shuffle the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split into train and test sets

# Data augmentation for training images
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values to [0, 1]
    rotation_range=20,  # Random rotation
    width_shift_range=0.2,  # Random horizontal shift
    height_shift_range=0.2,  # Random vertical shift
    shear_range=0.2,  # Shear transformation
    zoom_range=0.2,  # Random zoom
    horizontal_flip=True,  # Random horizontal flip
    fill_mode='nearest'  # Fill mode for new pixels
)

# Only rescale for test images
test_datagen = ImageDataGenerator(rescale=1./255)

# Create generators for training and testing data
train_generator = train_datagen.flow(X_train, y_train, batch_size=BATCH_SIZE)
test_generator = test_datagen.flow(X_test, y_test, batch_size=BATCH_SIZE)

# Define the CNN model architecture
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),  # First convolutional layer
    MaxPooling2D((2, 2)),  # First max pooling layer
    Conv2D(64, (3, 3), activation='relu'),  # Second convolutional layer
    MaxPooling2D((2, 2)),  # Second max pooling layer
    Conv2D(128, (3, 3), activation='relu'),  # Third convolutional layer
    MaxPooling2D((2, 2)),  # Third max pooling layer
    Flatten(),  # Flatten the output for dense layers
    Dense(128, activation='relu'),  # Dense layer with 128 units
    Dropout(0.5),  # Dropout for regularization
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model with optimizer, loss function, and metric
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(
    train_generator,  # Training data
    steps_per_epoch=len(X_train) // BATCH_SIZE,  # Steps per epoch
    epochs=EPOCHS,  # Number of epochs
    validation_data=test_generator,  # Validation data
    validation_steps=len(X_test) // BATCH_SIZE  # Validation steps
)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_generator)
print(f'\nTest accuracy: {test_acc:.4f}')  # Print test accuracy

# Save the trained model
model.save('WRO2025new.keras')
print("Model saved")