from collections import Counter
print(Counter('superfluous'))


counter = Counter('superfluous')
print(counter)

# counter.elements()
print('elements:', list(counter.elements()))


# counter.most_common(n) will get top n most common items
print('most common:', counter.most_common(3))



counter_two = Counter('super')
print(counter.subtract(counter_two))
print('subtract example:', counter)