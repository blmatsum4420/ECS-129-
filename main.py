import random
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
    x_coords_plusrad = []
    y_coords_plusrad = []
    z_coords_plusrad = []
    x_coords_minusrad = []
    y_coords_minusrad = []
    z_coords_minusrad = []
    for obj in sphere_storage:
        x_coords_plusrad.append(float(obj.x)+float(obj.radius))
        y_coords_plusrad.append(float(obj.y)+float(obj.radius))
        z_coords_plusrad.append(float(obj.z)+float(obj.radius))
        x_coords_minusrad.append(float(obj.x)-float(obj.radius))
        y_coords_minusrad.append(float(obj.y)-float(obj.radius))
        z_coords_minusrad.append(float(obj.z)-float(obj.radius))
    xmax = math.ceil(max(x_coords_minusrad))
    xmin = math.floor(min(x_coords_minusrad))
    ymax = math.ceil(max(y_coords_minusrad))
    ymin = math.floor(min(y_coords_minusrad))
    zmax = math.ceil(max(z_coords_minusrad))
    zmin = math.floor(min(z_coords_minusrad))
    return xmax,xmin,ymax,ymin,zmax,zmin

def random_points():
    n_input = int(input("Please give N number of points: "))
    for i in range(n_input):
        random_plots.append((random.randrange(xmin,xmax),random.randrange(ymin,ymax)))

def overlap_check():
    overlap_in_circle = 0
    no_overlap_in_circle = 0
    for out in random_plots:
        for center in sphere_storage:
            if ((float(out[0]) - float(center.x))**2) + ((float(out[1]) - float(center.y))**2) < float(center.radius)**2:
                overlap_in_circle += 1
            else:
                no_overlap_in_circle += 1
    return overlap_in_circle, no_overlap_in_circle

def protein_vol():
#quation is (xmax-xmin)(ymax-ymin)(zmax-zmin)(points in union of balls/total of point)

def plot_data():
    for sphere in sphere_storage:
        plt.scatter(float(sphere.x),float(sphere.y), c = 'blue')
    for points in random_plots:
        plt.scatter(float(points[0]),float(points[1]), c = 'red')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('sample_data')
    plt.show()

#will auto run main fxn at start of program being run
if __name__ == "__main__":
    main()   
    #trash code practices here
    xmax,xmin,ymax,ymin,zmax,zmin = max_min()
    random_points()
    overlap,noverlap = overlap_check()
    print(overlap,noverlap)
    plot_data()