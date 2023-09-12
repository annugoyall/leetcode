from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        freq_arr = list(freq.values())
        freq_arr.sort()
        val_appeared = set()
        count = 0
        for i in freq_arr:
            if i not in val_appeared:
                val_appeared.add(i)
            else:
                curr = i
                while curr > 0 and curr in val_appeared:
                    curr -= 1
                    count += 1
                val_appeared.add(curr)
        return count