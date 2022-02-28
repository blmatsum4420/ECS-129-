from optimized import *

print("Welcome to Protein Volume Finder")
input_file = input("Please provide input file (sphere coordinates given as x,y,z,radius): ")
output_file = input("Please provide ouput file (contains N, protein volume): ")

if input("Would you like to do an iterative loop from 1 to N?  Yes/No: ") == "yes":
    max_input = int(input("How many random points would you like (N)? "))
    f = open(output_file, "w")
    sum_tracker = 0

    for i in range(1, max_input):
        volume_protein = main(i,input_file)
        f.write(str(i) + " " + str(volume_protein) + "\n")
        sum_tracker += volume_protein
    f.close()

    average_volume = sum_tracker / (max_input-1)

    print("The volume of your protein is: ",average_volume, "Å³")
    print("Done, have a good day!")
else:
    if input("Would you like to plot a single point once (yes) or N times (No) ") == "yes":
        n_input = int(input("How many random points would you like (N)? "))
        plot_toggle = input("Would you like to see a plot of your data and random points?  Yes/No: ")

        f = open(output_file, "w")
        volume_protein = main(n_input,input_file,plot_toggle)
        f.write(str(n_input) + " " + str(volume_protein) + "\n")
        f.close()
        print("The volume of your protein is: ",volume_protein,"Å³")
        print("Done, have a good day!")
    else:
        n_input = int(input("For what N randm points would you like to test? "))
        z_loop = int(input("How many times would you like to run the loop (1-z iterations)? "))
        
        f = open(output_file, "w")
        sum_tracker = 0
        for i in range(1, z_loop):
            volume_protein = main(n_input,input_file)
            f.write(str(i) + " " + str(volume_protein) + "\n")
            sum_tracker += volume_protein
        f.close()

        average_volume = sum_tracker / (z_loop-1)

        print("The volume of your protein is: ",average_volume, "Å³")
        print("Done, have a good day!")

#c:\Users\mahtz\Documents\GitHub\ECS-129-\sample_data.txt 