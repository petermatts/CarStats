def model(data: list[str]):
    corrections = {
        "Cooper Clubman Jcw": "Cooper Clubman JCW",
        "Cooper Countryman Jcw": "Cooper Countryman JCW",
        "Cooper Coupe S Jcw": "Cooper Coupe S JCW",
        "Cooper Jcw": "Cooper JCW",
        "Cooper Paceman S Jcw": "Cooper Paceman S JCW",
        "Cooper Roadster S Jcw": "Cooper Roadster S JCW"
    }

    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

