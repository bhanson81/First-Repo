class findLongestCommPrefix:
    def longestCommonPrefix(self, strngs):
        """
        :type strngs: List[str]
        :rtype: str
        """
        if not strngs: return ""
        if len(strngs) == 1: return strngs[0]
        
        strngs.sort()
        p = ""
        for x, y in zip(strngs[0], strngs[-1]):
            if x == y: p+=x
            else: break
        return r
