
# explicit conversion

star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1:"Anakin", 2:"Darth Vader", 3:1000}
print(star_wars_dict)



# converting to list

# tuple to list
star_wars_list = list(star_wars_tup)
print(star_wars_list)

# set to list
star_wars_list = list(star_wars_set)
print(star_wars_list)

# dictionary to list
star_wars_list = list(star_wars_dict)
print(star_wars_list)

star_wars_list = list(star_wars_dict.keys())
star_wars_list1 = list(star_wars_dict.values())
print(star_wars_list)
print(star_wars_list1)
tup = zip(star_wars_list, star_wars_list1)
print(type(tup))
dict1 = dict(tup)
print(dict1)


# converting to a tuple

star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# Converting from list
star_wars_tup = tuple(star_wars_list)  
print(star_wars_tup)

# Converting from set
star_wars_tup = tuple(star_wars_set)  
print(star_wars_tup)

# Converting from dictionary
star_wars_tup = tuple(star_wars_dict)  
print(star_wars_tup)


# Converting to a set

star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# Converting from list
star_wars_set = set(star_wars_list)  
print(star_wars_set)

# Converting from tuple
star_wars_set = set(star_wars_tup)  
print(star_wars_set)

 # Converting from dictionary
star_wars_set = set(star_wars_dict) 
print(star_wars_set)



# Converting to a Dictionary

star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

# Converting from list
star_wars_dict = dict(star_wars_list) 
print(star_wars_dict)

# Converting from tuple
star_wars_dict = dict(star_wars_tup) 
print(star_wars_dict)

# Converting from set
star_wars_dict = dict(star_wars_set) 
print(star_wars_dict)

