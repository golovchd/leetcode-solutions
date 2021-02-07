class Solution:
    # Submition https://leetcode.com/submissions/detail/449800704/
    # Runtime: 32 ms, faster than 63.19% of Python3 online submissions for Count of Matches in Tournament.
    # Memory Usage: 14 MB, less than 90.83% of Python3 online submissions for Count of Matches in Tournament.
    # Time O(log(n)), Memory O(1)
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n > 1:
            m += n // 2
            n = n // 2 + n % 2
        return m
