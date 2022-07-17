def big_endian(arr, start, end):
    root = start
    child = root << 1 + 1
    while child <= end:
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
            child = root << 1 + 1
        else:
            break


def heap_sort(arr):
    """
    堆排序

    :param arr:
    :return:
    """
    first = len(arr) >> 1 - 1
    for start in range(first, -1, -1):
        big_endian(arr, start, len(arr) - 1)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        big_endian(arr, 0, end - 1)
    return arr
