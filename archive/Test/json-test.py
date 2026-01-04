import json

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
    # write obj1 to file
    # data = json.dumps([obj1], indent=4) #! IMPORTANT: instance must be a list
    # # print(data)
    # with open("json-test.json", "w") as outfile:
    #     outfile.write(data) 

    # get contents of file and append obj2
    with open("json-test.json", "r+") as file:
        contents = json.load(file)

        # data = json.dumps(obj2, indent=4) #! important
        contents.append(obj2)
        # print(contents)
        data = json.dumps(contents, indent=4)
        # print(data)

    with open("json-test.json", "w") as outfile:
        outfile.write(data)

