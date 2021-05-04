import bisect


# Returns index and element
def binary_search(arr, element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        print('low', low, 'high', high, 'mid', mid)
        if arr[mid] == element:
            return mid, arr[mid]
        elif element > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1, None


print(binary_search([2, 3, 4, 5, 7], 7))
