x = 300

def my_func():
    global y
    y = 200
    print(x)

my_func()
print(x)
print(y)

