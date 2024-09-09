import os
import csv
import pandas as pd


def create_datasets():
    dataset_paths = ["/train/", "/test/"]
    dataset_files = ["train_dataset.csv", "test_dataset.csv"]
    sentiment_folders = ["negative", "positive", "neutral"]
    i = 0
    for file in dataset_files:
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "sentiment"])
        for folder in sentiment_folders:
            folder_path = "data" + dataset_paths[i] + folder
            with open(file, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)

                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)
                        with open(file_path, "r") as f:
                            content = f.read()
                            writer.writerow([content, folder])
        i += 1
    return


create_datasets()
