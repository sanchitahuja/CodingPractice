from typing import List


class Solution:
    def is_valid(self, st, decimal):
        if decimal  and st[-1] == '0':
            return False
        if len(st) != 1 and decimal != 1 and st[0] == '0':
            return False

        return True

    def ambiguousCoordinates(self, s: str) -> List[str]:
        final_list = []
        for i in range(2, len(s) - 1):
            first = str(s[1:i])
            second = str(s[i:-1])
            print('s', s)
            first_arr, second_arr = [], []
            for j in range(len(first)):
                if self.is_valid(first, j):
                    first_arr.append(f'{str(first[:j])}{"." if j != 0 else ""}{str(first[j:])}')
            for j in range(len(second)):
                if self.is_valid(second, j):
                    second_arr.append(f'{str(second[:j])}{"." if j != 0 else ""}{str(second[j:])}')

            for f in first_arr:
                for second in second_arr:
                    final_list.append(f'({f}, {second})')

        return final_list


fo = Solution().ambiguousCoordinates("(1111)")
print('f', fo)
