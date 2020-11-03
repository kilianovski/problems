class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        suspect = ''
        stack = s

        for i in range(len(t)):
            if stack != '' and t[i] == stack[0]:
                suspect += t[i]
                stack = stack[1:]



        return suspect == s


s = Solution()

# print( s.isSubsequence('23', '125534') )
print( s.isSubsequence("aca", 'aaca') )

ss = "leeeeetcode"
t = "ylyeyeyeyeyeyeytycyoydyey"

print( s.isSubsequence(ss, t) )