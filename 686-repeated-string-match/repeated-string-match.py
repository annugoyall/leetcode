class Solution:
    def findHash(self, string):
        val = 0
        places = len(string) - 1
        for i in string:
            val += (ord(i) * (10**places))
            places -= 1
        return val

    def haspattern(self, a, b):
        hash_b = self.findHash(b)
        left = 0
        right = len(b)
        hash_a = self.findHash(a[:right])

        if hash_a == hash_b:
            return True
        
        while right != len(a):
            hash_a -= (ord(a[left])*(10**(len(b)-1)))
            hash_a *= 10
            hash_a += ord(a[right])
            left += 1
            right += 1
            if hash_a == hash_b:
                return True
        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        new = a

        while len(new) < len(b):
            new += a
            count += 1
        if self.haspattern(new, b):
            return count
        elif self.haspattern(new+a, b):
            return count + 1
        else:
            return -1