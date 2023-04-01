def model(data: list[str]):
    corrections = {
        "Bolt Euv": "Bolt EUV",
        "Bolt Ev": "Bolt EV",
        "Camaro Z 28": "Camaro Z/28",
        "Camaro Zl1": "Camaro ZL1",
        "Corvette Zr1": "Corvette ZR1",
        "Hhr": "HHR",
        "Spark Ev": "Spark EV",
        "Ss": "SS",
        "Trailblazer": "Trailblazer"
    }

    special_corrections = ["Silverado 2500hd 3500hd", "Trax 2022"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if temp[idx] == special_corrections[1]:
                temp[idx] = temp[idx][:-5]

            if "silverado-3500hd_" in temp[u]:
                temp[idx] = "Silverado 3500HD"
            elif "silverado-2500hd_" in temp[u]:
                temp[idx] = "Silverado 2500HD"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

