#!/usr/bin/python3.4
def hidden_discovery():
    hide = dir(hidden_4)
    for indx in hide:
        if(indx[ :2] != "__"):
            print(indx)


if __name__ == "__main__":
    import hidden_4
    hidden_discovery()
