def string_copy(DNA_String):
    DNA_clone=""
    for i in range(len(DNA_String)):
        DNA_clone = DNA_clone + DNA_String[i]
    pass
    return DNA_clone
    pass


# unit test
DNA1 = "ATGCTATGCTTGACTGATCATTGAAGCTGATC"
DNA2 = string_copy(DNA1)

print("DNA1 = ", DNA1)
print("DNA2 = ", DNA2)

"""
To make 2 n copies of a string of length m,
• Cell: O ( n ) steps
• Computer: O ( m * 2^n ) steps.
"""

my_list = [1,2,3,3,4,54,5,65,66,6,7,7,7,7,88,89,9,9,0,0,0,2,2,3,3,4,4,4,1,1]
my_list = list(set(my_list))
print(my_list)