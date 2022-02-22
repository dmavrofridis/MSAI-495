from descriptive_statistics import *
from features_from_data import *


def main():
    print("Program Started")

    # Generate the downloaded_files folder if doesnt exist
    generate_dir_if_not_exists("./downloaded_files")
    generate_dir_if_not_exists("./results")
    # Now get the datasets required
    instance = GenerateInitialFeatures()
    instance.generate_csv()

    df = group_age_decades()
    df = generate_of_age_distribution(df)
    df = generate_class_and_plot(df)
    df = break_names(df)
    df = most_occuring_actors(df)


if __name__ == '__main__':
    main()
