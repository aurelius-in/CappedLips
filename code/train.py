import numpy as np
from data_loader import LipreadingDataLoader
from model import LipreadingCapsuleNetwork

# This Python file contains the implementation of the training loop for the capsule network model for lipreading.

# This implementation defines the training loop for the capsule network model for lipreading. The code loads the 
# dataset using the LipreadingDataLoader class from data_loader.py and creates

# Set random seed for reproducibility
tf.random.set_seed(1234)
np.random.seed(1234)

# Hyperparameters
batch_size = 32
num_epochs = 100
learning_rate = 0.001
num_classes = 10

# Load dataset
data_loader = LipreadingDataLoader(batch_size=batch_size)
train_dataset, val_dataset, test_dataset = data_loader.load_dataset()

# Create model
model = LipreadingCapsuleNetwork(num_classes=num_classes)

# Define loss function and optimizer
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

# Define metrics for evaluation
train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
val_loss = tf.keras.metrics.Mean(name='val_loss')
val_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='val_accuracy')

# Define training step
@tf.function
def train_step(inputs, labels):
    with tf.GradientTape() as tape:
        # Compute logits
        logits, _ = model(inputs, training=True)
        
        # Compute loss
        loss = loss_fn(labels, logits)
    
    # Compute gradients
    gradients = tape.gradient(loss, model.trainable_variables)
    
    # Update weights
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    # Update metrics
    train_loss(loss)
    train_accuracy(labels, logits)

# Define validation step
@tf.function
def val_step(inputs, labels):
    # Compute logits
    logits, _ = model(inputs, training=False)
    
    # Compute loss
    loss = loss_fn(labels, logits)
    
    # Update metrics
    val_loss(loss)
    val_accuracy(labels, logits)

# Training loop
for epoch in range(num_epochs):
    # Reset metrics
    train_loss.reset_states()
    train_accuracy.reset_states()
    val_loss.reset_states()
    val_accuracy.reset_states()
    
    # Train on batches
    for inputs, labels in train_dataset:
        train_step(inputs, labels)
        
    # Evaluate on validation set
    for inputs, labels in val_dataset:
        val_step(inputs, labels)
        
    # Print metrics
    template = 'Epoch {}, Loss: {}, Accuracy: {}, Val Loss: {}, Val Accuracy: {}'
    print(template.format(epoch+1,
                          train_loss.result(),
                          train_accuracy.result() * 100,
                          val_loss.result(),
                          val_accuracy.result() * 100))

# Evaluate on test set
test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')
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
