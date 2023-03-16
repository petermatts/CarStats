# Corrections for typos/misprints in CSVs

# import sys
import os

### General CSV corrections ###


#
# NOTE: Done, Do not use anymore
# 
def fix_width_issue():
    os.chdir('../Data')
    for d in os.listdir():
        if os.path.isdir(d):
            os.chdir(d)
            print(os.getcwd())
            for y in os.listdir():
                if os.path.isdir(y):
                    os.chdir(y)

                    for f in os.listdir():
                        file = open(f, 'r')
                        lines = file.readlines()
                        file.close() 
                        idx = lines[0].split(",").index("Width")

                        lines[0] = lines[0].replace("Width, no mirrors (in)", "Width no mirrors (in)") # retroactively fix headers

                        for l in range(1, len(lines)):
                            csep = lines[l].split(",") # means comma separated
                            temp = csep[:idx] + csep[idx+1:]
                            lines[l] = ",".join(temp)

                        file = open(f, 'w')
                        file.writelines(lines)
                        file.close()

                    os.chdir('../')
            os.chdir('../')


if __name__ == '__main__':
    # fix_width_issue()
    pass
