def partition(arr, low, high):
    pivot = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    arr[high], arr[j] = arr[j], arr[high]
    return j


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, 0, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


arr = [2, 3, 1, 6, 0]
print(quick_sort(arr, 0, len(arr) - 1))
