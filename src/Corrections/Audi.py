def model(data: list[str]):
    corrections = {
        "A3 Sportback E Tron": "A3 Sportback e-tron",
        "A6 Allroad": "A6 Allroad Quattro",
        "E Tron Gt": "e-tron GT",
        "Q4 E Tron": "Q4 e-tron",
        "Q8 E Tron": "Q8 e-tron",
        "Rs Q8": "RSQ8",
        "Rs3": "RS3",
        "Rs4": "RS4",
        "Rs5": "RS5",
        "Rs5 Sportback": "RS5 Sportback",
        "Rs6 Avant": "RS6 Avant",
        "Rs7": "RS7", 
        "Sq5": "SQ5",
        "Sq7": "SQ7",
        "Sq8": "SQ8",
        "Tt Rs": "TT RS",
   }
    
    special_corrections = ["Tt Tts"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if '-tt-' in temp[u]:
                temp[idx] = 'TT'
            elif '-tts-' in temp[u]:
                temp[idx] = 'TTS'
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
