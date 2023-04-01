def model(data: list[str]):
    corrections = {
        "E Pace": "E-Pace",
        "F Pace": "F-Pace",
        "F Pace Svr": "F-Pace SVR",
        "F Type": "F-Type",
        "I Pace": "I-Pace",
        "Xe": "XE",
        "Xf": "XF",
        "Xf Sportbrake": "XF Sportbrake",
        "Xj": "XJ",
        "Xjr575": "XJR575",
        "Xk": "XK"
    }

    special_corrections = ["Xkr Xkr S"]

    hp = data[0].split(',').index('Max Horsepower')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if temp[hp] == "550":
                temp[idx] = "XKR-S"
            elif temp[hp] == "510":
                temp[idx] = "XKR"
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

