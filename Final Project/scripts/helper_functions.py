import gdown
from pathlib import Path
from global_variables import *


def generate_dir_if_not_exists(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_file_from_google_drive(file_id, out_file_path_name):
    url = 'https://drive.google.com/uc?id=' + file_id
    gdown.download(url, out_file_path_name, quiet=False, resume=True)
