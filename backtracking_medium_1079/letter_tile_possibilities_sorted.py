class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """Use sort, recursion on new symbol."""
        def generate(tiles: str, length: int) -> int:
            count = 0
            for i, symbol in enumerate(tiles):
                if i and tiles[i - 1] == symbol:
                    continue
                if length > 1:
                    count += generate(tiles[:i] + tiles[i+1:], length - 1)
                else:
                    count += 1
            return count

        count = 0
        tiles = ''.join(sorted(tiles))
        for i in range(len(tiles)):
            count += generate(tiles, i + 1)
        return count
