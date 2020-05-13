class Solution:
    
  
            
    def letterCasePermutation(self, S: str) -> List[str]:
        stack = []
        
        stack.append([S,0])
        result = []
        while len(stack) != 0 :
            #print("stack: %s" %(stack))
            current = stack.pop()
            
            index = current[1]
            string = current[0]
            
            if index == len(string) :
               result.append(string)
               continue
            if string[index].isdigit():
               stack.append([string,index + 1])
               continue
            stringLower = string[:index] + string[index].lower() + string[index+1:]
            stringUpper = string[:index] + string[index].upper() + string[index+1:]
            
            stack.append([stringLower,index+1])
            stack.append([stringUpper,index + 1])
            
        return result 