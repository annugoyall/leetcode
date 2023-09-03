class Solution:
    def minimumOperations(self, num: str) -> int:
        count = 0

        n = len(num)
        index_5 = -1
        index_0 = -1

        for i in range(n-1, -1, -1):
            if num[i] == '5' and index_5 == -1:
                index_5 = i
            if num[i] == '0' and index_0 == -1:
                index_0 = i
            if index_5 != -1 and index_0 != -1:
                break

        ans = n
        found = False
        if index_5 != -1:
            ans1 = n - index_5 - 1
            index = -1
            for i in range(index_5-1, -1, -1):
                if num[i] in {'2', '7'}:
                    index = i
                    break
            if index != -1:
                found = True
                ans1 += (index_5 - index - 1)
            
            ans = min(ans, ans1)

        if index_0 != -1:
            ans2 = n - index_0 - 1
            index = -1
            for i in range(index_0-1, -1, -1):
                if num[i] in {'0', '5'}:
                    index = i
                    break
            if index != -1:
                found = True
                ans2 += (index_0 - index - 1)
                ans = min(ans, ans2)
        
        if not found:
            if index_0 != -1:
                ans = n - 1
            else:
                ans = n
        
        return ans
