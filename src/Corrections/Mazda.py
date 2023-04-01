def model(data: list[str]):
    corrections = {
        "B Series": "B-Series",
        "Cx 3": "CX 3",
        "Cx 30": "CX 30",
        "Cx 5": "CX 5",
        "Cx 50": "CX 50",
        "Cx 7": "CX 7",
        "Cx 9": "CX 9",
        "Mx 30": "MX 30",
        "Mx 5 Miata": "MX 5 Miata",
        "Rx 8": "RX 8"
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

