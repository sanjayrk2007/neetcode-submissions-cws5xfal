class     Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in range(len(s)):
            c=s[i]
            if(c=='(' or c=='{' or c=='['): 
                stack.append(c)
                top+=1
            elif(c==')'or c=='}'or c==']'):
                if(top==-1):return False
                else:
                    remove=stack.pop()
                    top-=1
                    if not ((remove == '(' and c == ')') or (remove == '{' and c == '}') or (remove == '[' and c == ']')):
                        return False

        return top == -1