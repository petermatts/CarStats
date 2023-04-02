def model(data: list[str]):
    corrections = {
        "Gls600": "GLS600"
   }
    
    special_corrections = [
        "S580 S680"
    ]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if "mercedes-maybach-s580_" in temp[u]:
                temp[idx] = "S580"
            elif "mercedes-maybach-s680_" in temp[u]:
                temp[idx] = "S680"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
