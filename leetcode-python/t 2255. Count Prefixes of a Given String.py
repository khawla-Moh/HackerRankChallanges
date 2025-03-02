class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count=0
        new_arr=[]
        substring=[s[:i] for i in range(1, len(s) + 1)]
        print(substring)
        for word in words:
             if word in substring :
                new_arr.append(word)
                 #for word in words:
        #    m=word    
           #for letter in range(min(len(s), len(word))):
           #    if m[count] in s:
           #        new_arr.append(m)
        return len(new_arr)   
                      

"""         
    def countPrefixes1(self, words: List[str], s: str) -> int:
		res = 0
		for word in words:
			if s[:len(word)] == word: res += 1]
		return res       
       
""" 
""" 
    def countPrefixes2(self, words: List[str], s: str) -> int:
        count=0
        for word in words:
            n=len(word)
            if s[0:n]==word:
                count+=1
        return count

"""           

o=Solution()
words = ["a","a"]
s = "aa"
d=o.countPrefixes(words,s)
print(d)        