import urllib.request
import os

# This code will download the MIRACL-VC1 dataset and save it to the specified directory 
# (./miracl_vc1_dataset/). You can modify the save_dir variable to change where you want 
# to save the dataset on your local machine.

# Set the URL of the MIRACL-VC1 dataset
url = "https://www.dropbox.com/s/9cc4nbpik6fzi6x/MIRACL-VC1.zip?dl=1"

# Set the directory where you want to save the dataset
save_dir = "./miracl_vc1_dat/aset/"

# Create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download the dataset and save it to the save directory
urllib.request.urlretrieve(url, os.path.join(save_dir, "MIRACL-VC1.zip"))
