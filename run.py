from time import sleep
from functools import reduce
import random
from tqdm import tqdm

# Define Arrays
index_skew_array = []
exponent_array = []
multiplication_array = []
addition_array = []

sequence = [34, 41, 51]
index = [2, 4, 6]
ranges = [[-2, 2], [-2, 5], [-2, 5], [-50, 50]]
tolerance = [10, 7.5, 5, 1, 0.5, 0.1, 0]
iteration = [70, 70, 70, 70]

# Create arrays for upper and lower sequence then work out values
upper_sequences = []
lower_sequences = []

for x in range(len(tolerance)):
    lower_seq = []
    upper_seq = []
    for y in range(len(sequence)):
        lower_seq.append(round(sequence[y] * (1-(tolerance[x]/100)), 2))
        upper_seq.append(round(sequence[y] * (1+(tolerance[x]/100)), 2))
    lower_sequences.append(lower_seq)
    upper_sequences.append(upper_seq)

# print(upper_sequences)
# print(lower_sequences)

# Get total number of calculations performed
total_calculations = 1
for c in range(len(iteration)):
    total_calculations *= iteration[c]

# Logic Function - Formula ((index + index_skew) ^ exponent * multiplication) + addition)
for x in range(len(tolerance)):
    for i in tqdm(range(iteration[0])):
        index_skew = round(random.uniform(ranges[0][0], ranges[0][1]), 3)
        for ii in range(iteration[1]):
            exponent = round(random.uniform(ranges[1][0], ranges[1][1]), 3)
            for iii in range(iteration[2]):
                multiplication = round(random.uniform(ranges[2][0], ranges[2][1]), 3)
                for iv in range(iteration[3]):
                    addition = round(random.uniform(ranges[3][0], ranges[3][1]), 2)
                    x1 = round((pow(index[0] + index_skew, exponent) * multiplication) + addition, 2)
                    x2 = round((pow(index[1] + index_skew, exponent) * multiplication) + addition, 2)
                    x3 = round((pow(index[2] + index_skew, exponent) * multiplication) + addition, 2)
                    if (
                        lower_sequences[x][0] <= x1 <= upper_sequences[x][0] and
                        lower_sequences[x][1] <= x2 <= upper_sequences[x][1] and
                        lower_sequences[x][2] <= x3 <= upper_sequences[x][2]
                       ):
                       index_skew_array.append(index_skew)
                       exponent_array.append(exponent)
                       multiplication_array.append(multiplication)
                       addition_array.append(addition)
                    if x1 == sequence[0] and x2 == sequence[1] and x3 == sequence[2]:
                        print(index_skew, exponent, multiplication, addition)
    print("Tested:", "{:,}".format(total_calculations), "Calculations - ","{:,}".format(len(index_skew_array)), "Solutions @", tolerance[x], "%")
    ranges[0][0] = min(index_skew_array)
    ranges[0][1] = max(index_skew_array)
    ranges[0][0] = max(exponent_array)
    ranges[0][1] = max(exponent_array)
    ranges[0][0] = max(multiplication_array)
    ranges[0][1] = max(multiplication_array)
    # print(min(index_skew_array),max(index_skew_array))
    # print(min(exponent_array),max(exponent_array))
    # print(min(multiplication_array),max(multiplication_array))
    index_skew_array.clear()
    exponent_array.clear()
    multiplication_array.clear()
    addition_array.clear()

# for i in range(len(solutions)):
#     print(solutions[i], sep="\n")
