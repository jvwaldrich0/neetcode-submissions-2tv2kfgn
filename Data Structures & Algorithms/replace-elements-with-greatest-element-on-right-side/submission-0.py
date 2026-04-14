class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index, num in enumerate(arr):
            if index == len(arr) - 1:
                break
            arr[index] = max(arr[index+1:])
        arr[-1] = -1
        return arr