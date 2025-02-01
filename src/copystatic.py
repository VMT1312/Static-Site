import os
import shutil

def file_transfer(source_path, destination_path):
    # Remove destination directory if it already exists
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)

    # Ensure the root destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    for file in os.listdir(source_path):
        cur_source_path = os.path.join(source_path, file)
        cur_destination_path = os.path.join(destination_path, file)

        # If it's a file, copy it
        if os.path.isfile(cur_source_path):
            shutil.copy(cur_source_path, cur_destination_path)
        # If it's a directory, recurse
        else:
            file_transfer(cur_source_path, cur_destination_path)