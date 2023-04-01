def model(data: list[str]):
    corrections = {
        "I3": "i3",
        "I4": "i4",
        "I7": "i7",
        "I8": "i8",
        "Ix": "iX",
        "Xm": "XM"
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

def trim(data: list[str]):
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if "XDrive" in temp[idx]:
            temp[idx] = temp[idx].replace("XDrive", "xDrive")
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines


def all(data: list[str]):
    data = model(data)
    data = trim(data)
    return data

