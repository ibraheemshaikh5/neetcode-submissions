class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # val, time

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        output = ""
        values = self.map.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (r + l) // 2

            if values[m][1] <= timestamp:
                output = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return output

