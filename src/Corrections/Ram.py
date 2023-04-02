def model(data: list[str]):
    corrections = {
        "1500 Trx": "1500 TRX"
   }
    
    special_corrections = ["2500 3500"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if "ram-2500" in temp[u]:
                temp[idx] = "2500"
            elif "ram-3500" in temp[u]:
                temp[idx] = "3500"
                
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
