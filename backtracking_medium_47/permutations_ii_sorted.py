class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generate(nums: List[int], result, path):
            if len(nums) == 1:
                result.append(path + nums)
            else:
                for i, num in enumerate(nums):
                    if i and nums[i - 1] == num:
                        continue
                    generate(nums[:i] + nums[i + 1:], result, path + [num])
        
        result = []
        nums.sort()
        generate(nums, result, [])
        return result
