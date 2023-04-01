def model(data: list[str]):
    corrections = {
        "Hummer Ev": "Hummer EV"
   }
    
    special_corrections = ["Canyon 2022", "Sierra 2500hd 3500hd", "Yukon Yukon Xl"]

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

            elif temp[idx] == special_corrections[1]:
                if "sierra-3500hd_" in temp[u]:
                    temp[idx] = "Sierra 3500HD"
                elif "sierra-2500hd_" in temp[u]:
                    temp[idx] = "Sierra 2500HD"

            elif temp[idx] == special_corrections[2]:
                if "yukon_" in temp[u]:
                    temp[idx] = "Yukon"
                elif "yukon-xl_" in temp[u]:
                    temp[idx] = "Yukon XL"
            
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
