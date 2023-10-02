# switcher = {
#     'a': 'A'
# }

# print(switcher.get('a'))
# print(switcher.get('b'))

def default(x):
    return x

switch = {
    'odd': lambda x: 3*x+1,
    'even': lambda x: x/2
}

x = 5

while x != 1:
    print(x)
    if x%2 == 0:
        x = int(switch.get('even')(x))
    else:
        x = int(switch.get('odd')(x))

print(x)
