import kagglehub
import shutil
import os

# Download dataset
cache_path = kagglehub.dataset_download(
    "abhishek14398/salary-dataset-simple-linear-regression" 
)

print("Downloaded to:", cache_path)

# Destination folder
destination = r"D:\Machine_Learning\Datasets"

os.makedirs(destination, exist_ok=True)

# Copy files
for file in os.listdir(cache_path):
    src = os.path.join(cache_path, file)
    dst = os.path.join(destination, file)

    if os.path.isfile(src):
        shutil.copy2(src, dst)

print("Copied to:", destination)