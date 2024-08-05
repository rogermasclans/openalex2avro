import os

def create_dir(dir_path):
    """
    Create a directory if it does not exist
    :param dir_path: path to the directory
    :return: path to thedirectory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def retrieve_folders_in_dir(dir_path):
    """
    Retrieve all the folders in a directory
    :param dir_path: path to the directory
    :return: list of folders
    """
    return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

def retrieve_files_in_dir(dir_path):
    """
    Retrieve all the files in a directory
    :param dir_path: path to the directory
    :return: list of files
    """
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
