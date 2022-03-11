import os
import sys
from global_variables import *
import pandas as pd
from PIL import Image


parser = ArgumentParser()
parser.add_argument('--config', default='../config_files/config.yaml', help='Config .yaml file to use for training')




def age_to_group(age):
    if 18 <= age < 30:
        return 0
    elif age > 55:
        return 1
    else:
        None


if __name__ == '__main__':

    # To read the data directory from the argument given
    # user_path = sys.argv[1]

    # To read the data directory from the argument given
    args = parser.parse_args()
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    print(config)

    # To read the data directory from the argument given
    user_path = config['user_path']

    txt = []

    for filename in os.listdir(user_path + clean_images_path):
        if '.DS_Store' in filename:
            continue
        print(filename)
        age = int(filename.split('_')[0])
        group = age_to_group(age)
        if group != None:
            strline = filename + ' %d\n' % group
            txt.append(strline)

    with open('files/gan_train.txt', 'w') as f:
        f.writelines(txt)

    df = pd.read_csv('files/gan_train.txt', sep=' ', names=['name', 'age'])

    for index in range(len(df['name'])):
        img = Image.open(PATH_TO_IMAGES + df['name'][index])
        img.save(user_path + "/data/images_aws/" + df['name'][index])
        # change local path if needed
