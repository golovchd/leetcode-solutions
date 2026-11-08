class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (x[0], x[1]))
        l = len(people)
        result:list[list[int]] = [[]] * l
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
