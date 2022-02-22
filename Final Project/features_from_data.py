import mat73
import os
import pandas as pd
from global_variables import *
from helper_functions import *


class GenerateInitialFeatures:  # path of the original celebrity celebrity document. "NOTE" I read from local,
    def __init__(self, original_path="./downloaded_files/celebrity2000.mat"):
        self.path = original_path
        # Get the file from the URL
        if not os.path.exists(original_path):
            get_file_from_google_drive(mat_dataset_id)
        else:
            print("File already exists, skipping the download..")
        # Code will pause here until the file is downloaded, a progress bar keeps the user informed
        # regarding the progress
        print("Loading the .mat file..")
        self.data = mat73.loadmat(original_path)

    def generate_csv(self):
        print("Generating the image name & age CSV file..")
        name = [self.data['celebrityImageData']['name'][i][0] for i in
                range(len(self.data['celebrityImageData']['name']))]
        age = self.data['celebrityImageData']['age']
        dic = {'image_name': name, 'age': age}
        df = pd.DataFrame(dic)
        # Generate the CSV file now..
        df.to_csv('./results/imageName_age.csv')
