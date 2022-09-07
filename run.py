from time import sleep
from functools import reduce
import random
from tqdm import tqdm

sequence = [34, 41, 51]
index = [2, 4, 6]
solutions = []
ranges = [[-1, 1], [-1, 3], [-1, 3], [-10, 50]]

# formula = ((index + index_skew)^f * m) + a
# for iteration in range(2):
for i in tqdm(range(5)):
    index_skew = round(random.uniform(ranges[0][0], ranges[0][1]), 3)
    for ii in range(75):
        exponent = round(random.uniform(ranges[1][0], ranges[1][1]), 3)
        for iii in range(50):
            multiplication = round(random.uniform(ranges[2][0], ranges[2][1]), 3)
            for iv in range(50):
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


