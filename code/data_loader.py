import numpy as np
import cv2
import tensorflow as tf

# This Python file contains the implementation of a data loader for lipreading.
# This implementation defines the LipreadingDataLoader class, which loads the 
# lipreading dataset and prepares it for training the capsule network model. 
# The class has a constructor that takes the path to the dataset, the shape of 
# the video frames, the number of frames per video, and the batch size. The 
# _load_video method loads a video from the dataset and returns an array of 
# frames. The load_data method loads all the videos from the dataset and creates 
# batches of videos and labels. The method returns a generator that yields batches 
# of videos and labels.

class LipreadingDataLoader:
    def __init__(self, dataset_path, frame_shape=(64, 64), num_frames=16, batch_size=32):
        self.dataset_path = dataset_path
        self.frame_shape = frame_shape
        self.num_frames = num_frames
        self.batch_size = batch_size
        self.num_classes = len(os.listdir(self.dataset_path))
        
    def _load_video(self, video_path):
        # Load video frames
        cap = cv2.VideoCapture(video_path)
        frames = []
        while len(frames) < self.num_frames:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, self.frame_shape)
            frames.append(frame)
        cap.release()
        
        # Pad frames if necessary
        while len(frames) < self.num_frames:
            frames.append(np.zeros(self.frame_shape, dtype=np.uint8))
            
        # Convert frames to array and normalize
        frames = np.array(frames, dtype=np.float32) / 255.0
        
        return frames
        
    def load_data(self):
        # Load video paths and labels
        video_paths, labels = [], []
        for class_idx, class_name in enumerate(os.listdir(self.dataset_path)):
            class_path = os.path.join(self.dataset_path, class_name)
            for video_name in os.listdir(class_path):
                video_path = os.path.join(class_path, video_name)
                video_paths.append(video_path)
                labels.append(class_idx)
        labels = tf.keras.utils.to_categorical(labels, num_classes=self.num_classes)
        
        # Load videos and create batches
        while True:
            batch_indices = np.random.choice(len(video_paths), size=self.batch_size, replace=False)
            batch_video_paths = np.array(video_paths)[batch_indices]
            batch_labels = np.array(labels)[batch_indices]
            batch_videos = np.array([self._load_video(video_path) for video_path in batch_video_paths])
            yield batch_videos, batch_labels
