class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        valueList = self.timeMap[key]

        l, r = 0, len(valueList) - 1
        res = ""

        while l <= r:
            m = (l+r) // 2
            currTimestamp = valueList[m][0]

            if currTimestamp <= timestamp:
                res = valueList[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
