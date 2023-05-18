# Task 1
# approximation of the constant "e"
# e = 2.71828

import math

tol = 0.001  # tolerance
diff = 1  # difference
k = 1  # step -> k up -> better approximation
while diff > tol:
    diff = math.e - abs(math.pow((1 + 1 / k), k))
    print("1. k = ", k, "2. discrete approximation of the continuous formula: ", math.pow((1 + 1 / k), k),
          "3. difference = ", diff)
    k += 1
    if k > 1500:
        print("Value of tol (tolerance) is probably wrong... break.")
        break  # just practicing the break statement

# Task 2
# Please write function which returns index of given pattern in the list.
# #If pattern does not exist in the list,function returns -1.

x = [1, 2, 3, 4, 5]


def fun_index(lst, p):
    for i in range(len(lst)):
        if lst[i] == p:
            return i

    return -1


print(fun_index(x, 4))
