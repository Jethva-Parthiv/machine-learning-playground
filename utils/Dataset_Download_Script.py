import kagglehub
import shutil
import os

# Download dataset
try:
    # Note: Removed "datasets/" from the path as kagglehub just needs "username/dataset"
    ds_handle = input("Enter Dataset Handel URL : ") 
    cache_path = kagglehub.dataset_download(ds_handle)
    print(f"Success! Dataset downloaded to: {cache_path}")

except Exception as error:
    print("Error While Downloading Dataset !!")
    print(f"Reason: {error}")
    exit

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