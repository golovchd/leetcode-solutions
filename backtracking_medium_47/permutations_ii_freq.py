class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Frequency count solution."""
        def generate(num_freq: Dict[int, int], todo_length: int, depth: int, result: List[List[int]], path: List[int]):
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
        
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        result = []
        template = [0] * len(nums)
        generate(num_freq, len(nums), 0, result, template)
        return result
