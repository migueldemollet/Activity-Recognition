import numpy as np
import pandas as pd
import glob
import os


def train_model() -> None:
    pass

def prepare_data() -> None:
    if os.path.exists("data/idle/idle.csv"):
        os.remove("data/idle/idle.csv")

    if os.path.exists("data/running/running.csv"):
        os.remove("data/running/running.csv")

    if os.path.exists("data/stairs/stairs.csv"):
        os.remove("data/stairs/stairs.csv")

    if os.path.exists("data/idle/idle.csv"):
        os.remove("data/idle/idle.csv")

    if os.path.exists("data/walking/walking.csv"):
        os.remove("data/walking/walking.csv")

    if os.path.exists("data/dataset.csv"):
        os.remove("data/dataset.csv")

    all_files_idle = glob.glob("data/idle/*.csv")
    all_files_running = glob.glob("data/running/*.csv")
    all_files_stairs = glob.glob("data/stairs/*.csv")
    all_files_walking = glob.glob("data/walking/*.csv")

    df_from_each_file_idle = (pd.read_csv(f) for f in all_files_idle)
    df_from_each_file_running = (pd.read_csv(f) for f in all_files_running)
    df_from_each_file_stairs = (pd.read_csv(f) for f in all_files_stairs)
    df_from_each_file_walking = (pd.read_csv(f) for f in all_files_walking)

    pd.concat(df_from_each_file_idle, axis=0, ignore_index=True).to_csv("data/idle/idle.csv", index=False)
    pd.concat(df_from_each_file_running, axis=0, ignore_index=True).to_csv("data/running/running.csv", index=False)
    pd.concat(df_from_each_file_stairs, axis=0, ignore_index=True).to_csv("data/stairs/stairs.csv", index=False)
    pd.concat(df_from_each_file_walking, axis=0, ignore_index=True).to_csv("data/walking/walking.csv", index=False)

    df1 = pd.read_csv("data/idle/idle.csv")
    df2 = pd.read_csv("data/running/running.csv")
    df3 = pd.read_csv("data/stairs/stairs.csv")
    df4 = pd.read_csv("data/walking/walking.csv")  
    pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True).to_csv("data/dataset.csv", index=False)

def main() -> None:
    prepare_data()

if __name__ == '__main__':
    main()