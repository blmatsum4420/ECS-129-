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
    #issue as proper max and min not coming out
    x_coords = []
    y_coords = []
    z_coords = []
    for obj in sphere_storage:
        x_coords.append(float(obj.x)+float(obj.radius))
        y_coords.append(float(obj.y)+float(obj.radius))
        z_coords.append(float(obj.z)+float(obj.radius))
        x_coords.append(float(obj.x)-float(obj.radius))
        y_coords.append(float(obj.y)-float(obj.radius))
        z_coords.append(float(obj.z)-float(obj.radius))
    xmax = math.ceil(max(x_coords))
    xmin = math.floor(min(x_coords))
    ymax = math.ceil(max(y_coords))
    ymin = math.floor(min(y_coords))
    zmax = math.ceil(max(z_coords))
    zmin = math.floor(min(z_coords))
    return xmax,xmin,ymax,ymin,zmax,zmin

def random_points():
    n_input = int(input("Please give N number of points: "))
    for i in range(n_input):
        #is it good to add to a outside list from a fxn for storage?
        #how can we append to a global list but cannot use global varaibles without declaring
        random_plots.append((random.randrange(xmin,xmax),random.randrange(ymin,ymax)))
    return n_input

def overlap_check():
    #right now this only checks if something is inside another circle, not if its in the union of multiple circles
    union_of_circle = 0
    for out in random_plots:
        for center in sphere_storage:
            if ((float(out[0]) - float(center.x))**2) + ((float(out[1]) - float(center.y))**2) < float(center.radius)**2:
                union_of_circle += 1
                break
    return union_of_circle

def protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,n_input,union_of_circle):
#equation is (xmax-xmin)(ymax-ymin)(zmax-zmin)(points in union of balls/total of point)
#easier way to turn everything into a float at once?
    volume_of_protein = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)*(union_of_circle/n_input)
    return volume_of_protein

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
    #reads file and applies class and puts data into list
    main()   
    #find mins and max of all data
    xmax,xmin,ymax,ymin,zmax,zmin = max_min()
    print("max/min",xmax,xmin,ymax,ymin,zmax,zmin)
    #request from user number of random points wanted
    n_input = random_points()
    # checks for all points that are in union of a circle
    union_of_circle = overlap_check()
    print("# of points in union of circle: ", union_of_circle)
    #calculates volume of our protein
    volume_of_protein = protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,n_input,union_of_circle)
    #plots all data by center points only
    print("volume of protein: ",volume_of_protein)
    plot_data()