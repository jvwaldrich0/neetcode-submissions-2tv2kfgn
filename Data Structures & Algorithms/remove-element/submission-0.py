class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_removed = 0
        for i in range(0, len(nums)):
            i -= total_removed
            if nums[i] == val:
                nums.pop(i)
                total_removed += 1
        return len(nums)
