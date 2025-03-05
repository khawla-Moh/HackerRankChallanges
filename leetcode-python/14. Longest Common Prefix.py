class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        """

        # Start with the first string as the prefix
        prefix = strs[0]
       

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the string
            while not s.startswith(prefix):
                
                
                prefix = prefix[:-1]  # Remove the last character
                
                if not prefix:
                    return ""  # No common prefix

        return prefix
    












o=Solution()

strs = ["flower","flow","flight"]
print(o.longestCommonPrefix(strs))