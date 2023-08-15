import os
from pathlib import Path


def find_largeFile(source_path, file_size):
    for folders, sub_folders, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(folders, file)
            file_size_get = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_get > file_size:
                print(f"Large Files Detected on {file_path}: ({file_size_get:.2f}MB)")


source = r"D:\Z Laptop"
large_size = 50

find_largeFile(source, large_size)
