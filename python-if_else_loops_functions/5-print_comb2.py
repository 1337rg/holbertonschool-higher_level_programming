#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print('{:02}'.format(i))
        continue
    print('{:02}, '.format(i), end="")
