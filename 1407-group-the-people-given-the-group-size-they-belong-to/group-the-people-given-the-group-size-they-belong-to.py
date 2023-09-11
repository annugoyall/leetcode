class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        d = dict()
        ans = []
        for i in range(n):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = [i]
            else:
                if len(d[groupSizes[i]]) == groupSizes[i]:
                    ans.append(d[groupSizes[i]])
                    d[groupSizes[i]] = [i]
                else:
                    d[groupSizes[i]].append(i)
        ans.extend(d.values())
        return ans