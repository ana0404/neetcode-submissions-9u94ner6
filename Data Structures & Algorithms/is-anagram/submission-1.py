class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count_s,count_t = {},{}
        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i],0)+1
        #     count_t[t[i]] = count_t.get(t[i],0)+1
            
        # return count_s == count_t

        arr_s = [0]*26
        arr_t = [0]*26

        for ch in s:
            arr_s[ord(ch)-ord('a')]+=1
        for ch in t:
            arr_t[ord(ch)-ord('a')]+=1
        return arr_s == arr_t

               