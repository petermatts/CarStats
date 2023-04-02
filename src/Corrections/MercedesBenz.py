def model(data: list[str]):
    corrections = {
        "Cl Class": "CL Class",
        "Cla Class": "CLA Class",
        "Clk Class": "CLK Class",
        "Cls Class": "CLS Class",
        "Eqb": "EQB",
        "Eqe": "EQE",
        "Eqs": "EQS",
        "Gla Class": "GLA Class",
        "Glb Class": "GLB Class",
        "Glc Class": "GLC Class",
        "Glc Coupe": "GLC Coupe",
        "Gle Class": "GLE Class",
        "Glk Class": "GLK Class",
        "Gls Class": "GLS Class",
        "Ml63 Amg": "ML63 AMG",
        "Sl Class": "SL Class",
        "Slc Class": "SLc Class",
        "Slk Class": "SLK Class",
        "Slk55 Amg": "SLK55 AMG",
        "Slr Class": "SLR Class",
        "Sls Amg": "SLS AMG"
   }
    
    special_corrections = [
        "Cl63 Cl65 Amg",
        "G63 G65 Amg",
        "S63 S65 Amg"
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
                if "mercedes-benz-cl65-amg_" in temp[u]:
                    temp[idx] = "CL65 AMG"
                elif "mercedes-benz-cl63-amg_" in temp[u]:
                    temp[idx] = "CL63 AMG"
            elif temp[idx] == special_corrections[1]:
                if "mercedes-benz-g65-amg_" in temp[u]:
                    temp[idx] = "G65 AMG"
                elif "mercedes-benz-g63-amg_" in temp[u]:
                    temp[idx] = "G63 AMG"
            elif temp[idx] == special_corrections[2]:
                if "mercedes-benz-s65-amg_" in temp[u]:
                    temp[idx] = "S65 AMG"
                elif "mercedes-benz-s63-amg_" in temp[u]:
                    temp[idx] = "S63 AMG"

            Lines.append(",".join(temp))
        else:
            Lines.append(data[i])

    return Lines
        

def all(data: list[str]):
    data = model(data)
    return data
