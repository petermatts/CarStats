def model(data: list[str]):
    corrections = {
        "Cls63 S 4matic": "CLS63 S",
        "Eqe53": "EQE53",
        "Eqs53": "EQS53",
        "Gl63": "GL63",
        "Glb35": "GLB35",
        "Gls63 4matic": "GLS63",
        "Slc43": "SLC43",
        "Slk55": "SLK55"
   }
    
    special_corrections = [
        "Cla35 Cla45",
        "Gla35 Gla45",
        "Glc43 4matic Glc63 4matic",
        "Glc43 Coupe Glc63 Coupe",
        "Gle43 Coupe 4matic Gle63 S Coupe 4matic",
        "Gle53 4matic Gle63 4matic",
        "Gt Gt S Gt C Gt R",
        "Gt43 Gt53 Gt63",
        "Sl55 Sl63"
    ]

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
                if "mercedes-amg-cla35-4matic_" in temp[u]:
                    temp[idx] = "CLA35"
                else:
                    temp[idx] = "CLA45"
            elif temp[idx] == special_corrections[1]:
                if "mercedes-amg-gla35_" in temp[u]:
                    temp[idx] = "GLA35"
                else:
                    temp[idx] = "GLA45"
            elif temp[idx] == special_corrections[2]:
                if "mercedes-amg-glc43-4matic_" in temp[u]:
                    temp[idx] = "GLC43"
                else:
                    temp[idx] = "GLC63"
            elif temp[idx] == special_corrections[3]:
                if "mercedes-amg-glc43-coupe-4matic_" in temp[u]:
                    temp[idx] = "GLC43 Coupe"
                else:
                    temp[idx] = "GLC63 Coupe"
            elif temp[idx] == special_corrections[4]:
                if "mercedes-amg-gle43-coupe-4matic_" in temp[u]:
                    temp[idx] = "GLE43 Coupe"
                else:
                    temp[idx] = "GLE63 S Coupe"
            elif temp[idx] == special_corrections[5]:
                if "mercedes-amg-gle63-s-4matic-coupe_" in temp[u]:
                    temp[idx] = "GLE63 S"
                else:
                    temp[idx] = "GLE53"
            elif temp[idx] == special_corrections[6]:
                if "mercedes-amg-gt-c-coupe_" in temp[u] or "mercedes-amg-gt-c-roadster_" in temp[u]:
                    temp[idx] = "GT C"
                elif "mercedes-amg-gt-r-coupe_" in temp[u]:
                    temp[idx] = "GT R"
                elif "mercedes-amg-gt-s-coupe_" in temp[u]:
                    temp[idx] = "GT S"
                else:
                    temp[idx] = "GT"
            elif temp[idx] == special_corrections[7]:
                if "mercedes-amg-gt43_" in temp[u]:
                    temp[idx] = "GT43"
                elif "mercedes-amg-gt53_" in temp[u]:
                    temp[idx] = "GT53"
                else:
                    temp[idx] = "GT63"
            elif temp[idx] == special_corrections[8]:
                if "mercedes-amg-sl63_" in temp[u]:
                    temp[idx] = "SL63"
                elif "mercedes-amg-sl53_" in temp[u]:
                    temp[idx] = "SL53"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
