class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        largest = 0
        for n in nums:
            if n - 1 not in nums:
                #start of sequence
                count = 0
                i = 0
                while n + i in nums:
                    count += 1
                    i += 1
                if count > largest:
                    largest = count
        return largest
