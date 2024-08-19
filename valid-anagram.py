class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            if s[i] not in t:
                return False
            tmp = s[i]
            s = s.replace(tmp, ".", 1)
            t = t.replace(tmp, ".", 1)
        return True
        
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        if sorted(s) == sorted(t):
            return True
        return False
        
        if len(s) != len(t):
            return False
        countS,{} countT = {}, {} 
        for i in range(len(s)):
            if s[i] not in countS:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
        for c in countS:
            if c not in countT or countS[c] != countT[c]:
                return False
        return True
        return Counter(s) == Counter(t)
