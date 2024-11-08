# Runtime 149ms
# Beats 27.87%

# Memory 73.90MB
# Beats 42.92%

class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        currentValue = self.timemap.get(key, [])
        currentValue.append([value, timestamp])
        self.timemap[key] = currentValue

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key)
        if values:
            start = 0
            end = len(values) - 1
            while start <= end: 
                mid = (start + end) // 2

                # values: [[value, timestamp], [value, timestamp], [value, timestamp]]
                midTimestamp = values[mid][1]
                midValue = values[mid][0]
                if midTimestamp == timestamp: 
                    return midValue
                elif midTimestamp > timestamp:
                    end = mid - 1
                    # Find the previous timestamp, if one does not exist
                    if end >= 0 and values[end][1] < timestamp: 
                        return values[end][0]
                else:
                    start = mid + 1
                    # Find the previous timestamp, if one does not exist
                    if start > len(values) - 1 or values[start][1] > timestamp:
                        return midValue
        return ''
