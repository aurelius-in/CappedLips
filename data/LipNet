import urllib.request
import os

# This code downloads the LipNet dataset zip file from the given URL and saves it to the specified directory (./lrw1/). 
# It then extracts the zip file to the same directory. You can modify the save_dir variable to specify a different 
# directory to save the dataset.

# Note that this dataset is quite large (around 150 GB), so downloading and extracting it may take some time depending 
# on your internet speed and computer hardware.

# URL of the dataset zip file
url = "http://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrw1.zip"

# Directory to save the dataset
save_dir = "./lrw1/"

# Create the save directory if it does not exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download the dataset zip file
filename, headers = urllib.request.urlretrieve(url, save_dir + "lrw1.zip")

# Extract the zip file to the save directory
import zipfile
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(save_dir)
