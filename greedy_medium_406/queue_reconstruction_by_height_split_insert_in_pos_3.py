class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        heights: dict[int,list[list[int]]] = {}
        for p in people:
            if p[0] in heights:
                heights[p[0]].append(p)
            else:
                heights[p[0]] = [p]
        for h in heights:
            heights[h].sort(key=lambda x: x[1])
        heights_queue = list(heights.keys())
        heights_queue.sort()
        l = len(people)
        result: list[list[int]] = [[]] * l
        for height in heights_queue:
            for cur in heights[height]:
                c = 0
                for i in range(l):
                    if not result[i]:
                        if c == cur[1]:
                            result[i] = cur
                            break
                        else:
                            c += 1
                    elif result[i][0] == cur[0]:
                        c += 1
        return result
