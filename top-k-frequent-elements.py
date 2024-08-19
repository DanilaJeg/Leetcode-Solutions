class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frq = [[] for i in range(len(nums) + 1)]
        '''
        This is going to give a list of lists where each lists index is a list of integers with that freq
        e.g [[], [2], [4], [1], [], [], []]
        2 appears once in the list and 4 appears twice and so on


        '''
        '''
        Proper method of making count dict
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        Or this way
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        '''
        for n, c in count.items():
            frq[c].append(n)
        print(frq)
        
        result = []
        for i in range(len(frq) - 1, 0, -1):
            for n in frq[i]:
                result.append(n)
                if len(result) == k:
                    return result
