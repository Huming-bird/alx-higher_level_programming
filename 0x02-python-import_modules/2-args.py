#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = len(sys.argv)

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
        print(f"1: {sys.argv[0]}")
    else:
        print(f"{arg} arguments:")
        print("{}: {}".format((i for i in range(1,  arg+1)), sys.argv[i-1]))
