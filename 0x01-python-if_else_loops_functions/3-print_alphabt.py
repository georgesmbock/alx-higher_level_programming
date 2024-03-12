#!/usr/bin/python3
for l in range(97,123,1):
    if (l == 101 or l == 113):
        continue
    else:
        print("{}".format(chr(l)), end='')
