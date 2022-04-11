class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common = ""
        common = ""
        
        for s in strs[0]:
            common += s
            if all(x.startswith(common) for x in strs[1:]):
                longest_common = common
            else:
                break
            
        return longest_common
            
        