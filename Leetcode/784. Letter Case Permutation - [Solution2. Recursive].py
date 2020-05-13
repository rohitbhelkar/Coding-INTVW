class Solution:
    
    def recurString(self,string,temp,index,result) :
        if len(temp) == len(string) :
           result.append(temp)
           return result
        
        if string[index].isalpha() :
           
           self.recurString(string,temp+string[index].lower(),index + 1,result)
           self.recurString(string,temp+string[index].upper(),index + 1,result) 
        
        else:
           self.recurString(string,temp+string[index],index + 1,result)  
        
        return result
            
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = []
        temp = ""
        result = self.recurString(S,temp,0,result)
        return result