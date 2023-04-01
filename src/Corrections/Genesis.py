def model(data: list[str]):
    corrections = {
        "Electrified Gv70": "Electrified GV70",
        "Gv60": "GV60",
        "Gv70": "GV70",
        "Gv80": "GV80"
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

