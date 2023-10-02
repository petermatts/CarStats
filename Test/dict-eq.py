a = {'a': 1, 'b': 2}
b = {'b': 2, 'a': 1}
c = {'a': 1, 'b': 2, 'c': 3}

print(a == b)
print(a == c)
print(b == c)

l = [a, b, c]
d = {'a': 1, 'b': 2}
print(d in l)
