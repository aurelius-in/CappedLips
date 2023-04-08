import tensorflow as tf
import numpy as np
from data_loader import LipreadingDataLoader
from model import LipreadingCapsuleNetwork

# This Python file contains the implementation for evaluating the trained capsule network model on a given test set.

# This implementation defines the evaluation of the trained capsule network model on a given test set.  
# The code loads the test set using the LipreadingDataLoader class from data_loader.py and loads the trained 
# model from the model_weights.h5 file. The code then evaluates the model on the test set and prints the final 
# test loss and accuracy.

# Set random seed for reproducibility
tf.random.set_seed(1234)
np.random.seed(1234)

# Hyperparameters
batch_size = 32
num_classes = 10

# Load dataset
data_loader = LipreadingDataLoader(batch_size=batch_size)
_, _, test_dataset = data_loader.load_dataset()

# Load model
model = LipreadingCapsuleNetwork(num_classes=num_classes)
model.load_weights('model_weights.h5')

# Define loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Define metrics for evaluation
test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

# Evaluate on test set
for inputs, labels in test_dataset:
    # Compute logits
    logits, _ = model(inputs, training=False)
    
    # Compute loss
    loss = loss_fn(labels, logits)
    
    # Update metrics
    test_loss(loss)
    test_accuracy(labels, logits)

# Print final metrics
print('Test Loss: {}, Test Accuracy: {}'.format(test_loss.result(), test_accuracy.result() * 100))
