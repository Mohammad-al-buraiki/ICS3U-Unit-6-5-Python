# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the average of the marks


def average_percent(mark_list):
    # calculation of the mark
    total = 0
    for loop_counter in range(len(mark_list)):
        number = mark_list[loop_counter]
        total += number

    multiply_value = 10 * len(mark_list)
    average = total / multiply_value
    average = average * 10

    return average


def main():
    # getting user input

    mark_list = []

    # input
    print("Enter 1 mark at a time 1 - 100. Enter -1 to end")
    while True:
        mark = int(input("Enter the mark: "))
        if mark > 100:
            print("Sorry that was a big integer")
        elif mark < -1:
            print("Sorry that was a small integer")
        elif mark == -1:
            average = average_percent(mark_list)
            print("")
            print("The average is {0: .1f} %.".format(average))
            break
        else:
            mark_list.append(mark)


if __name__ == "__main__":
    main()
