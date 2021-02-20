class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        s = 0
        e = len(people) - 1
        boats = 0
        while s < e:
            boats += 1
            if people[s] + people[e] <= limit:
                s += 1
                e -= 1
            else:
                e -= 1
        if s == e:
            boats += 1
        return boats
