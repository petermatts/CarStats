def model(data: list[str]):
    corrections = {
        "Ats": "ATS",
        "Ats V": "ATS V",
        "Ct4": "CT4",
        "Ct4 V Blackwing": "CT4 V Blackwing",
        "Ct5": "CT5",
        "Ct5 V Blackwing": "CT5 V Blackwing",
        "Ct6": "CT6",
        "Cts": "CTS",
        "Cts V": "CTS V",
        "Dts": "DTS",
        "Elr": "ELR",
        "Escalade Ext": "Escalade EXT",
        "Srx": "SRX",
        "Sts": "STS",
        "Xlr": "XLR",
        "Xt4": "XT4",
        "Xt5": "XT5",
        "Xt6": "XT6",
        "Xts": "XTS",
    }

    special_corrections = ["Escalade Escalade Esv"]

    u = data[0].split(',').index('URL')
    idx = data[0].split(',').index('Model')
    Lines = [data[0]]

    for i in range(1, len(data)):
        temp = data[i].split(',')
        if temp[idx] in corrections.keys():
            temp[idx] = corrections[temp[idx]]
            Lines.append(",".join(temp))
        elif temp[idx] in special_corrections:
            if "_cadillac-escalade-esv_" in temp[u]:
                temp[idx] = "Escalade ESV"
            elif "_cadillac-escalade_" in temp[u]:
                temp[idx] = "Escalade"
            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data

