class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                max = 0
                for k in range(i + 1, len(arr)):
                    if arr[k] > max:
                        max = arr[k]
                arr[i] = max

        return arr