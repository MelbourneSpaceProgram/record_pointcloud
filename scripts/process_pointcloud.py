# %%
import numpy as np
import pickle
import os
from struct import unpack, pack
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def save_obj(filename, obj):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def convert_to_rgb(rgb_fl):
    return unpack('i', pack('f', rgb_fl))[0]

def visualize(pointcloud, label):
    i = 0
    indx = np.arange(3070) * 100
    scan = pointcloud[i, indx]
    x, z, y = -scan[..., 0], -scan[..., 1], scan[..., 2]
    v = label[i, indx]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c=v)

    plt.show()

def hist_plot_colour(colour):
    plt.hist(colour, bins=50)
    plt.show()

def main():
    data = np.load(os.path.join("data", "gazebo_pointcloud.npy"))
    print("Frames: {}".format(data.shape[0]))

    pointcloud = data[...,:-1]
    colour = np.vectorize(convert_to_rgb)(data[...,-1])
    
    label = (colour > 0.8e7) & (data[..., 2] < 10)

    dataset = {"label": label, "pointcloud": pointcloud}
    save_obj(os.path.join("data", "gazebo_pc_dataset.pickle"), dataset)

    # visualize(pointcloud, label)

    hist_plot_colour(colour[0, np.where(data[0, 2] < 10)])

# %%
# i = 0
# indx = np.arange(3070) * 100
# scan = pointcloud[i, indx]
# x, y, z = -scan[..., 0], -scan[..., 1], -scan[..., 2]
# v = label[i, indx]

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.scatter(x, y, z, c=v)

# plt.show()
