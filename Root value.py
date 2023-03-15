# Please write function,which finds root value of monotonic function on given interval.
# Input parameters: function formula,starting/ending point of interval. Use bisection method.
A = 0
B = 10
eps = 0.001
fun_1 = lambda x: x ** 2 - 4
fun_2 = lambda x: x ** 2 - 9


def findroot(A, B, eps, fun):
    m = A + (B - A) / 2
    while (abs(fun(m) > eps)):
        if (fun(A) * fun(m) < 0):
            A = A
            B = m
        else:
            B = B
            A = m
        m = A + (B - A) / 2
    return m


print(findroot(A, B, eps, fun_1))
print(findroot(A, B, eps, fun_2))
