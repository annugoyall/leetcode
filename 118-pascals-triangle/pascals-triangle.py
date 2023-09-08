class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        for i in range(numRows-1):
            new = [1]
            for j in range(i):
                new.append(ans[i][j]+ans[i][j+1])
            new.append(1)
            ans.append(new)
        return ans
        