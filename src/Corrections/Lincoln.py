def model(data: list[str]):
    corrections = {
        "Mkc": "MKC",
        "Mks": "MKS",
        "Mkt": "MKT",
        "Mkz": "MKZ",
    }

    special_corrections = ["Mkx 2017"]

    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            temp[idx] = "MKX"
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

