def generator():
    for i in range(5):
        yield i

gen_object = generator()
print(type(gen_object))
for i in gen_object:
    print(i)