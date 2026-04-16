class LongestSubstring:
    """
    longest substring in the given string
    """
    def long_sub(self,s:str) -> str:
        """
        using sliding window with set
        """
        char_set=set()
        max_len=0
        left=0
        start=0
        for right, value in enumerate(s):
            if value in char_set:
                while value in char_set:
                    char_set.remove(s[left])
                    left+=1
            
            char_set.add(value)
            if right-left+1>max_len:
                max_len=right-left+1
                start = left
        return s[start: start+max_len]
    
    def long_sub_map(self,s:str) -> str:
        """
        using sliding window with set
        """
        char_set={}
        max_len=0
        left=0
        start=0
        for right, value in enumerate(s):
            if value in char_set:
                left=max(left, char_set[value]+1)
            
            char_set[value]=right
            if right-left+1>max_len:
                max_len=right-left+1
                start = left
        return s[start: start+max_len]
    
ls=LongestSubstring()
obj=ls.long_sub("geeksforgeeks")
obj1=ls.long_sub_map("geeksforgeeks")
print(obj)
print(obj1)
