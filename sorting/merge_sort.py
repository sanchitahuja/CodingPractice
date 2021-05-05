def merge(arr1, arr2):
    i = 0
    j = 0
    final_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final_arr.append(arr1[i])
            i += 1

        else:
            final_arr.append(arr2[j])
            j += 1

    while j < len(arr2):
        final_arr.append(arr2[j])
        j += 1

    while i < len(arr1):
        final_arr.append(arr1[i])
        i += 1

    return final_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    print('mid', mid, )
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


print(merge_sort([4, 2]))
