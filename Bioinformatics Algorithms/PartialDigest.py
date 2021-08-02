import math
from itertools import combinations


def PartialDigest(l):
    # -------------------------------------------
    def number_of_cuts(l_size):
        # factorized formula from the general formula of the 2 roots  (+ve root)
        n_cuts = (1 + math.sqrt(1 + 8 * l_size)) / 2
        return math.ceil(n_cuts)
    # -------------------------------------------
    # print("l = ", l)
    n = number_of_cuts(len(l))
    l2 = list(set(l))
    m = l2.pop(-1)
    comb2 = combinations(l2, n-2)
    solutions = []
    for i in list(comb2):
        i = list(i)
        i.insert(0, 0)
        i.append(m)
        # print(i)
        delta_x = delta_X(i)
        if delta_x == l:
            solutions.append(i)
            # print("--" * 24)
            # print("i       = ", i)
            # print("delta_x = ", delta_x)
            # print("l       = ", l)
    return solutions
# =====================================================


#  matrix that calculate the the lengths of certain restriction points
# functions get the lengths of DNA according to the given restriction points (positions of cuts)
def delta_X(restriction_points):
    sorted(restriction_points)     # sort the positions of cuts
    delta_x = []
    for j in range(len(restriction_points)):
        for i in range(j + 1, len(restriction_points)):
            delta_x.append(restriction_points[i] - restriction_points[j])
    return sorted(delta_x)

# =============================================================================================================

# == Delta X testing unit ===================


'''
print("--"*30)
cut = [0, 2, 4, 7, 10]
print(delta_X(cut))
cut2 = [0, 1, 2, 5, 7, 9, 12]
cut3 = [0, 1, 5, 7, 8, 10, 12]
x1 = delta_X(cut2)
x2 = delta_X(cut3)
print("lengths of x1", x1)
print("lengths of x2", x2)
print("is x1 == x2 ", x1 == x2)
'''
# ========================================
print("Brute Force Partial Digest Algorithm ")
print("--"*50)

# == Partial Digestion testing unit =====

L1 = [1, 2, 2, 3, 4, 5]                  # n = 4                 # [[0, 1, 3, 5], [0, 2, 4, 5]]
L2 = [2, 3, 5, 5, 7, 10]                 # n = 4                 # [[0, 3, 5, 10], [0, 5, 7, 10]]
L3 = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]     # n = 5                 # [[0, 2, 4, 7, 10], [0, 3, 6, 8, 10]]

# n = 7   [[0, 1, 2, 5, 7, 9, 12], [0, 1, 5, 7, 8, 10, 12], [0, 2, 4, 5, 7, 11, 12], [0, 3, 5, 7, 10, 11, 12]]
L4 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]

print(PartialDigest(L1))
print("--"*50)
print(PartialDigest(L2))
print("--"*50)
print(PartialDigest(L3))
print("--"*50)
print(PartialDigest(L4))

# =======================================

