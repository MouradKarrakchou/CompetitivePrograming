class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=""
        for k in range (min(map(lambda x:len(x),strs))):
            letter=strs[0][k]
            for j in (strs):
                if letter!=j[k]:
                    return(str)
            str+=letter
        return str