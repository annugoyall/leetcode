class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        groups = [[i, groupSizes[i]] for i in range(n)]
        groups.sort(key = lambda x : x[1])

        ans = [[groups[0][0]]]
        items = 1
        curr_size = groups[0][1]
        for i in range(1, n):
            if len(ans[-1]) != curr_size:
                ans[-1].append(groups[i][0])
            else:
                ans.append([groups[i][0]])
                curr_size = groups[i][1]
        return ans