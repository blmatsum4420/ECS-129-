from optimized import *

input_file = "C:/Users/mahtz/Documents/GitHub/ECS-129-/sample_data.txt"

print("running")
# for n_iteration in range(1,100000,10000):
#     print("doing", n_iteration)
#     what_n = []
#     output_file = "C:/Users/mahtz/Documents/GitHub/ECS-129-/text" + str(n_iteration) + str(".txt")
#     f = open(output_file, "w")
#     sum_tracker = 0
#     for b in range(100):
#         volume_protein = main(n_iteration,input_file)
#         f.write(str(n_iteration) + " " + str(volume_protein) + "\n")
#         sum_tracker += volume_protein
#     what_n.append(n_iteration)
#     f.close()
#     print("done", n_iteration)

output_file = "C:/Users/mahtz/Documents/GitHub/ECS-129-/text" + str(100000) + str(".txt")
f = open(output_file, "w")
for b in range(100):
    print(b)
    volume_protein = main(100000,input_file)
    f.write(str(100000) + " " + str(volume_protein) + "\n")
f.close()
print("done", n_iteration)
