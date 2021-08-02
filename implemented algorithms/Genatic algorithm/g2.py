from random import randint

listg = []


number=int(input("Enter Number of genes  "))
for k in range(0,number):
  genes=input("Enter gene in binary string of 9 bits  ")
  listg.append(genes)

"""
number = 4
listg[0] = "111111111"
listg[1] = "101010101"
listg[2] = "101100110"
listg[3] = "000100000"
"""

ng = int(input("Enter number of generations "))


def fitness_function(gene):
    d1 = gene[0:3]

    d2 = gene[1:4]

    d3 = gene[2:5]

    d4 = gene[3:6]

    d5 = gene[4:7]

    d6 = gene[5:8]

    d7 = gene[6:9]

    # compare every substring of the gene with the fixed string f
    f = "010"
    fitness = 0
    listf = [d1, d2, d3, d4, d5, d6, d7]
    for i in listf:
        if (i == f):
            fitness = fitness + 1
    return fitness


fitness_list = []
templist = []
# passing every string to the fitness_function to calculate the fitness value
for j in listg:
    fitness_list.append(fitness_function(j))
    templist.append(fitness_function(j))
# print(fitness_list)

# finding the first max of the fitness values
max1 = max(templist)
# finding index of the max in the list
index1 = fitness_list.index(max1)
# remove max from temp list
templist.remove(max1)

max2 = max(templist)
index2 = fitness_list.index(max2)

# print(fitness_list)

min = min(fitness_list)
index3 = fitness_list.index(min)


def crossover_function(index1, index2):
    g1 = listg[index1]
    g2 = listg[index2]

    first_bits1 = g1[0:6]
    last_bits1 = g1[6:9]

    first_bits2 = g2[0:6]
    last_bits2 = g2[6:9]

    g1 = first_bits1 + last_bits2
    g2 = first_bits2 + last_bits1

    listg[index1] = g1
    listg[index2] = g2


def mutation_function(index3):
    g3 = listg[index3]

    first_bits3 = g3[0:2]
    last_bits3 = g3[3:9]
    mutated_bit = g3[2]

    if (mutated_bit == "0"):
        mutated_bit = "1"
    else:
        mutated_bit = "0"

    g3 = first_bits3 + mutated_bit + last_bits3

    listg[index3] = g3


for l in range(0, ng):
    crossover_function(index1, index2)
    mutation_function(index3)
    print(l, "generation")
    print(listg)


