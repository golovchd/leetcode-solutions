class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heights = {}
        for p in people:
            if p[0] in heights:
                heights[p[0]].append(p)
            else:
                heights[p[0]] = [p]
        for h in heights:
            heights[h].sort(key=lambda x: x[1])
        heights_queue = list(heights.keys())
        heights_queue.sort(key=lambda x: -x)
        l = len(people)
        result = []
        for height in heights_queue:
            for cur in heights[height]:
                result.insert(cur[1], cur)
        return result
