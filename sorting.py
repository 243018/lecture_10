import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """

    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        dictionary = {}
        for line in reader:
            for head, value in line.items():
                if head not in dictionary:
                    dictionary[head] = [int(value)]
                else:
                    dictionary[head].append(int(value))

    return dictionary


def selection_sort(array):
    """
    Selection sort algorithm implementation, sorts all elements in ascending order
    :param array: (list), of any length containing only integer values
    :return: (list), in ascending order
    """

    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def bubble_sort(array_2):
    """
    Bubble sort algorithm implementation
    :param array_2: (list), of any length containing only integer values
    :return: (list), in ascending order
    """

    n = len(array_2)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array_2[j] > array_2[j + 1]:
                array_2[j], array_2[j + 1] = array_2[j + 1], array_2[j]

    return array_2


def insertion_sort(array_3):
    """
    Insertion sort algorithm implementation
    :param array_3: (list), of any length containing only integer values
    :return: (list), in ascending order
    """

    for i in range(1, len(array_3)):
        key = array_3[i]
        j = i - 1
        while j >= 0 and key < array_3[j]:
            array_3[j + 1] = array_3[j]
            j -= 1
        array_3[j + 1] = key

    return array_3


def main():
    """
    Main program function, reads the .csv file and orders a list of integers under selected key in ascending order
    :return: sorted list using three different sorting algorithms
    """

    output = read_data("numbers.csv")
    print(output)
    print(selection_sort(output["series_1"]))
    print(bubble_sort(output["series_2"]))
    print(insertion_sort(output["series_3"]))


if __name__ == '__main__':
    main()
