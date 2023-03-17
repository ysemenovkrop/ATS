# Basic variables and print
# Create a basic Hello World program as follows: create two strings, one for each word.
# Create a third variable, which will concatenate two previous variables, and then show its contents.

a = "Hello "
b = "World"
print(a + b)

# Following exercises about lists:
# Create a list of three names.
# Add a fourth name at the end of the list.
# Add another name at the beginning of the list.
# Delete third element from the list.
# Show the number of elements on the list.
# Using Python syntax to check if following names are on the list: Anna, John, Siegfried

list_1 = ["Jan", "Stepan", "Bob"]
list_1.append("Smith")  # insert value to the end
print(list_1)
list_1.insert(0, "Vasyl")  # add item to the specific position
print(list_1)
list_1.remove("Bob")  # removing specific value
list_1.pop(3)  # removing and indexed value
print(list_1)
print(len(list_1))  # checking the length of the list

# Create a list containing your three lucky numbers.
# Concatenate two lists.
# Create a new list, which will be a list of all three lists available in the notebook.
# Create a copy of the list of lists.
# Clear the original list of lists.
# Find Python 3.6 documentation for lists.

list_2 = [1, 2, 3]
list_3 = list_1 + list_2
print(list_3)

list_of_lists = [list_1, list_2, list_3]
print(list_of_lists)
copy_of_list = list_of_lists.copy()  # .copy method is used to copy the list
print(copy_of_list)
print(list_of_lists == copy_of_list)

# ## Sets
# Create three sets of colors: colorsRainbow, colorsRGB, colorsCMYK, and do the following exercises:
# Add white to rainbow.
# Delete "K" color from CMYK.
# Create a set of these colors, which are both in rainbow and RGB.
# Create a set of these colors, which are in rainbow and are not in CMYK.
# Create a set which contains colors from all sets.
# Make a list of the set of all colors.

colorsRainbow = set(["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
colorsRGB = set(["red", "green", "blue"])
colorsCMYK = set(["cyan", "magneta", "yellow", "black"])

colorsRainbow.add("white") # adding a white color
#print(colorsRainbow)

colorsCMYK.discard("black")
#print(colorsCMYK)

colors_Rainbow_RGB = colorsRainbow.intersection(colorsRGB)
print(colors_Rainbow_RGB)

unique_colors = colorsRainbow.difference(colorsCMYK)
print(unique_colors)

merge_colors = colorsRainbow.union(colorsRGB, colorsCMYK)
print(merge_colors)

list_colors = list(merge_colors)
print(list_colors)
print(type(list_colors))

# ## Dictionaries
# Create an English-Polish (or another foreign language) dictionary,
# which contains your three favorite English words and then:
# Add "author", which will contain your first name and surname.
# Delete the second added word from dictionary.
# Create a dictionary, which will be a translation of the previous dictionary. (inverse dictionaries)
# Concatenate two existing dictionaries.
# Find Python 3.6 documentation for dictionaries.

dic_1 = {"cat": "kot", "dog": "pies"}
print(type(dic_1))
print(dic_1)
dic_1["author"] = "Yurii Semenov"
print(dic_1)
del dic_1["dog"]
print(dic_1)
# inverse dictionary
dic_2 = {}
# iterate through the key and value in
for key, value in dic_1.items():
    dic_2[value] = key
print(dic_2)
# union of the dictionaries
dic_3 = dic_1.update(dic_2)
print(dic_3)

# Create the following two tuples:
# Tuple containing your name, surname and year of birth.
# Tuple containing three lists: colorsRainbow, colorsRGB, colorsCMYK

tuple_1 = ("Yurii", "Semenov", "1997")
print(type(tuple_1))
tuple_2 = merge_colors
print(tuple_2)
print(type(tuple_2))
print(tuple_2)
tuple_3 = (colorsRainbow, colorsRGB, colorsCMYK)
print(type(tuple_3))
print(tuple_3)

# Please write function which returns index of given pattern in the list.
# If pattern does not exist in the list,function returns -1

q = "Gorge"
list1 = ["Bob", "John", "green"]
def my_fun(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return(i)
    return -1

print(my_fun(list1,q))










