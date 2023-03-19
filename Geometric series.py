# Sum of a following geometric series: 1, 0.5, 0.25... equals 2. Using while and break check if more than
# 100 elements are required to get a difference between sum elements and 2 which is lower than 0.001.
# If yes - how many elements are required?

# formula for geometric series: x = a * (r**n)

a = 1  # first term of geometric series
r = 0.5  # common ratio = 0.5 by default
count = 0  # current term count
sum_1 = 0

while True:
    term = a * (r ** count)  # 1* (0.5 ** 0) -> term = 1
    sum_1 += term  # sum = 0 + 1 = 1
    count += 1  # add number of counts

    if abs(sum_1 - 2) < 0.001 and count > 100:
        print("Number of terms required:", count)
        break
