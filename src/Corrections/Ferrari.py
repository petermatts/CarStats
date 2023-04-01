def model(data: list[str]):
    corrections = {
        "296 Gtb": "296 Gtb",
        "488": "488 Pista",
        "599gtb Fiorano": "599GTB Fiorano",
        "F8 Tributo Spider": "F8",
        "Ff": "FF",
        "Gtc4lusso": "GTC4Lusso",
        "Laferrari": "LaFerrari",
        "Sf90 Stradale": "SF90 Stradale"
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

