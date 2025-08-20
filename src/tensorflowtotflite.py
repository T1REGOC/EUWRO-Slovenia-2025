## EXPANSION KIT ##
## TEAM REGOC ##
import tensorflow as tf  # Import TensorFlow library

# Load the trained Keras model from file
model = tf.keras.models.load_model('WRO2025new.keras') 

# Create a TFLiteConverter object from the Keras model
converter = tf.lite.TFLiteConverter.from_keras_model(model) 

# Convert the Keras model to TensorFlow Lite format
tflite_model = converter.convert() 

# Save the converted TensorFlow Lite model to a file
with open('WRO2025new.tflite', 'wb') as f: 
    f.write(tflite_model)