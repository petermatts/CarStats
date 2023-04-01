def model(data: list[str]):
    corrections = {
        "600lt": "600LT",
        "650s": "650S",
        "720s": "720S",
        "765lt": "765LT",
        "Mclaren Gt": "GT",
        "Mp4 12c": "MP4 12C"
    }

    special_corrections = ["570s 570gt"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        if temp[idx] in special_corrections:
            if "mclaren-570s_" in temp[u]:
                temp[idx] = "570S"
            else:
                temp[idx] = "570GT"
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

