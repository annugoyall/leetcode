class Solution:
    def symmetric(self, num):
        num = str(num)
        if len(num) % 2:
            return False
        r_sum = 0
        l_sum = 0
        while num:
            r_sum += int(num[0])
            l_sum += int(num[-1])
            num = num[1:len(num)-1]
        return r_sum == l_sum
        
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high+1):
            if self.symmetric(i):
                count += 1
        
        return count