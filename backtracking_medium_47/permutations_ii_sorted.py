import random
import sys
from typing import List
from typing import Dict


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

_UNIQUE_DEFAULT = 10
_COUNT = 10

if __name__ == '__main__':
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    else:
        count = _COUNT
    if len(sys.argv) > 2:
        unique_count = min(int(sys.argv[2]), count)
    else:
        unique_count = min(_COUNT, count)

    if count <= unique_count:
        nums = random.sample(range(1, unique_count + 1), count)
    else:
        nums = random.choices(range(1, unique_count + 1), k=count)
    result = Solution().permuteUnique(nums)
    print('Result count:', len(result), f' Total size or result from {nums} in bytes is ', sys.getsizeof(result))
    total_gb = sys.getsizeof(result) * sys.getsizeof(result[0]) / (8 * 1024 * 1024 * 1024)
    print(f'Size of each premutation is about ', sys.getsizeof(result[0]), ' total mem usage in GB: ', total_gb)
