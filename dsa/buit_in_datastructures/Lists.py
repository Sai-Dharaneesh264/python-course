# Lists

# creating a List
json_snow = ["Jon Snow", "Winterfell", 30]
print(json_snow)

# Indexing
print(json_snow[0])

# Length
print(len(json_snow))

# Lists are mutable
print(json_snow[2])
json_snow[2] += 20
print(json_snow[2])

# using range
num_seq = range(0, 10)
print(type(num_seq))
num_list = list(num_seq)
print(num_list)

num_seq = range(3, 20, 3) # 3, 6, 9, 12, 15, 18
print(list(num_seq))

# List-Ception
world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])
print(world_cup_winners[1][1][0])

# Merging Lists
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A += part_B
print(part_A)

# we can also use extend() to merge list
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)


"""
    common list operations:
    
    -> adding elements
    -> removing elements
    -> list slicing
    -> index search
    -> list sort

"""

# adding elements
# append() is used to add element at the last of list
num_list = []
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)


# to add an element at a particular index we use insert()
a = [1, 2, 3, 4, 5]
a.insert(3, 10)
print(a)



# removing elements
# pop() is used to remove the last element from the list
# pop(index) is used to remove the element at index 
array = [1, 2, 3, 4, 5]
answer = array.pop()
print(answer)
print(array)


# if we want to remove a particular value from list
# remove() is use to remove the element
# syntax: list.remove(element_to_be_deleted)
a = [1, 2, 3, 4, 3, 2, 1]
a.remove(2)
print(a)


# list slicing
a = [1, 2, 3, 4, 5, 6, 7, 8]
slice1 = a[2:5]
slice2 = a[0::2]
print(slice1)
print(slice2)


# index search
cities = ["london", "paris", "Los Angels", "Beirut"]
print("index of london:", cities.index("london"))

# if you want to verify the existence of an element in a list we can use in operator
cities = ["london", "paris", "los angels", "beirut"]
print("london" in cities)
print("moscow" not in cities)

# list sort
a = [20, 40, 10, 50.4, 30, 100, 5, 20]
a.sort()
print(a)

# List comprehension

nums = [10, 20, 30, 40, 50]
nums_double = []
for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)



# alternative approach
nums = [10, 20, 30, 40, 50]
nums_double = [n * 2 for n in nums]
print(nums)
print(nums_double)

# adding condition
nums = [10, 20, 30, 40, 50]

nums_double = [n * 2 for n in nums if n % 4 == 0]
print(nums)
print(nums_double)


# using multiple lists

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)