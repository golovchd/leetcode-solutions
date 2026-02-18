class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """Use frequency count."""
        def backtracking(frequencies: Dict[str, int]) -> int:
            count = 0
            for symbol in frequencies:
                if frequencies[symbol] > 0:
                    frequencies[symbol] -= 1
                    count += 1 + backtracking(frequencies)
                    frequencies[symbol] += 1
            return count

        frequencies = {}
        for symbol in tiles:
            if symbol in frequencies:
                frequencies[symbol] += 1
            else:
                frequencies[symbol] = 1
        return backtracking(frequencies)
