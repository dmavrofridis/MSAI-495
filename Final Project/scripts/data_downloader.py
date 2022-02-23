from helper_functions import *
import os
from global_variables import *


def download_mat_file():
    # Get the file from the URL
    if not os.path.exists(mat_dataset_path):
        get_file_from_google_drive(mat_dataset_id, mat_dataset_path)
    else:
        print("File already exists, skipping the download..")
    # Code will pause here until the file is downloaded, a progress bar keeps the user informed
    # regarding the progress


def download_images_file():
    # Get the file from the URL
    if not os.path.exists(images_dataset_path):
        get_file_from_google_drive(images_dataset_id, images_dataset_path)
    else:
        print("File already exists, skipping the download..")
    # Code will pause here until the file is downloaded, a progress bar keeps the user informed
    # regarding the progress


if __name__ == '__main__':
    generate_dir_if_not_exists("../downloaded_files")
    download_mat_file()
    download_images_file()
    print("All files have been downloaded, you can now use the program.")
