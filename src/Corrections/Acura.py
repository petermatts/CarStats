def model(data: list[str]):
    corrections = {
        "Ilx": "ILX",
        "Mdx": "MDX",
        "Nsx": "NSX",
        "Rdx": "RDX",
        "Rl": "RL",
        "Rlx": "RLX",
        "Tl": "TL",
        "Tlx": "TLX",
        "Tsx": "TSX",
        "Zdx": "ZDX",
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

