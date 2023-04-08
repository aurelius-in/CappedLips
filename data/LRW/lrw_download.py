import urllib.request
import os

# This code will download the LRW dataset and save it to the specified directory (./lrw_dataset/). 
# You can modify the save_dir variable to change where you want to save the dataset on your local machine.

# Set the URL of the LRW dataset
url = "http://www.robots.ox.ac.uk/~vgg/data/lip_reading_in_the_wild/lrw_dataset.zip"

# Set the directory where you want to save the dataset
save_dir = "./lrw_dataset/"

# Create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download the dataset and save it to the save directory
urllib.request.urlretrieve(url, os.path.join(save_dir, "lrw_dataset.zip"))
