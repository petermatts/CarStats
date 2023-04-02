def model(data: list[str]):
    corrections = {
        "Xc40": "XC40",
        "Xc40 Recharge": "XC40 Recharge",
        "Xc60": "XC60",
        "Xc70": "XC70",
        "Xc90": "XC90",
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

