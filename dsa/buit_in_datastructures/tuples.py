# Tuples
# Tuples are immutable
# the contents of tuple are enclosed in ()


# creating a tuple
car = ("ford", "raptor", 2019, "Red")
print(car)

print(len(car))
print(car[1])
print(car[2:])


# merging tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

# nested tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# search
cities = ('london', 'paris', 'los angels', 'tokyo')
print('moscow' in cities)
print(cities.index('tokyo'))

