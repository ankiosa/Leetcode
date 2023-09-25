'''
1. Convert multiple slash into single slash
2. remove trailing slash at the end
3. convert double period into removing the last 
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_list = path.split("/")
        
        print(path_list)
        print(path_list[0]=="")
        for each_key in path_list:
            if((""!=each_key) and ("."!=each_key)):
                if(".."==each_key):
                    if(len(stack)>0):
                        stack.pop()
                else:
                    stack.append(each_key)
        if(len(stack)==0):
            return "/"
        str_key = ""
        print(stack)
        for each_key in stack:
            str_key = str_key+"/"+each_key
        return str_key
               
               
               
        
        
        