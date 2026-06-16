class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        count = 0
        if(len(str1)> len(str2)):
            for i in range(len(str1)):
                if(str2.count(str1[i]) == str1.count(str1[i]) ):
                    count += 1
            if(count == len(str1)):
                return True
            else:
                return False    
        else:
            for i in range(len(str2)):
                if(str1.count(str2[i]) == str2.count(str2[i]) ):
                    count += 1
            if(count == len(str2)):
                return True
            else:
                return False    