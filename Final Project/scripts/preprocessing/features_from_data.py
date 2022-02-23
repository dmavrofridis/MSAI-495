import mat73
import os
import pandas as pd
from scripts.data_downloader import *
from scripts.global_variables import *


class GenerateInitialFeatures:  # path of the original celebrity celebrity document. "NOTE" I read from local,
    def __init__(self, original_path=mat_dataset_path):
        self.path = original_path
        # Get the file from the URL
        if not os.path.exists(original_path):
            download_mat_file()
        else:
            print("File already exists, skipping the mat file download..")
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
        generate_dir_if_not_exists('./results')
        df.to_csv('./results/imageName_age.csv')


if __name__ == '__main__':
    # Now get the datasets required
    instance = GenerateInitialFeatures()
    instance.generate_csv()