class Solution:
    def countOrders(self, n: int) -> int:

        dp = [-1 for i in range(n+1)]
        mod = 10**9 + 7

        def helper(n):
            if n == 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = (helper(n-1) * (2*n - 1)*n)%mod
            return dp[n]
        
        return helper(n)