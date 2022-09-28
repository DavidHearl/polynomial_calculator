from time import sleep
from functools import reduce
import random
from tqdm import tqdm

# Define Arrays
solutions = []

sequence = [34, 41, 51]
index = [2, 4, 6]
ranges = [[-1, 1], [-1, 3], [-1, 3], [-10, 50]]
tolerance = [10, 5, 1, 0.5, 0]
iteration = [50, 75, 50, 50]

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


# Logic Function - Formula ((index + index_skew) ^ exponent * multiplication) + addition)
def logic():
    for  i in tqdm(range(tolerance[0])):
        index_skew = round(random.uniform(ranges[0][0], ranges[0][1]), 3)
        for ii in range(tolerance[1]):
            exponent = round(random.uniform(ranges[1][0], ranges[1][1]), 3)
            for iii in range(tolerance[2]):
                multiplication = round(random.uniform(ranges[2][0], ranges[2][1]), 3)
                for iv in range(tolerance[3]):
                    addition = round(random.uniform(ranges[3][0], ranges[3][1]), 2)
                    x1 = round((pow(sequence[0] + index_skew, exponent) * multiplication) + addition, 2)
                    x2 = round((pow(sequence[1] + index_skew, exponent) * multiplication) + addition, 2)
                    x3 = round((pow(sequence[2] + index_skew, exponent) * multiplication) + addition, 2)
                    if 33.5 <= x1 <= 34.5 and 40.5 <= x2 <= 41.5 and 50.5 <= x3 <= 51.5:
                        solutions.append([index_skew, exponent, multiplication, addition])
                    if x1 == 34 and x2 == 41 and x3 == 51:
                        print(index_skew, exponent, multiplication, addition)


for i in range(len(solutions)):
    print(solutions[i], sep="\n")

print("Tested:", "{:,}".format(5*50*50*50), "Calculations - ", "{:,}".format(len(solutions)), "Solutions")