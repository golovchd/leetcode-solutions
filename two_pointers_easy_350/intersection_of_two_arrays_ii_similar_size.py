class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        result = []
        while i < l1 and j < l2:
            # Skip first less then second 
            while i < l1 and nums1[i] < nums2[j]:
                i += 1
            if i == l1:
                break
            # Add matching to result
            while i < l1 and j < l2 and nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            if i == l1 or j == l2:
                break
            # Skip second less then first
            while j < l2 and nums2[j] < nums1[i]:
                j += 1
        return result            
