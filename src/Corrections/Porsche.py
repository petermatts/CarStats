def model(data: list[str]):
    corrections = {
        "911 Gt2 Rs": "911 Gt2 Rs",
        "Macan Gts": "Macan Gts"
   }
    
    special_corrections = [
        "911 Gt3 Gt3 Rs",
        "911 Turbo Turbo S",
        "Cayenne Coupe Turbo Turbo S",
        "Cayenne Turbo Turbo S",
        "Panamera Turbo Turbo S"
    ]

    u = data[0].split(',').index('URL')
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
                if "porsche-911-gt3-rs_" in temp[u]:
                    temp[idx] = "911 GT3 RS"
                else:
                    temp[idx] = "911 GT3"
            elif temp[idx] == special_corrections[1]:
                if temp[t] == "Cabriolet" or temp[t] == "Coupe":
                    temp[idx] = "911 Turbo"
                else:
                    temp[idx] = "911 Turbo S"
            elif temp[idx] == special_corrections[2]:
                if "porsche-cayenne-coupe-turbo-gt_" in temp[u]:
                    temp[idx] = "Cayenne Coupe Turbo GT"
                elif "porsche-cayenne-coupe-turbo-s-e-hybrid_" in temp[u]:
                    temp[idx] = "Cayenne Coupe Turbo S"
                elif "porsche-cayenne-coupe-turbo_" in temp[u]:
                    temp[idx] = "Cayenne Coupe Turbo"
            elif temp[idx] == special_corrections[3]:
                if "porsche-cayenne-turbo-s-e-hybrid_" in temp[u]:
                    temp[idx] = "Cayenne Turbo S"
                else:
                    temp[idx] = "Cayenne Turbo"
            elif temp[idx] == special_corrections[4]:
                if "porsche-panamera-turbo_" in temp[u]:
                    temp[idx] = "Panamera Turbo"
                else:
                    temp[idx] = "Panamera Turbo S"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
