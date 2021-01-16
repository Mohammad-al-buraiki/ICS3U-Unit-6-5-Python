# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program uses a 2D array


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
    print("Enter 1 mark at a time. Enter -1 to end")
    while True:
        mark = input("Enter the mark: ")
        if mark != int(mark):
            if mark != "-1":
                mark_list.append(mark)
            else:
                average = average_percent(mark_list)
    
    print("The average is {0} %.".format(average))


if __name__ == "__main__":
    main()
