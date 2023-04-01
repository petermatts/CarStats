def model(data: list[str]):
    corrections = {
        "C Max": "C-Max",
        "Ecosport": "EcoSport",
        "F 150": "F-150",
        "F 150 Lightning": "F-150 Lightning",
        "F 150 Raptor": "F-150 Raptor",
        "Fiesta St": "Fiesta ST",
        "Focus Rs": "Focus RS",
        "Focus St": "Focus ST",
        "Mustang Shelby Gt500": "Mustang Shelby GT500",
        "": "",
    }
    
    special_corrections = ["E Transit 2022, Super Duty 2022", "Mustang Shelby Gt350 Gt350r"]

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
                temp[idx] = "E-Transit"
            elif temp[idx] == special_corrections[1]:
                temp[idx] = temp[idx][:-5]

            if temp[idx] == special_corrections[2]:
                if 'GT350R' in temp[t]:
                    temp[idx] = "Mustang Shelby GT350R"
                else:
                    temp[idx] = "Mustang Shelby GT350"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
