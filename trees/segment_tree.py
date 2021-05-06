class SegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.segment_tree = [0] * 4 * len(arr)

    def func(self, x, y):
        return x + y

    def create_tree(self):
        self.create_tree_util(0, len(self.arr) - 1, 0)

    def create_tree_util(self, i, j, curr):
        if i == j:
            self.segment_tree[curr] = self.arr[i]
        else:
            mid = (i + j) // 2
            self.create_tree_util(i, mid, 2 * curr + 1)
            self.create_tree_util(mid + 1, j, 2 * curr + 2)
            self.segment_tree[curr] = self.func(self.segment_tree[2 * curr + 1], self.segment_tree[2 * curr + 2])

    def find_range_util(self, query_start, query_end, start, end, curr):
        if query_start <= start and end <= query_end:
            return self.segment_tree[curr]
        elif end < query_start or start > query_end:
            return 0  # For sum 0 for product 1
        else:
            mid = (start + end) // 2
            return self.func(self.find_range_util(query_start=query_start, query_end=query_end, start=start, end=mid,
                                                  curr=2 * curr + 1),
                             self.find_range_util(query_start=query_start, query_end=query_end, start=mid + 1, end=end,
                                                  curr=2 * curr + 2)
                             )

    def find_range_val(self, query_start, query_end):
        if query_start < 0 and query_end >= len(self.arr):
            return -1
        else:
            return self.find_range_util(query_start=query_start, query_end=query_end, start=0, end=len(self.arr) - 1,
                                        curr=0)


s = SegmentTree([1, 12, 3, 4])
s.create_tree()
print(s.segment_tree)
print(s.find_range_val(1,1))
