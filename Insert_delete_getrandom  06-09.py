import random
class RandomizedSet:

    def __init__(self):
        self.data = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.data.append(val)
        self.pos[val]=len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        index=self.pos[val]
        last_val=self.data[-1]

        self.data[index]=last_val
        self.pos[last_val] = index

        self.data.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
