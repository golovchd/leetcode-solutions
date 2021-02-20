class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 < l2:
            return self._intersect(nums1, nums2)
        return self._intersect(nums2, nums1)


    def _intersect(self, small: List[int], large: List[int]) -> List[int]:
        small.sort()
        result = []
        e = len(small) - 1
        for n in large:
            if e > 0:
                p = self.b_search(n, small, 0, e)
                if p != -1:
                    result.append(small.pop(p))
                    e -= 1
                if e < 0:
                    return result
            else:
                if small[0] == n:
                    result.append(n)
                    return result
        return result


    def b_search(seld, value: int, nums: List[int], s: int, e: int) -> int:
        while s <= e:
            m = (s + e) // 2
            if value == nums[m]:
                return m
            if value < nums[m]:
                e = m - 1
            else:
                s = m + 1
        return -1
