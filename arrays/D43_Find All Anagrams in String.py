class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if  len(p)>len(s):
            return []
        p_count = Counter(p)
        window = Counter(s[:len(p)])
        result = []
        if window == p_count:
            result.append(0)

        left = 0
        for right in range (len(p),len(s)):
            window[s[right]]+=1
            window[s[left]]-=1
            if window [s[left]]==0 :
                del window[s[left]]
            left += 1
            if window == p_count :
                result.append(left)         

        return result         
    