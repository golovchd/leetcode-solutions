# One pass, O(1) memory solution
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_m = 0
        s = 0
        l = len(arr)
        while s + 2 < l:
            i = s + 1
            while i < l and arr[i - 1] < arr[i]:
                i += 1
            p = i - 1
            while i < l and arr[i - 1] > arr[i]:
                i += 1
            if s < p < i - 1:
                max_m = max(max_m, i - s)
            if i == s + 1:
                s = i
            else:
                s = i - 1
        return max_m
