class Solution(object):
    def restoreString(self, s, indices):
        sr = list(s)
        for i in range(len(s)):
            sr[indices[i]] = s[i]
        new =''
        return new.join(sr)
