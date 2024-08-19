class Solution:
    def romanToInt(self, nums: str) -> int:
        rome = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and rome[nums[i]] < rome[nums[i + 1]]:
                total -= rome[nums[i]]
            else:
                total += rome[nums[i]]
        return total
