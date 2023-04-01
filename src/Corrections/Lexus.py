def model(data: list[str]):
    corrections = {
        "Ct": "CT",
        "Es": "ES",
        "Gs": "GS",
        "Gs F": "GS F",
        "Gx": "GX",
        "Hs": "HS",
        "Is": "IS",
        "Is F": "IS F",
        "Lc": "LC",
        "Lfa": "LFA",
        "Ls": "LS",
        "Lx": "LX",
        "Nx": "NX",
        "Rc": "RC",
        "Rc F": "RC F",
        "Rx": "RX",
        "Rz": "RZ",
        "Sc": "SC",
        "Ux": "UX"
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

