class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if(len(str1) != len(str2)):
            return False
        list1 = list(str1)
        list2 = list(str2)
        list1.sort()
        list2.sort()
        return(list1 == list2)