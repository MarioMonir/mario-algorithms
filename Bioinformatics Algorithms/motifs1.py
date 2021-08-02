def is_subset(big_list, small_list):
    for i in small_list:
        flag = 0
        for j in big_list:
            if i == j:
                flag = 1
                big_list.remove(j)
        if flag == 0:
            return False
    return True

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3]
# print(is_subset(L1, L2))
# -------------------------------------------------------------
def sequence_finder(String_S, String_l):
    # Given a string S with |S|=s and a string L with  |L|=l such that s≤l. Decide whether or not S is
    # in L, and return the starting position of S in L if S is in L.

    for i in range(len(String_S)-len(String_l)):
        flag = 1
        if String_S[i] == String_l[0]:
            # print("at index = {}  String_S[{}] = {} == String_l[{}] = {}".format(i, i, String_S[i],0, String_l[0]))
            k = i
            for j in range(len(String_l)):
                if String_S[k] != String_l[j]:
                    # print("at index = {}  String_S[{}] = {} != String_l[{}] = {}".format(k, k, String_S[k],j, String_l[j]))
                    flag = 0
                    break
                else:
                    # print("at index = {}  String_S[{}] = {} == String_l[{}] = {}".format(k, k, String_S[k],j, String_l[j]))
                    k += 1

            if flag == 1:
                print("found at index = ", i)
                return i
# -------------------------------------------------------------
def hamming_distance(s1,s2):
    if len(s1) != len(s2):
        return "Strings are not equal in lengths"
    else:
        dis = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dis += 1
        return dis

# -------------------------------------------------------------
def ancestor(lists):
    Ancestor = ""
    for i in range(len(lists[0])):
        char = {"A": 0, "C": 0, "T": 0, "G": 0}
        for j in range(len(lists)):
            char[lists[j][i]] += 1
        Ancestor += max(char, key=char.get)
        # print(char, Ancestor)
    return Ancestor
# -------------------------------------------------------------
def Scoring_Motifs(lists):
    Ancestor = ancestor(lists)
    lists.append(Ancestor)
    print(lists)
    scores = []
    for i in range(len(lists)):
        score = 0
        for j in range(len(lists)):
            if lists[j] != lists[i]:
                score += hamming_distance(lists[i], lists[j])
        scores.append(score)
        #scores.update({str(lists[j]) : score})
        s = dict(zip(lists, scores))
    return s
# -------------------------------------------------------------

'''

def motif_finder(lists, length):
    scores = {}
    for i in range(len(lists[0])):
        sequences = []
        sequence = lists[0][i:i+length]
        sequences.append(sequence)
        for j in range(0, len(lists[0])):
            for k in range(1, lists):
                sequence = lists[k][j:j+length]
                sequences.append(sequence)


pass

'''
# ----------------------------------------------------
s1 = "ATTCGTTTAGGCTAGCCTATCGGTACACATGTG"
s2 = "CGT"
sequence_finder(s1, s2)
# ----------------------------------------------------
s3 = "AGTCT"
s4 = "ACTGT"
print("hamming distance = ", hamming_distance(s3, s4))
# ----------------------------------------------------
list1 = ["ATGCA", "ATCGA", "AGTGC", "GTCGG", "ATCCG"]
print("Ancestor = ", ancestor(list1))
# ----------------------------------------------------
print(Scoring_Motifs(list1))
