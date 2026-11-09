import random
import sys


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """Frequency count solution."""
        def generate(num_freq: dict[int, int], todo_length: int, depth: int, result: list[list[int]], path: list[int]):
            if not todo_length:
                result.append(path[:])  # Copy path to result
                return

            for num in num_freq:
                if not num_freq[num]:
                    continue
                num_freq[num] -= 1
                path[depth] = num
                generate(num_freq, todo_length - 1, depth + 1, result, path)
                num_freq[num] += 1

        num_freq: dict[int,int] = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        result: list[list[int]] = []
        template = [0] * len(nums)
        generate(num_freq, len(nums), 0, result, template)
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
    print(f'Size of each permutation is about ', sys.getsizeof(result[0]), ' total mem usage in GB: ', total_gb)
