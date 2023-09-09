from random import choice
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_ele, ind = self.arr[-1], self.dict[val]
        self.arr[ind] = last_ele
        self.dict[last_ele] = ind
        self.arr.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()