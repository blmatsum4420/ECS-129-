import random
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.spatial
from scipy.spatial import Voronoi, voronoi_plot_2d, KDTree

def get_max_min(input_file):
    #reads the input file and inputs all data into sphere storage as a series of tuples.  
    #function also reads all x,y,z values, alters them +/- of radius, and find the max and min of each coordinate plane
    sphere_storage = []
    test_list = []
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

def voronoi_plot(sphere_storage,random_plots):
    union_of_circle = 0
    np_sphere_storage = np.array(sphere_storage).astype(float)
    np_random_plots = np.array(random_plots)
    voronoi_kdtree = KDTree(np_sphere_storage[:,:3])
    # print(np_sphere_storage)
    # print(np_sphere_storage[:,3])
    test_point_dist, test_point_regions = voronoi_kdtree.query(np_random_plots, k=1)
    #test_point_regions stores all the index values of nearest 
    #point from sphere_storage to each of our points in random plots
    for i in range(len(np_random_plots)):
        distance = (np_random_plots[i] - np_sphere_storage[test_point_regions[i]][:3])**2 #(3,)
        distance_sum = distance.sum()
        within_range = np.less_equal(distance_sum, np_sphere_storage[test_point_regions[i]][3:]**2)
        union_of_circle += within_range.any()
    return union_of_circle

def plot_it(sphere_storage):
    
    np_sphere_storage = np.array(sphere_storage).astype(float)
    adjusted_sphere_storage = np_sphere_storage[:,:2]
    vor = Voronoi(adjusted_sphere_storage)
    fig = voronoi_plot_2d(vor)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
        
def random_points(n_input,xmax,xmin,ymax,ymin,zmax,zmin):
    #creates a series of random plots that are appended to random_plots as storage, stored as tuples
    random_plots = []
    for i in range(n_input):
        random_plots.append((random.randrange(int(math.floor(xmin)),int(math.ceil(xmax))),random.randrange(int(math.floor(ymin)),int(math.ceil(ymax))),random.randrange(int(math.floor(zmin)),int(math.ceil(zmax)))))
    return random_plots

def protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input):
    #function applies formula and returns volume of protein
    volume_of_protein = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)*(union_of_circle/n_input)
    return volume_of_protein

def run_voronoi(n_input,input_file):
    xmax,xmin,ymax,ymin,zmax,zmin,sphere_storage = get_max_min(input_file)
    random_plots = random_points(n_input,xmax,xmin,ymax,ymin,zmax,zmin)
    union_of_circle = voronoi_plot(sphere_storage,random_plots)
    volume_of_protein = protein_vol(xmax,xmin,ymax,ymin,zmax,zmin,union_of_circle,n_input)
    return volume_of_protein, sphere_storage

if __name__ == "__main__":
    run_voronoi()