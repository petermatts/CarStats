import yaml

obj1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

obj2 = {
    'd': 4,
    'e': 5
}

if __name__ == '__main__':

    # writing
    # with open('yaml-python.yml', 'a') as file:
    #     # y = yaml.dump([obj1])
    #     y = yaml.dump([obj2])
    #     file.write(y)

    # reading
    data = None
    with open('yaml-python.yml', 'r') as file:
        data = yaml.safe_load(file)
    print(data)
        