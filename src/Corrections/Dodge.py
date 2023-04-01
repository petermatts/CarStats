def model(data: list[str]):
    corrections = {
        "Challenger Srt Demon": "Challenger SRT Demon",
        "Challenger Srt Srt Hellcat": "Challenger SRT Hellcat",
        "Charger Srt Hellcat": "Charger SRT Hellcat",
        "Durango Srt": "Durango SRT",
        "Durango Srt Hellcat": "Durango SRT Hellcat"
    }

    special_corrections = ["Charger 2023"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if temp[idx] == special_corrections[0]:
                temp[idx] = temp[idx][:-5]
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

