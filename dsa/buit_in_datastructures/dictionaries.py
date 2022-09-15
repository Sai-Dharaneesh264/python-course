# Dictionary
# it is key-value pairs
# uses curly braces {}
# key: value
# it is a unordered data structure
# key should be unique
# two keys can have the same value


# creating a dictionary
empty_dict = {}
print(empty_dict)

phone_book = {"Batman": 234322, "Ghostbusters": 234134, "Cersei": 5323423, "Ghostbusters": 123432}
print(phone_book)


# using dict() contstructor
empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=2343242, Cersei=522234, Ghostbusters=123423)
print("this is using dict() constrcutor:", phone_book)


# accessing values
phone_book = {"Batman": 523423, "Cersei": 23432343, "Ghostbusters": 823423}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))


"""
    Dictionary Operations

    -> adding/updating entries
    -> removing entries
    -> length of a dictionary
    -> checking key existence
    -> copying contents
    -> dictionary comprehension

"""


# adding / updating entries

# adding new one
phone_book["Godzilla"] = 1235322
print(phone_book)

# updating the existence one
phone_book["Godzilla"] = 913234
print(phone_book)


# removing entries

# deletes the Batman key-value pair from phone_book
del phone_book["Batman"]
print(phone_book)

# pop() deletes the key and returns the value of the key
cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# popitem() deletes the last added key-value pair and returns that key-value pair
lastAdded = phone_book.popitem()
print(phone_book)
print("answer = ", lastAdded)

## length of the Dictionary
phone_book = {"Batman": 2341, "Cersei": 52334, "Ghostbusters": 1234}
print(len(phone_book))


# checking the key existence
print("Batman" in phone_book)
print("Godzilla" not in phone_book)

# copying contents
second_phone_book = {"Batman": 1234, "Jaime": 4321, "Godzilla": 1243}
phone_book.update(second_phone_book)
print('copying contents = ', phone_book)


# Dictionary comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepu", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print("houses:", houses)
print("new houses:", new_houses)