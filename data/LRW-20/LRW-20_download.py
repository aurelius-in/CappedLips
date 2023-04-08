import urllib.request
import os

# The above code downloads the LRW-20 dataset from the specified URL and saves it to the file path specified. 
# It then uses the zipfile library to extract the files from the downloaded archive.
# The code assumes that you are running it in a directory where you have write permissions and where you want 
# to download the dataset. You can modify the file_path variable to save the downloaded file to a different directory. 

# Also, note that the downloaded file is in .zip format, so we need to use the zipfile library to extract the files.


# set the URL and file path
url = "http://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrw1/lrw-20-words-list.zip"
file_path = os.path.join(".", "lrw-20-words-list.zip")

# download the file
urllib.request.urlretrieve(url, file_path)

# extract the files from the zip archive
import zipfile
with zipfile.ZipFile(file_path, "r") as zip_ref:
    zip_ref.extractall()
