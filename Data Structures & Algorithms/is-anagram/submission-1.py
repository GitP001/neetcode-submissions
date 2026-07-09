class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        assert 1<= len(s), len(t) <= 50000
        assert s.islower(), t.islower()
        if len(s) != len(t): # edge case where two strings don't have the same length
            return False
        count_char1=defaultdict(int)
        count_char2=defaultdict(int)
        for char in s:
            count_char1[char]+=1
        for char in t:
            count_char2[char]+=1
        return count_char1==count_char2 # this returns boolean
            