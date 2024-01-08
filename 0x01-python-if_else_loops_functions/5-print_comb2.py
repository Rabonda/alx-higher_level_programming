#!/usr/bin/python3
for indx in range(100):
    if indx == 99:
        pass
    else:
        print('{:02d}'.format(indx), end=", ")
print(indx)
