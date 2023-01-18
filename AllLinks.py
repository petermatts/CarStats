import os

if __name__ == '__main__':
    L = []
    os.chdir('Links')
    for x in os.listdir():
        if os.path.isdir(x):
            os.chdir(x)

            f = open("SUMMARY.txt", "r")
            L += f.readlines()
            f.close()

            os.chdir('../')
    os.chdir('../')

    file = open("AllLinks.txt", "w")
    file.writelines(L)
    file.close()