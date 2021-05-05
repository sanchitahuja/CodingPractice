# Min Heap
def heapify(arr, i, n):
    print('i', i ,'n', n)
    if i >= n:
        return

    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest, n)


def heap_sort(arr):
    n = len(arr)
    # Build Min Heap
    for i in range(n // 2 , -1, -1):
        heapify(arr, i, n)

    print('Arr', arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr


print(heap_sort(arr=[2, 3, 1, 6, 0]))
