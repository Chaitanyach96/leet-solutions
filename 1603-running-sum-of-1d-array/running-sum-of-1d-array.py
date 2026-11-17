class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        op = []

        for i in range(len(nums)):
            total = total + nums[i]
            op.append(total)

        return op    