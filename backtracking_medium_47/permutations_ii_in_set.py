class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def generate(nums: list[int]) -> list[list[int]]:
            if not nums:
                return []
            if len(nums) == 1:
                return [nums]
            ret = []
            test = set()
            processed = set()
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
