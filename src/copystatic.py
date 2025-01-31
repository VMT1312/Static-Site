import os, shutil

def file_transfer(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    destination = destination_path
    source = source_path
    os.mkdir(destination)
    for file in os.listdir(source):
        cur_path = os.path.join(source, file)
        if os.path.isfile(cur_path):
            shutil.copy(
                cur_path,
                destination_path
            )
        else:
            destination = os.path.join(destination, file)
            os.mkdir(destination)
            file_transfer(cur_path, destination)
