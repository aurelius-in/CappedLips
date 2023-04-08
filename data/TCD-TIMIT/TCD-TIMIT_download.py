import urllib.request
import os

# This code will download the TCD-TIMIT dataset and save it to the specified 
# directory (./tcd_timit_dataset/). You can modify the save_dir variable to 
# change where you want to save the dataset on your local machine.

# Set the URL of the TCD-TIMIT dataset
url = "http://homepages.dcu.ie/~tcdtimit/TCDTIMIT.tar.gz"

# Set the directory where you want to save the dataset
save_dir = "./tcd_timit_dataset/"

# Create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download the dataset and save it to the save directory
urllib.request.urlretrieve(url, os.path.join(save_dir, "TCDTIMIT.tar.gz"))
