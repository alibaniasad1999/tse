import glob
import pandas as pd
import os

def read_data(path=None):
    if path is None:
        path = "DataLearning/"
    print(path)
    print(os.listdir(path))
    files = glob.glob(path + "*.csv")
    data = {}
    for file in files:
        data[file.split("/")[-1].split(".")[0]] = pd.read_csv(file)
    return data 