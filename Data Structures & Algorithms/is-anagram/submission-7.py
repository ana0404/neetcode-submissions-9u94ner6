class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hset1 = {}
        hset2 = {}
        for i in range(len(s)):
            if s[i] in hset1:
                hset1[s[i]]+=1
            else:
                hset1[s[i]] = 1
        for j in range(len(t)):
            if t[j] in hset2:
                hset2[t[j]]+=1
            else:
                hset2[t[j]] = 1
        return hset1 == hset2
        