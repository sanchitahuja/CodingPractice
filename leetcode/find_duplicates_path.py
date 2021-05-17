from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            p = path.split()
            p_name = p[0]
            for f in p[1:]:
                name, content = '', ''
                i = 0
                while f[i] != '(' and i<len(f):
                    name += f[i]
                    i += 1
                i += 1
                while f[i] != ')' and i<len(f):
                    content += f[i]
                    i += 1
                # print('name', name, 'content', content)
                d[content].append(f'{p_name}/{name}')

        # print('d', d)
        final_list = []
        for val in d.values():
            if len(val) > 1:
                # print('val',val)
                final_list.append(val)
        return final_list


print(Solution().findDuplicate(
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
