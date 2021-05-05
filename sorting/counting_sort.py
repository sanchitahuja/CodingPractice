def counting_sort(arr):
    max_element = max(arr)
    min_element = min(arr)
    l = max_element - min_element + 1
    count = [0 for _ in range(l)]
    output = [0 for _ in range(len(arr))]

    for i in arr:
        count[i - min_element] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[arr[i] - min_element] - 1] = arr[i]
        count[arr[i] - min_element] -= 1

    return output


arr = [2, 3, 1, 6, 0]
print(counting_sort(arr))
