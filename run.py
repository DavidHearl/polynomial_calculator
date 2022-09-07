# from time import sleep
from functools import reduce
from tqdm import tqdm


# class PolynomialCalculations:
#     def __int__(self):
#         terms = [34, 41, 51]
#         a_increments = [0.05, 0.01, 0.005, 0.001]
#         b_increments = [0.05, 0.1, 0.05, 0.01]
#         c_increments = [0.05, 0.01, 0.005, 0.001]
#         d_increments = [1, 0.5, 0.1, 0.05]

#     def calculation:
#         difference1 = terms[1] - terms[0]





# sequence = [2, 4, 6]

# ranges = [2, 75, 80, 80, 60]
# t = [5, 2, 0.5, 0]

# total_calculations = reduce(lambda x, y: x * y, ranges)

# a_array = []
# b_array = []
# c_array = []
# d_array = []

# # ((n + b)^f * m) + a

# for test in range(ranges[0]):
#     a = -0.75
#     for i in tqdm(range(ranges[1])):
#         b = -1
#         for ii in range(ranges[2]):
#             c = -1
#             for iii in range(ranges[3]):
#                 d = -10
#                 for iv in range(ranges[4]):
#                     x1 = round((pow(sequence[0] + a, b) * c) + d, 2)
#                     x2 = round((pow(sequence[1] + a, b) * c) + d, 2)
#                     x3 = round((pow(sequence[2] + a, b) * c) + d, 2)
#                     if terms[0] - t[test] <= x1 <= terms[0] + - t[test] and \
#                             terms[1] - t[test] <= x2 <= terms[1] + t[test] and \
#                             terms[2] - t[test] <= x3 <= terms[2] + t[test]:
#                         a_array.append((round(a, 2))/1)
#                         b_array.append((round(b, 2))/1)
#                         c_array.append((round(c, 2))/1)
#                         d_array.append((round(d, 2))/1)
#                     d += d_increments[test]
#                 c += c_increments[test]
#             b += b_increments[test]
#         a += a_increments[test]
#     print("Tested:", "{:,}".format(total_calculations / ranges[0]),
#           "Calculations - ", "{:,}".format(len(a_array)), "Solutions")
#     # print(round(a,3), round(b,3), round(c,3), round(d,3))
#     a = (sum(a_array) / len(a_array)) - (a_increments[test] * ranges[test]) / 2
#     b = (sum(b_array) / len(b_array)) - (b_increments[test] * ranges[test]) / 2
#     c = (sum(c_array) / len(c_array)) - (c_increments[test] * ranges[test]) / 2
#     d = (sum(d_array) / len(d_array)) - (d_increments[test] * ranges[test]) / 2
#     a_array.clear()
#     b_array.clear()
#     c_array.clear()
#     d_array.clear()
#     # for x in range(len(a_array)):
#     #     print(f"a = {a_array[x]} : b = {b_array[x]} : c = {c_array[x]} : d = {d_array[x]}")

