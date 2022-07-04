def find_smallest(arr):
    """
    找出最小值
    :param arr:
    :return:
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    """
    选择排序

    :param arr:
    :return:
    """
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr
