class Solution:
    def isValid(self, s: str) -> bool:
        opening_type = {'[', '(', '{'}
        valid_combo = {'[]','()','{}'}
        stack = []
        for ch in s:
            if(ch not in opening_type and len(stack) == 0):
                return False
            if(ch in opening_type):
                stack.append(ch)
            if(len(stack) != 0):
                top_element = stack[-1]
            if((ch not in opening_type) and (top_element + ch not in valid_combo)):
                return False
            if((ch not in opening_type) and (top_element + ch in valid_combo)):
                stack.pop()
        return(len(stack)== 0)    

