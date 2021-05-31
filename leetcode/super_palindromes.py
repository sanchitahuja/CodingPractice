def reverse(x):
    ans = 0
    while x:
        ans = 10 * ans + x % 10
        x //= 10
    return ans


def is_palindrome(x):
    return x == reverse(x)


def generate_possible_palidromes(n):
    _list = []
    cur = 1
    i = 1
    # Even length palindromes
    even_list = []
    while cur < n:

        cur = int(str(i) + str(i)[::-1])
        if is_palindrome(cur ** 2):
            even_list.append(cur)
            even_list.append(cur ** 2)

        i += 1

    odd_list = []
    cur = 1
    i = 1
    while cur < n:

        cur = int(str(i) + str(i)[-2::-1])
        if is_palindrome(cur ** 2):
            odd_list.append(cur ** 2)

        i += 1

    print('odd_list', odd_list)
    print('even_list', even_list)
    l1 = 0
    l2 = 0
    while l1 < len(even_list) and l2 < len(odd_list):
        if even_list[l1] <= odd_list[l2]:
            _list.append(even_list[l1])
            l1 += 1
        else:
            _list.append(odd_list[l1])
            l2 += 1

    while l1 < len(even_list):
        _list.append(even_list[l1])
        l1 += 1

    while l2 < len(odd_list):
        _list.append(odd_list[l1])
        l2 += 1
    return _list


generate_possible_palidromes(100000)
