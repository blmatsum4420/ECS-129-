import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d

ax = plt.axes(projection ='3d')

# for now
xmin = 2
xmax = 20
ymin = 0
ymax = 20
zmin = 0
zmax = 30
ball1x =  5
ball1y = 10
ball1z = 10
ball1r = 10
class Point (object):
    def __init__(self, x, y, z, radius):
        self.x, self.y, self.z, self.radius = radius

    def dist_from(self, x,y,z,radius):
        # change to include the radius
        # for now works assuming each point has no volume
        return math.sqrt( (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2)

def plot():
    # have the user input how many points here. More points = more accurate volume caclucation
    N = int(input("Number of points: "))
    # check counter with incredment if point is in ball
    counter = 0
    color = np.random.rand(100)
    for i in range(N):
        check = 0
        # choose random point within the boundary conditions
        R = np.random.uniform(0,1)
        x = xmin + R*(xmax - xmin)
        y = ymin + R*(ymax - ymin)
        z = zmin + R*(zmax - zmin)
        d = math.sqrt((x - ball1x)**2 + (y - ball1y)**2 + (z - ball1z)**2)
        print("This is value of d:", d)
        # plot random point
        ax.scatter(x, y, z,s = 5)
        #plot ball
        #ax.scatter(ball1x, ball1y, ball1z,s = ball1r)
        # this should actually check ALL the balls
        check_point(d,ball1r)
        counter += check
        #plt.plot(x,y, marker = 'o', markersize = 5)

    #plt.plot(ball1x, ball1y, marker = 'o', markersize = ball1r)
    plt.show()
    return volume_of_box() * ( counter / N)

def check_point(d, radius):
    for i in range(200):
        if d < ball1r:
            check = 1
            break

    return check

def volume_of_box():
    #xmin must be minimum coordinate + min radius 
    #ymin must be minimum coordinate + min radius
    volume = ((xmax-xmin) * (ymax-ymin) * (zmax- zmin))
    print(volume)
    return volume

def random_points():
    #creates N number of random coordinates
    number_of_darts = input("Input random N: ")
    coords = np.random.rand(n,2)*2
    #plot coordinates or check as we got?
    return 
    
def volume_of_protein():
    return 0

def main():
    f = open(input("coordinate file"), 'r')
    num_protein = f.readline()
    
    big_arr = []
    
    while(f.readline()):
        # read each line
        cur_coords = f.readline()
        # split each line by whitespace and get the 3-D coordinates and radius
        x,y,z,rad = cur_coords.split()
        # store each point in the object
        cur_point = Point(x,y,z,rad)
        # add object to an array of points
        big_arr.append(cur_point) 

    return 0
volume_of_box()
plot()