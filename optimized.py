import random
import numpy as np
import matplotlib.pyplot as plt
import math 

def get_max_min(input_file):
    #reads the input file and inputs all data into sphere storage as a series of tuples.  
    #function also reads all x,y,z values, alters them +/- of radius, and find the max and min of each coordinate plane
    sphere_storage = []
    f = open(input_file, 'r')

    num_protein = f.readline()
    x_max = np.NINF
    x_min = np.Inf
    y_max = np.NINF
    y_min = np.Inf
    z_max = np.NINF
    z_min = np.Inf

    for line in f:
        cur_coords = line
        x,y,z,rad = cur_coords.split()
        x_add = float(x)+float(rad)
        y_add = float(y)+float(rad)
        z_add = float(z)+float(rad)
        x_neg = float(x)-float(rad)
        y_neg = float(y)-float(rad)
        z_neg = float(z)-float(rad)
        if x_add > x_max:
            x_max = x_add
        if x_neg < x_min:
            x_min = x_neg
        if y_add > y_max:
            y_max = y_add
        if y_neg < y_min:
            y_min = y_neg
        if z_add > z_max:
            z_max = z_add
        if z_neg < z_min:
            z_min = z_neg
        sphere_storage.append((x,y,z,rad)) 
    f.close()
    return x_max,x_min,y_max,y_min,z_max,z_min,sphere_storage 

def random_points(n_input,xmax,xmin,ymax,ymin,zmax,zmin):
    #creates a series of random plots that are appended to random_plots as storage, stored as tuples
    random_plots = []
    for i in range(n_input):
        random_plots.append((random.randrange(int(math.floor(xmin)),int(math.ceil(xmax))),random.randrange(int(math.floor(ymin)),int(math.ceil(ymax))),random.randrange(int(math.floor(zmin)),int(math.ceil(zmax)))))
    return random_plots

def overlap_check(random_plots,sphere_storage):
    #loops through both random_plots and sphere_storage and applies the ecludian formula to see if any random dots are in the union of a single sphere
    #if any random point is in the union of another sphere, the program will add 1 to the counter
    #uses numpy arrays instead of double for loops for optimization
    union_of_circle = 0
    np_random_plots = np.array(random_plots)
    np_sphere_storage = np.array(sphere_storage).astype(np.float)

    for out in np_random_plots:
        extended_out_array = np.repeat(out, len(np_sphere_storage)).reshape(len(out), -1).T
        distance = (extended_out_array - np_sphere_storage[:,:3])**2
        distance_sum = distance.sum(axis=1)
        within_range = np.less_equal(distance_sum, np_sphere_storage[:,3]**2)
        union_of_circle += within_range.any()
    return union_of_circle

def protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input):
    #function applies formula and returns volume of protein
    volume_of_protein = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)*(union_of_circle/n_input)
    return volume_of_protein

def plot_data(sphere_storage,random_plots):
    #funciton plots sphere points and random points
    for sphere in sphere_storage:
        plt.scatter(float(sphere[0]),float(sphere[1]), c = 'blue')
    for points in random_plots:
        plt.scatter(float(points[0]),float(points[1]), c = 'red')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('sample_data')
    plt.show()

def main(n_input,input_file, plot_toggle = "no"):
    #main funciton provides order of funciton calls
    xmax,xmin,ymax,ymin,zmax,zmin,sphere_storage = get_max_min(input_file)
    random_plots = random_points(n_input,xmax,xmin,ymax,ymin,zmax,zmin)
    union_of_circle = overlap_check(random_plots,sphere_storage)
    volume_of_protein = protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input)  
    if plot_toggle == "yes":
        plot_data(sphere_storage,random_plots) 
    return volume_of_protein

if __name__ == "__main__":
    #default test cases
    vol = main(100000)
    print(vol)

