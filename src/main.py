import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt


def train_model() -> None:
    pass

def graficas() -> None:
    pass

def plot_3d_scatter(x, y, z, title="3d puntos"):
    # Creating color map
    my_cmap = plt.get_cmap('hsv')
    
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
 
    sctt = ax.scatter3D(x, y, z,
                        alpha = 0.8,
                        c = (x+y+z),
                        cmap = my_cmap,
                        marker ='^')
                        
    plt.title(title)
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje y')
    ax.set_zlabel('Eje z')
    fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
    plt.show()

def prepare_data() -> None:

    all_files_idle = glob.glob("data/idle/*.csv")
    all_files_running = glob.glob("data/running/*.csv")
    all_files_stairs = glob.glob("data/stairs/*.csv")
    all_files_walking = glob.glob("data/walking/*.csv")

    df_from_each_file_idle = (pd.read_csv(f) for f in all_files_idle)
    df_from_each_file_running = (pd.read_csv(f) for f in all_files_running)
    df_from_each_file_stairs = (pd.read_csv(f) for f in all_files_stairs)
    df_from_each_file_walking = (pd.read_csv(f) for f in all_files_walking)

    df_idle = pd.concat(df_from_each_file_idle, axis=0, ignore_index=True)
    df_running = pd.concat(df_from_each_file_running, axis=0, ignore_index=True)
    df_stairs = pd.concat(df_from_each_file_stairs, axis=0, ignore_index=True)
    df_walking = pd.concat(df_from_each_file_walking, axis=0, ignore_index=True)

    df = pd.concat([df_idle, df_running, df_stairs, df_walking], axis=0, ignore_index=True)

    plot_3d_scatter(df_idle['accelerometer_X'], df_idle['accelerometer_Y'], df_idle['accelerometer_Z'], "3D IDLE")
    plot_3d_scatter(df_running['accelerometer_X'], df_running['accelerometer_Y'], df_running['accelerometer_Z'], "3D RUNNING")
    plot_3d_scatter(df_walking['accelerometer_X'], df_walking['accelerometer_Y'], df_walking['accelerometer_Z'], "3D WALKING")
    plot_3d_scatter(df_stairs['accelerometer_X'], df_stairs['accelerometer_Y'], df_stairs['accelerometer_Z'], "3D STAIRS")


def main() -> None:
    prepare_data()

if __name__ == '__main__':
    main()