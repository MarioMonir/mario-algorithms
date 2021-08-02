#  testing unit

print("you can enter 5 binary strings with 5 bits ")
s1 = input("Enter first string  ")
s2 = input("Enter second string ")
s3 = input("Enter third string  ")
s4 = input("Enter fourth string ")
s5 = input("Enter fifth string  ")
"""
s1 = "10011"
s2 = "01101"
s3 = "10010"
s4 = "11111"
s5 = "10001"
"""
gene_list = [s1, s2, s3, s4, s5]
reproduction_list = [s1, s2]

print("The genes are")
print(gene_list)


# calculate fitness function
# fitness=5a+3bc-d+2e


def fitness_function(gene):
    a = int(gene[0])
    b = int(gene[1])
    c = int(gene[2])
    d = int(gene[3])
    e = int(gene[4])

    f = 5 * a + 3 * b * c - d + 2 * e
    return f


def crossover(gene1, gene2, gene3):
    # bits of gene1 and gene2 and gene3

    a1 = gene1[0]
    b1 = gene1[1]
    c1 = gene1[2]
    d1 = gene1[3]
    e1 = gene1[4]

    a2 = gene2[0]
    b2 = gene2[1]
    c2 = gene2[2]
    d2 = gene2[3]
    e2 = gene2[4]

    a3 = gene3[0]
    b3 = gene3[1]
    c3 = gene3[2]
    d3 = gene3[3]
    e3 = gene3[4]

    gene1 = a1 + b2 + c2 + d1 + e1
    gene2 = a2 + b1 + c1 + d2 + e2
    # bits of gene2 after crossover

    a4 = gene2[0]
    b4 = gene2[1]
    c4 = gene2[2]
    d4 = gene2[3]
    e4 = gene2[4]

    gene2 = a2 + b3 + c3 + d2 + e2
    gene3 = a3 + b4 + c4 + d3 + c3

    crossover_list = [gene1, gene2, gene3]
    return crossover_list


list = crossover(s3, s4, s5)

# passing every string to fitness function
f_list = [] * 5
for i in gene_list:
    f_list.append(fitness_function(i))
print("their fitness value")
print(f_list)

# concatenation first two strings and the last 3 string after crossover
for j in list:
    reproduction_list.append(j)
print("The new childers")
print(reproduction_list)

# passing genes to fitness function after crossover
f_list = []
for k in reproduction_list:
    f_list.append(fitness_function(k))
print("their fitness value")
print(f_list)








