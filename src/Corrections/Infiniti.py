def model(data: list[str]):
    corrections = {
        "Ex": "EX",
        "Jx": "JX",
        "Qx": "QX",
        "Qx30": "QX30",
        "Qx50": "QX50",
        "Qx60": "QX60",
        "Qx70": "QX70",
        "Qx80": "QX80"
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

