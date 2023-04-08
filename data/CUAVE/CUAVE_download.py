import urllib.request
import os

# The code downloads the CUAVE dataset from the specified URL and saves 
# it to the file path specified. It then uses the tarfile library to extract 
# the files from the downloaded archive.

# The code assumes that you are running it in a directory where you have write 
# permissions and where you want to download the dataset. You can modify the file_path 
# variable to save the downloaded file to a different directory. Also, note that the downloaded 
# file is in .tar.gz format, so we need to specify the mode as "r:gz" when using the tarfile library to extract the files.

# set the URL and file path
url = "http://www.ee.columbia.edu/ln/dvmm/downloads/CUAVE_dataset.tar.gz"
file_path = os.path.join(".", "CUAVE_dataset.tar.gz")

# download the file
urllib.request.urlretrieve(url, file_path)

# extract the files from the tar archive
import tarfile
with tarfile.open(file_path, "r:gz") as tar:
    tar.extractall()
