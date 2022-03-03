from optimized import *
# from voronoi_algo import *
import time




start_time = time.time()
time_storage = []

input_file = "C:/Users/mahtz/Documents/GitHub/ECS-129-/sample_data.txt"

for b in range(100):
    volume_protein = main(100000,input_file)

print ("My program took", time.time() - start_time, "to run")

