class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        Palindrome={}
        longest_palindrom=''
        
        def expand_center(left,right):
            while left >=0 and right<len(s) and s[left]==s[right]:
                substring=s[left:right +1] #to include letter(if right=3 letter in index(3) so I increment right to include letter in index 3 so right=4,index 3 included)
                if substring in Palindrome:
                    Palindrome[substring] +=1
                else:
                    Palindrome[substring] = 1
                left -=1
                right +=1
                        


        for i in range(len(s)):
            expand_center(i,i)    #Odd(to handle this type of sub palindrome): "aba", "a", "b"  to    
            expand_center(i,i+1)  #Even(to handle this type of sub palindrome): "abba", "aa"

        for i in Palindrome.keys():   
            
            if len(i) >len(longest_palindrom)  :
                longest_palindrom=i
        
        
        return longest_palindrom 

Solution=Solution()
a=Solution.longestPalindrome('babad')
print(a)



"""



Here's a detailed walkthrough of what happens with the left and right indices during each iteration for the string s = "ababa":
For i = 0:

    Odd-length: expand_around_center(0, 0)
        Initial: left = 0, right = 0
        Characters: s[0] = "a"
        Found: Substring "a"
        Expand: left = -1, right = 1 (loop exits as left < 0)

    Even-length: expand_around_center(0, 1)
        Initial: left = 0, right = 1
        Characters: s[0] = "a", s[1] = "b"
        No palindrome found (loop exits as s[left] != s[right])

For i = 1:

    Odd-length: expand_around_center(1, 1)
        Initial: left = 1, right = 1
        Characters: s[1] = "b"
        Found: Substring "b"
        Expand: left = 0, right = 2
        Characters: s[0] = "a", s[2] = "a"
        Found: Substring "aba"
        Expand: left = -1, right = 3 (loop exits as left < 0)

    Even-length: expand_around_center(1, 2)
        Initial: left = 1, right = 2
        Characters: s[1] = "b", s[2] = "a"
        No palindrome found (loop exits as s[left] != s[right])

For i = 2:

    Odd-length: expand_around_center(2, 2)
        Initial: left = 2, right = 2
        Characters: s[2] = "a"
        Found: Substring "a"
        Expand: left = 1, right = 3
        Characters: s[1] = "b", s[3] = "b"
        Found: Substring "aba"
        Expand: left = 0, right = 4
        Characters: s[0] = "a", s[4] = "a"
        Found: Substring "ababa"
        Expand: left = -1, right = 5 (loop exits as left < 0)

    Even-length: expand_around_center(2, 3)
        Initial: left = 2, right = 3
        Characters: s[2] = "a", s[3] = "b"
        No palindrome found (loop exits as s[left] != s[right])

For i = 3:

    Odd-length: expand_around_center(3, 3)
        Initial: left = 3, right = 3
        Characters: s[3] = "b"
        Found: Substring "b"
        Expand: left = 2, right = 4
        Characters: s[2] = "a", s[4] = "a"
        No further expansion (loop exits as s[left] != s[right])

    Even-length: expand_around_center(3, 4)
        Initial: left = 3, right = 4
        Characters: s[3] = "b", s[4] = "a"
        No palindrome found (loop exits as s[left] != s[right])

For i = 4:

    Odd-length: expand_around_center(4, 4)
        Initial: left = 4, right = 4
        Characters: s[4] = "a"
        Found: Substring "a"
        Expand: left = 3, right = 5 (loop exits as right >= len(s))

    Even-length: expand_around_center(4, 5)
        Initial: left = 4, right = 5
        No palindrome found (loop exits as right >= len(s))

Summary of Left and Right Indices

    For odd-length palindromes, the center is a single character, with left and right starting at the same index.
    For even-length palindromes, the center is between two characters, with left starting at the current index and right at the next index.
    The indices expand outward as long as the conditions for a palindrome are met.




"""