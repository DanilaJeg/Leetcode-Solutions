class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)
        word, word1 = strs[0], strs[-1]
        longest = []
        for i in range(len(word)):
            if word[i] != word1[i]:
                return "".join(longest)
            longest.append(word[i])
        return "".join(longest)
            
