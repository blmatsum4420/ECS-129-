from optimized import *
from voronoi_algo import *

print("----------------------------------------------")
print("Welcome to Protein Volume Finder")
print("----------------------------------------------")

if input("Would you like to read the readme? (yes/no) ") == "yes":
    print("Test")

print("----------------------------------------------")
print("Please input file path as a direct file path without quotes eg C:/Users/...")
input_file = input("Please provide input file (sphere coordinates given as x,y,z,radius): ")
output_file = input("Please provide ouput file (contains N, protein volume): ")
print("----------------------------------------------")

print("What algorithm would you like to run? (Brute Force = B or Voronoi = V) ")
print("We suggest using Voronoi algorithm for fastest results and a N of 1000")

repeat = "yes"

while repeat == "yes":
    algo = input("Please type name of algorithm you would like to use: ")
    plot_toggle = "no"

    if algo == "B" or algo == "b":
        print("error")
        print("----------------------------------------------")
        print("Would you like to run the algorithm once, iteratively (1-N), or a loop of the same N? ")
        print("Please Note that the added graphing function is only available for a run of once given computation time")
        run_type = input("once = o,iteratively = i,loop = l: ")

        if run_type == "o":
            print("----------------------------------------------")
            n_input = int(input("How many random points would you like (N)? "))
            print("----------------------------------------------")
            plot_toggle = input("Would you like to see a plot of your data and random points?  Yes/No: ")
            f = open(output_file, "w")
            volume_protein = run_brute(n_input,input_file,plot_toggle)
            f.write(str(n_input) + " " + str(volume_protein) + "\n")
            f.close()
            if plot_toggle == "yes":
                print("----------------------------------------------")
                print("Blue Dots are sphere data points while red dots are random points")
            print("----------------------------------------------")
            print("The volume of your protein is: ",volume_protein,"Å³")

        if run_type == "i":
            print("----------------------------------------------")
            n_input = int(input("What would you like your max N to be? "))
            sum_tracker = 0
            f = open(output_file, "w")
            for i in range(1, n_input):
                volume_protein = run_brute(i,input_file)
                f.write(str(i) + " " + str(volume_protein) + "\n")
                sum_tracker += volume_protein
            f.close()
            average_volume = sum_tracker / (n_input-1)
            print("----------------------------------------------")
            print("The volume of your protein is: ",average_volume, "Å³")
        
        if run_type == "l":
            n_input = int(input("For what N random points would you like to test? "))
            z_loop = int(input("How many times would you like to run the loop (1-z iterations)? "))
            
            f = open(output_file, "w")
            sum_tracker = 0
            for i in range(1, z_loop):
                volume_protein = run_brute(n_input,input_file)
                f.write(str(i) + " " + str(volume_protein) + "\n")
                sum_tracker += volume_protein
            f.close()
            average_volume = sum_tracker / (z_loop-1)
            print("----------------------------------------------")
            print("The volume of your protein is: ",average_volume, "Å³")

    if algo == "V" or algo == "v":
        print("----------------------------------------------")
        print("Would you like to run the algorithm once, iteratively (1-N), or a loop of the same N? ")
        print("Please Note that the added graphing function is only available for a run of once given computation time")
        run_type = input("once = o,iteratively = i,loop = l: ")

        if run_type == "o":
            print("----------------------------------------------")
            n_input = int(input("How many random points would you like (N)? "))
            print("----------------------------------------------")
            plot_toggle = input("Would you like to see a plot of your data and random points (2D x,y only)?  Yes/No: ")
            f = open(output_file, "w")
            volume_protein, sphere_storage = run_voronoi(n_input,input_file)
            f.write(str(n_input) + " " + str(volume_protein) + "\n")
            f.close()
            print("----------------------------------------------")
            print("The volume of your protein is: ",volume_protein,"Å³")
            if plot_toggle == "yes":
                plot_it(sphere_storage)
                print("----------------------------------------------")
                print("Blue Dots are sphere data points while red dots are random points")

        if run_type == "i":
            print("----------------------------------------------")
            n_input = int(input("What would you like your max N to be? "))
            sum_tracker = 0
            f = open(output_file, "w")
            for i in range(1, n_input):
                volume_protein, sphere_storage = run_voronoi(i,input_file)
                f.write(str(i) + " " + str(volume_protein) + "\n")
                sum_tracker += volume_protein
            f.close()
            average_volume = sum_tracker / (n_input-1)
            print("----------------------------------------------")
            print("The volume of your protein is: ",average_volume, "Å³")
        
        if run_type == "l":
            n_input = int(input("For what N random points would you like to test? "))
            z_loop = int(input("How many times would you like to run the loop (1-z iterations)? "))
            
            f = open(output_file, "w")
            sum_tracker = 0
            for i in range(1, z_loop):
                volume_protein, sphere_storage = run_voronoi(n_input,input_file)
                f.write(str(i) + " " + str(volume_protein) + "\n")
                sum_tracker += volume_protein
            f.close()
            average_volume = sum_tracker / (z_loop-1)
            print("----------------------------------------------")
            print("The volume of your protein is: ",average_volume, "Å³")

    print("----------------------------------------------")
    repeat = input("Would you like to use another alogrithm? (yes,no): ")

print("\nDone, have a good day!")

# if input("Would you like to do an iterative loop from 1 to N?  Yes/No: ") == "yes":
#     max_input = int(input("How many random points would you like (N)? "))
#     f = open(output_file, "w")
#     sum_tracker = 0

#     for i in range(1, max_input):
#         volume_protein = main(i,input_file)
#         f.write(str(i) + " " + str(volume_protein) + "\n")
#         sum_tracker += volume_protein
#     f.close()

#     average_volume = sum_tracker / (max_input-1)

#     print("The volume of your protein is: ",average_volume, "Å³")
#     print("Done, have a good day!")
# else:
#     if input("Would you like to plot a single point once (yes) or N times (No) ") == "yes":
#         n_input = int(input("How many random points would you like (N)? "))
#         plot_toggle = input("Would you like to see a plot of your data and random points?  Yes/No: ")

#         f = open(output_file, "w")
#         volume_protein = main(n_input,input_file,plot_toggle)
#         f.write(str(n_input) + " " + str(volume_protein) + "\n")
#         f.close()
#         print("The volume of your protein is: ",volume_protein,"Å³")
#         print("Done, have a good day!")
#     else:
#         n_input = int(input("For what N randm points would you like to test? "))
#         z_loop = int(input("How many times would you like to run the loop (1-z iterations)? "))
        
#         f = open(output_file, "w")
#         sum_tracker = 0
#         for i in range(1, z_loop):
#             volume_protein = main(n_input,input_file)
#             f.write(str(i) + " " + str(volume_protein) + "\n")
#             sum_tracker += volume_protein
#         f.close()

#         average_volume = sum_tracker / (z_loop-1)

#         print("The volume of your protein is: ",average_volume, "Å³")
#         print("Done, have a good day!")

# #c:\Users\mahtz\Documents\GitHub\ECS-129-\sample_data.txt 