class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result:list[list[int]] = []
        for cur in people:
            result.insert(cur[1], cur)
        return result
