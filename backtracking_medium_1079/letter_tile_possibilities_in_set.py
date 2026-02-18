class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """Use set, recursion on new symbol."""
        def generate(tiles: str, length: int) -> Set[str]:
            if length == 0:
                return set([])
            ret = set([])
            processed = set([])
            for i, symbol in enumerate(tiles):
                if length > 1:
                    if symbol in processed:
                        continue
                    processed.add(symbol)
                    for tail in generate(tiles[:i] + tiles[i+1:], length - 1):
                        ret.add(symbol + tail)
                else:
                    ret.add(symbol)
            return ret

        count = 0
        for i in range(len(tiles)):
            count += len(generate(tiles, i + 1))
        return count
