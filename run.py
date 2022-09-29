from time import sleep
from functools import reduce
import random
from tqdm import tqdm

# Define Arrays
index_skew_array = []
exponent_array = []
multiplication_array = []

sequence = [34, 41, 51]
index = [2, 4, 6]
ranges = [[0.4, 3.9], [1.618, 1.8], [2.183, 2.5]]
# tolerance = [20, 10, 5, 2.5, 1.25, 0.625, 0.25, 0]
tolerance = [20, 15, 10, 5, 4, 3, 2, 1, 0.5, 0.1]
iteration = [150, 200, 150]

# Check Calulation
# print(round((pow(index[0] + 0.4, 1.618) * 2.183) + 25, 2))
# print(round((pow(index[0] + 3.89, 1.462) * 2.245) + 11, 2))
# print(round((pow(index[0] + -0.41, 1.766) * 2.470) + 45.4, 2))

# Create arrays for upper and lower sequence then work out values
upper_sequences = []
lower_sequences = []

for x in range(len(tolerance)):
    lower_seq = []
    upper_seq = []
    for y in range(len(sequence)):
        lower_seq.append(round(sequence[y] * (1-(tolerance[x]/100)), 3))
        upper_seq.append(round(sequence[y] * (1+(tolerance[x]/100)), 3))
    lower_sequences.append(lower_seq)
    upper_sequences.append(upper_seq)

# Get total number of calculations performed
total_calculations = 1
for i in range(len(iteration)):
    total_calculations *= iteration[i]

# Generate Iterations
index_skew = []
index_skew_range = (ranges[0][1] - ranges[0][0]) / (iteration[0]-1)
for i in range(iteration[0]):
    index_skew.append(round(ranges[0][0] + (i * index_skew_range), 3))

exponent = []
exponent_range = (ranges[1][1] - ranges[1][0]) / (iteration[1]-1)
for i in range(iteration[1]):
    exponent.append(round(ranges[1][0] + (i * exponent_range), 3))

multiplication = []
multiplication_range = (ranges[2][1] - ranges[2][0]) / (iteration[2]-1)
for i in range(iteration[2]):
    multiplication.append(round(ranges[2][0] + (i * multiplication_range), 3))

print(index_skew_range, exponent_range, multiplication_range)


# Logic Function - Formula ((index + index_skew) ^ exponent * multiplication) + addition)
for x in range(len(tolerance)):
    for i in tqdm(range(iteration[0])):
        for ii in range(iteration[1]):
            for iii in range(iteration[2]):
                x1 = round((pow(index[0] + index_skew[i], exponent[ii]) * multiplication[iii]), 2)
                x2 = round((pow(index[1] + index_skew[i], exponent[ii]) * multiplication[iii]), 2)
                x3 = round((pow(index[2] + index_skew[i], exponent[ii]) * multiplication[iii]), 2)
                if (
                    lower_sequences[x][0] <= x1 <= upper_sequences[x][0] and
                    lower_sequences[x][1] <= x2 <= upper_sequences[x][1] and
                    lower_sequences[x][2] <= x3 <= upper_sequences[x][2]
                    ):
                    if (x2 - x1) - tolerance[x] <= sequence[1] - sequence[0] <= (x2 - x1) + tolerance[x]:
                        index_skew_array.append(index_skew[i])
                        exponent_array.append(exponent[ii])
                        multiplication_array.append(multiplication[iii])
                if x1 == sequence[0] and x2 == sequence[1] and x3 == sequence[2]:
                    print(index_skew, exponent, multiplication)
    print("Tested:", "{:,}".format(total_calculations), "Calculations - ","{:,}".format(len(index_skew_array)), "Solutions @", tolerance[x], "%")
    ranges[0][0] = round(min(index_skew_array) * 0.90, 3)
    ranges[0][1] = round(max(index_skew_array) * 1.1, 3)
    ranges[1][0] = round(max(exponent_array) * 0.90, 3)
    ranges[1][1] = round(max(exponent_array) * 1.10, 3)
    ranges[2][0] = round(max(multiplication_array) * 0.90, 3)
    ranges[2][1] = round(max(multiplication_array) * 1.10, 3)
    for w in range(3):
        print(ranges[w][0], ranges[w][1])

    index_skew_array.clear()
    exponent_array.clear()
    multiplication_array.clear()

# for i in range(len(solutions)):
#     print(solutions[i], sep="\n")
