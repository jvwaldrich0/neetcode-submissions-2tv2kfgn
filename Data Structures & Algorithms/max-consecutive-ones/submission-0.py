class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local = 0
        max_local = 0

        for num in nums:
            if num == 1:
                local += 1
            else:
                max_local = max(max_local, local)
                local = 0
        return max(max_local, local)