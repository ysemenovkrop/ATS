## Flow control.
# Print 5 consecutive numbers which are greater than 247 and divisible by 3.

x = 248
count = 0

while count < 5:  # count = 0 < 5 -> go
    if x > 247 and x % 3 == 0:  # 248 % 3 != 0
        print(x)  # omit
        count += 1  # counter == 1 now
    x += 1  # 248 + 1 = 249 # go to initial condition

# Print all colors of rainbow.
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for i in rainbow:
    print(i)

# Create a list of your three favorite numbers, and then (using enumerate) modify a list in such a way that new values
# are equal to the old value multiplied by its index.

list_1 = [1, 2, 3]

for i, num in enumerate(list_1):
    new_num = i * num
    print(f"Old value: {num} | New value: {new_num}")
    list_1[i] = new_num

# Using zip() print names and surnames of movie protagonist.

names = ['Grzegorz', 'Zdzisław', 'Ryszard']
surnames = ['Brzęczyszczykiewicz', 'Dyrman', 'Ochódzki']
# without converting the results to the list or tuple -> the output will be unreadable
x = zip(names, surnames)
print(list(x))

# List comprehension
# new_list = [expression for item in iterable if condition]

# Example 1
x = [1, 2, 3]
y = [g * 0.5 for g in x]
print(x, "\n", y)

# Example 2
even_numbers = [num for num in range(1, 21) if num % 2 == 0][:10]
print(even_numbers)

# Using list comprehensions create a list of letters which are not vowels.
# sentence = "The quick brown fox jumps over the lazy dog."
# vowels = 'aeiou'

sentence = "The quick brown fox jumps over the lazy dog."
vowels = 'aeiou'

list_x = [x for x in sentence if x not in vowels and x.isalpha()]
print(list_x)

# extension where sentence is a list
sentence_1 = ["The quick brown fox jumps over the lazy dog."]
vowels_1 = 'aeiou'

# create a nested list comprehension:
# 1. iteration over the string = "The quick brown fox jumps over the lazy dog."
# 2. iteration over each character in the string = T, h, e and so on
# .isalpha method
list_y = [x for sentence_1 in sentence_1 for x in sentence_1 if x not in vowels_1 and x.isalpha()]
print(list_y)

# extension where both sentence and vowels are the lists
sentence_2 = ["The quick brown fox jumps over the lazy dog."]
vowels_2 = ["a", "e", "i", "o", "u"]  # vowels should be modified

list_a = [x for sentence_2 in sentence_2 for x in sentence_2 if x not in vowels_2 and x.isalpha()]
print(list_a)

# Choose numbers between 2 and 37 (inclusive) which have
# a remainder of 1 when divided by 3, and raise them to the power of 2.

numbers = [num ** 2 for num in range(2, 37) if num % 3 == 1]
print(numbers)

## If & while
# For every element on the list below, using if, elif and else: if element is a string: print it;
# if it is a float greater than 0: print "Float, OK";
# if it is an even int print "Even int", in every other case print "else".

theList = [2, 2.5, 3, "element", -3.532]

# if version
for x in theList:
    if type(x) == str:
        print(x)
    elif type(x) == float and x > 0:
        print("Float, OK")
    elif type(x) == int and x % 2 == 0:
        print("Even int")
    else:
        print("else", '\n')

# while version
count = 0
print("The length of the list: ", len(theList), '\n')
while count < len(theList):

    print("count at the iteration: ", count)
    x = theList[count]
    print("value of the nth element: ", x)
    if type(x) == str:
        print(x, '\n')
    elif type(x) == float and x > 0:
        print("Float, OK", '\n')
    elif type(x) == int and x % 2 == 0:
        print("Even int", '\n')
    else:
        print("else", '\n')
    count += 1

# Print consecutive Fibonacci numbers as long as sum of previous elements is lower than 100.

a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

# Sum of a following geometric series: 1, 0.5, 0.25... equals 2. Using while and break check if more than
# 100 elements are required to get a difference between sum elements and 2 which is lower than 0.001.
# If yes - how many elements are required?








