def model(data: list[str]):
    corrections = {
        "4runner": "4Runner",
        "Bz4x": "bZ4X",
        "C Hr": "C-HR",
        "Gr 86": "GR86",
        "Rav4": "RAV4",
        "Rav4 Hybrid": "RAV4 Hybrid",
        "Yaris Ia": "Yaris IA"
    }

    special_corrections = ["Prius Prime 2022"]

    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            temp[idx] = temp[idx][:-5]
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

