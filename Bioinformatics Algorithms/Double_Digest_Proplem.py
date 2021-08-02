import math
from itertools import combinations



def Double_Digest(l):
    DNA_length = sum(l) / 2
    #print(DNA_length)

    def complemntary_list(big_list, small_list):
        temp = big_list[:]
        for i in small_list:
            for j in temp:
                if i == j:
                    temp.remove(j)
                    break
        return temp
    # print("l = ", l)
    l2 = list(set(l))
    for i in range(1, len(l2)):
        comb = combinations(l2, i)
        for j in list(comb):
            j = list(j)
            #print(j, "Sum = ", sum(j))
            if sum(j) == DNA_length:
                print("Enzyme A cut points = ", j)
                print("Enzyme B cut points = ", complemntary_list(l, j))
                print("--"*50)


# =============================================================================================================

# ----- Double Digest testing unit ------ #

L1 = [1, 2, 3, 3, 4, 5]
Double_Digest(L1)

L2 = [1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 7, 8]
# Double_Digest(L2)
