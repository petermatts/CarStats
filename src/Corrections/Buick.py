def model(data: list[str]):
    corrections = {
        "Encore Gx": "Encore GX",
        "Regal Gs": "Regal GS",
        "Regal Tourx": "Regal TourX",
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

