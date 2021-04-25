class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generate(nums: List[int]) -> List[List[int]]:
            if not nums:
                return []
            if len(nums) == 1:
                return [nums]
            ret = []
            test = set([])
            processed = set([])
            for i, num in enumerate(nums):
                if num in processed:
                    continue
                processed.add(num)
                for tail in generate(nums[:i] + nums[i + 1:]):
                    tmp = str([num] + tail)
                    if tmp not in test:
                        ret.append([num] + tail)
                        test.add(tmp)
            return ret
        
        return generate(nums)
