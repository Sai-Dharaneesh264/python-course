# Set
# set is an unordered collection data items
# it is not indexed, so we can't access elements using indices or get()
 

 # creating a set
random_set = {"Educative", 1408, 3.142, (True, False)}
print(random_set)
print(len(random_set))


 # using set() constructor
empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

# adding elements
empty_set.add(1)
print(empty_set)

# update elements
empty_set.update([2, 2, 3, 4, 5, 6])
print(empty_set)

# deleting elements
print(random_set)

# discard() method will not generate error if the item is not present
random_set.discard(1408)
print(random_set)

# remove() method will generate error if the item is not present
# random_set.remove(3.123) this method will generate error since 3.123 is not set


# iterating a set
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if (not num % 2 == 0):
        odd_list.append(num)

print(odd_list)


## SET THEORY


# UNION
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

# INTERSECTION
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))


# DIFFERENCE
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))