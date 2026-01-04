import argparse

def run(args):
    print(dir(args))
    #note args is not subscriptable
    print("str   = " + str(args.str))
    print("bool  = " + str(args.bool))
    print("int   = " + str(args.int))
    print("float = " + str(args.float))
    print(vars(args))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #note there is a boolean required param which will be useful
    parser.add_argument('-s', '--str', type=str, help='test string variable')
    parser.add_argument('-b', '--bool', type=bool, help='test boolean variable')
    parser.add_argument('-i', '--int', type=int, help='test integer variable')
    parser.add_argument('-f', '--float', type=int, help='test float variable')


    args = parser.parse_args()
    run(args)
