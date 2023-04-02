def model(data: list[str]):
    corrections = {
        "Fr S": "FR-S",
        "Ia": "iA",
        "Im": "iM",
        "Tc": "tC",
        "Xb": "xB",
        "Xd": "xD"
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

