class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        """
        for word in words:
            result=word
        new_arr=[]
        for i in result.split(separator):
            new_arr.append(i)
        return new_arr
        """
        return [splitWord for word in words for splitWord in word.split(separator) if splitWord]


o=Solution()
words =["$easy$","$problem$"]
separator = "$"        
d=o.splitWordsBySeparator(words,separator)
print(d)

