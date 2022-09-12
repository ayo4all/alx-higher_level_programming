#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(x):
        try:
            item = my_list[y]
            print("{}".format(item), end="")
            count = count + 1
        except IndexError:
            pass
    print()
    return count