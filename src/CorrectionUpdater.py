import os

def update(fixmap: dict):
    """
    @param: fixmap - dictionary mapping old key to a new key list|str
                     in the event that a list is supplied as a key the first element
                     in the list will recieve any existing key code. In the event that
                     the key is a string, the case will simply be replaced with the new 
                     string.
    @return: None
    """

    os.chdir('Corrections')
    files = list(filter(lambda x: x not in ['__pycache__', '__init__.py'], os.listdir()))
    
    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()

        # chunk file into sections
        sections = []
        start = 0
        for i in range(len(data)):
            if data[i].startswith("\t\t\t\tcase ") or data[i] == "\t\treturn result\n":
                sections.append((start, i))
                start = i
        sections.append((start, len(data)))
        
        # begin assembing updated file
        newData = data[sections[0][0]:sections[0][1]]

        for i in range(1, len(sections)):
            header = data[sections[i][0]]
            fixes = fixmap.get(header, None)

            if fixes is None:
                newData += data[sections[i][0]:sections[i][1]]
            elif type(fixes) is str: # fix is a stingle string
                newData += [fixes]
                newData += data[sections[i+1][0]:sections[i][1]]
            else: # fixes is a list of fixes
                newData += [fixes[0]]
                newData += data[sections[i+1][0]:sections[i][1]]

                for j in range(1, len(fixes)):
                    newData += [
                        "\t\t\t\tcase \"" + fixes[j] + "\":\n",
                        "\t\t\t\t\tpass #Implement this if necessary\n"
                    ]

        with open('../../Temp/'+file, 'w') as f: #! move from temp once verified this actually works
            f.writelines(newData)



if __name__ == "__main__":
    # DEFINE FIX HERE
    fix = {}

    update(fix)