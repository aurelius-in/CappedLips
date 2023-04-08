import tensorflow as tf
import numpy as np
from data_loader import LipreadingDataLoader
from model import LipreadingCapsuleNetwork, LipreadingBaselineModel

# This Python file contains the implementation for comparing the effectiveness of the 
# capsule network model against a baseline model on a given test set.

# This implementation defines the comparison of the effectiveness of the capsule network 
# model against a baseline model on a given test set. The code loads the test set using 
# the LipreadingDataLoader class from data_loader.py and loads the trained capsule network 
# model and baseline model from their respective weight files. The code then evaluates both 
# models on the test set and prints the final test loss and accuracy for each model.

# Set random seed for reproducibility
tf.random.set_seed(1234)
np.random.seed(1234)

# Hyperparameters
batch_size = 32
num_classes = 10

# Load dataset
data_loader = LipreadingDataLoader(batch_size=batch_size)
_, _, test_dataset = data_loader.load_dataset()

# Load capsule network model
capsule_model = LipreadingCapsuleNetwork(num_classes=num_classes)
capsule_model.load_weights('capsule_model_weights.h5')

# Load baseline model
baseline_model = LipreadingBaselineModel(num_classes=num_classes)
baseline_model.load_weights('baseline_model_weights.h5')

# Define loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Define metrics for evaluation
capsule_test_loss = tf.keras.metrics.Mean(name='capsule_test_loss')
capsule_test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='capsule_test_accuracy')
baseline_test_loss = tf.keras.metrics.Mean(name='baseline_test_loss')
baseline_test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='baseline_test_accuracy')

# Evaluate capsule network model on test set
for inputs, labels in test_dataset:
    # Compute logits
    logits, _ = capsule_model(inputs, training=False)
    
    # Compute loss
    loss = loss_fn(labels, logits)
    
    # Update metrics
    capsule_test_loss(loss)
    capsule_test_accuracy(labels, logits)

# Evaluate baseline model on test set
for inputs, labels in test_dataset:
    # Compute logits
    logits = baseline_model(inputs)
    
    # Compute loss
    loss = loss_fn(labels, logits)
    
    # Update metrics
    baseline_test_loss(loss)
    baseline_test_accuracy(labels, logits)

# Print final metrics
print('Capsule Network Test Loss: {}, Test Accuracy: {}'.format(capsule_test_loss.result(), capsule_test_accuracy.result() * 100))
print('Baseline Model Test Loss: {}, Test Accuracy: {}'.format(baseline_test_loss.result(), baseline_test_accuracy.result() * 100))
