import random
random_numbers = list(range(1, 11))
random.shuffle(random_numbers)


def selection_sort(unsorted_list: list):
    for i in range(0, len(unsorted_list) - 1):
        min_num = i
        for k in range(i + 1, len(unsorted_list)):
            if unsorted_list[k] < unsorted_list[min_num]:
                min_num = k
        unsorted_list[i], unsorted_list[min_num] = unsorted_list[min_num], unsorted_list[i]


selection_sort(random_numbers)
print(random_numbers)


def binary_search(val, a):
    n = len(a)
    result_ok = False
    first = 0
    last = n - 1
    while first < last:
        middle = (first + last) // 2
        if val == a[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        else:
            if val > a[middle]:
                first = middle + 1
            else:
                last = middle - 1
    else:
        if result_ok:
            print(f'Element is found at index {pos}.')
        else:
            print('Element is not found.')


binary_search(5, random_numbers)
