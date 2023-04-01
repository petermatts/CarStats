def model(data: list[str]):
    corrections = {
        "Cr V": "CR-V",
        "Cr Z": "CR-Z",
        "Fit Ev": "Fit EV",
        "Hr V": "HR-V",
   }
    
    special_corrections = ["Civic 2023"]

    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            temp[idx] = temp[idx][:-5]
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
