import tensorflow as tf

# This Python file contains the implementation of a capsule network model for lipreading.

# This implementation defines the LipreadingCapsuleNetwork class, which is a TensorFlow 
# Keras model that implements the capsule network architecture for lipreading. The class 
# has a constructor that takes the number of classes in the dataset. The call method applies 
# convolutional layers, primary capsule layer, digit capsule layers, and reshapes the output 
# to compute the predicted probabilities and activations of digit capsules. The _squash method 
# applies the squashing activation function.

class LipreadingCapsuleNetwork(tf.keras.Model):
    def __init__(self, num_classes):
        super(LipreadingCapsuleNetwork, self).__init__()
        
        # Convolutional layers
        self.conv1 = tf.keras.layers.Conv3D(filters=64, kernel_size=(3, 3, 3), activation='relu')
        self.conv2 = tf.keras.layers.Conv3D(filters=128, kernel_size=(3, 3, 3), activation='relu')
        self.conv3 = tf.keras.layers.Conv3D(filters=256, kernel_size=(3, 3, 3), activation='relu')
        
        # Primary capsule layer
        self.primary_caps = tf.keras.layers.Conv3D(filters=32, kernel_size=(3, 3, 3), strides=(2, 2, 2), padding='valid', activation='relu')
        
        # Digit capsule layers
        self.digit_caps1 = tf.keras.layers.Dense(units=512, activation='relu')
        self.digit_caps2 = tf.keras.layers.Dense(units=num_classes * 16, activation=None)
        
        # Reshape layer
        self.reshape = tf.keras.layers.Reshape(target_shape=(num_classes, 16))
        
    def call(self, inputs):
        # Apply convolutional layers
        x = self.conv1(inputs)
        x = self.conv2(x)
        x = self.conv3(x)
        
        # Reshape to primary capsules
        x = self.primary_caps(x)
        batch_size = tf.shape(x)[0]
        num_primary_caps = tf.reduce_prod(tf.shape(x)[1:-1])
        primary_caps_dim = x.shape[-1]
        x = tf.reshape(x, [batch_size, num_primary_caps, primary_caps_dim])
        
        # Apply squashing activation
        x = self._squash(x)
        
        # Compute predicted probabilities and activations of digit capsules
        x = self.digit_caps1(x)
        x = self.digit_caps2(x)
        
        # Reshape to final output
        x = self.reshape(x)
        probs = tf.norm(x, axis=-1)
        activations = x / (1 + probs[..., tf.newaxis])
        
        return probs, activations
    
    def _squash(self, x):
        # Compute squared norm of x
        squared_norm = tf.reduce_sum(tf.square(x), axis=-1, keepdims=True)
        
        # Compute scaling factor
        scaling_factor = squared_norm / (1 + squared_norm) / tf.sqrt(squared_norm + tf.keras.backend.epsilon())
        
        # Scale x
        x_scaled = scaling_factor * x
        
        return x_scaled
