from random import random
import numpy as np
import matplotlib.pyplot as plt
import math 

sphere_storage = []
random_plots = []

class Point (object):
    def __init__(self, x, y, z, radius):
        self.x, self.y, self.z, self.radius = x,y,z,radius   

def main():
    #function will read all file lines and push data into a singular class
    filename = input("Please provide data file: ")
    f = open(filename, 'r')
    num_protein = f.readline()

    for line in f:
        cur_coords = line
        # split each line by whitespace and get the 3-D coordinates and radius
        x,y,z,rad = cur_coords.split()
        # store each point in the object
        cur_point = Point(x,y,z,rad)
        # add object to an array of points
        sphere_storage.append(cur_point) 
        #increments counter
    f.close()
    return

def max_min():
    #do we need to take into account radius?  I assume so 
    x_coords = []
    y_coords = []
    z_coords = []
    for obj in sphere_storage:
        x_coords.append(obj.x)
        y_coords.append(obj.y)
        z_coords.append(obj.z)
    xmax = max(x_coords)
    xmin = min(x_coords)
    ymax = max(y_coords)
    ymin = min(y_coords)
    zmax = max(z_coords)
    zmin = min(z_coords)'
    return 

def plot_data():
    for sphere in sphere_storage:
        plt.scatter(float(sphere.x),float(sphere.y))
    for points in random_plots:
        plt.scatter(float(points[0]),float(points[1]))
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('sample_data')
    plt.show()

def random_points():
    n_input = int(input("Please give N number of points"))
    for i in range(n_input):
        random_plots.append((random.randrnage(xmin,xmax),random.randrnange(ymin,ymax)))



#will auto run main fxn at start of program being run
if __name__ == "__main__":
    main()
    max_min()   
    random_points()
    plot_data()