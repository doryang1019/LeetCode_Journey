class TimeMap:

    def __init__(self):
        self.dic = dict()



    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.dic.get(key, [])
        left = 0
        right = len(values) -1
        #print(values)
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                left = middle + 1
                res = values[middle][0]

            else:
                right = middle - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
