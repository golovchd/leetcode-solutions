class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], x[1]))
        l = len(people)
        result = [None] * l
        for cur in people:
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
