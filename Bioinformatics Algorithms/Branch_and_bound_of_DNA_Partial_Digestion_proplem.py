# ------------------------------------------------------------------------------------
def delta_y_x(point, restriction_points):
    delta_yx = []
    for i in range(len(restriction_points)):
        delta_yx.append(abs(point-restriction_points[i]))
    delta_yx = sorted(delta_yx)
    # print("delta x  = ", delta_yx)
    return delta_yx


# ------------------------------------------------------------------------------------
def subtract_list_distinct(big_list, small_list):
    for i in small_list:
        for j in big_list:
            if i == j:
                big_list.remove(j)
                break
    # print("big   list = ", big_list)
    # print("small list = ", small_list)
    return big_list


# ------------------------------------------------------------------------------------
def branch_and_bound(ls):
    # ls is already will be passed sorted
    width = ls.pop(-1)
    X = [0, width]

    def place(l, x):
        flag1 = 1
        # print("l = ", l)
        if len(l) == 0:
            return x
        y_left = l[-1]
        y_right = width - y_left
        delta_yx1 = delta_y_x(y_left, x)
        delta_yx2 = delta_y_x(y_right, x)
        if delta_yx1 == delta_yx2:
            flag1 = 0

        # print("y left = ", y_left)
        if set(delta_yx1).issubset(set(l)):
            # print("we entered to left branch")
            x.append(y_left)
            l = subtract_list_distinct(l, delta_yx1)
            # x = sorted(x)
            # print("from left l = ", l)
            # print("from left x = ", x)
            place(l, x)
            # x.remove(y_left)
            # l = l + delta_yx1

        # print("y right = ", y_right)
        if flag1:
            # print("we entered to right branch")
            if set(delta_yx2).issubset(set(l)):
                x.append(y_right)
                l = subtract_list_distinct(l, delta_yx2)
                # x = sorted(x)
                # print("from right l = ", l)
                # print("from right x = ", x)
                place(l, x)
                # x.remove(y_right)
                # l = l + delta_yx2
        return

    # print("x = ", x)
    place(ls, X)
    X = sorted(X)
    return X


# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
def PartialDigest(l):
    sorted(l)
    return branch_and_bound(l)


# ----------- Subtract list distinct ----------
'''
list1 = [1, 2, 3, 4, 4, 4, 5, 5, 6]
list2 = [2, 4, 4, 5]
print(list1)
subtract_list_distinct(list1, list2)
print(list1)
list1 = list1 + list2
list1 = sorted(list1)
print(list1)
'''

# == Partial Digestion testing unit =====
print("Branch and bound  Partial Digest Algorithm ")
print("--"*50)
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
