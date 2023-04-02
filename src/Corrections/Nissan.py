def model(data: list[str]):
    corrections = {
        "Gt R": "GT-R",
        "Nv200": "NV200",
        "Sentra Nismo": "Sentra NISMO",
        "Titan Xd": "Titan XD"
   }
    
    special_corrections = ["Juke Nismo Nismo Rs", "Nv1500 2500"]

    t = data[0].split(',').index('Trim')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if temp[idx] == special_corrections[0]:
                if "NISMO RS NISMO RS" in temp[t]:
                    temp[idx] = "Juke NISMO RS"
                else:
                    temp[idx] = "Juke NISMO"
            elif temp[idx] == special_corrections[1]:
                if "3500" in temp[t]:
                    temp[idx] = "NV3500"
                elif "2500" in temp[t]:
                    temp[idx] = "NV2500"
                elif "1500" in temp[t]:
                    temp[idx] = "NV1500"
            
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
