'''
Created on Jun 13, 2018

@author: rajat.arora07
'''

def chk_parenthesis(bracket_string):
    str1=''
    count=0
    for ele in bracket_string:
        # For every opening bracket,count is increased and str is updated.
        if(ele=='(' or ele=='[' or ele=='{'):
            count+=1
            str1+=ele
        #prvs=str1[len(str1)-1]
        
        # For every closing bracket,it is checked with last charecter of str1. #If it is the same charecter,count is decreased.
        elif(ele==')'):
            if(len(str1)==0 or str1[len(str1)-1]!='('):
                return False
            str1=str1[:len(str1)-1]
            count-=1
        elif(ele==']'):
            if(len(str1)==0 or str1[len(str1)-1]!='['):
                return False
            count-=1
            str1=str1[:len(str1)-1]
        elif(ele=='}'):
            if(len(str1)==0 or str1[len(str1)-1]!='{'):
                return False
            str1=str1[:len(str1)-1]
            count-=1
        
        #If at any point of time, count is less than zero i.e. more brackets are closed then that were opened then return False.
        if(count==-1):
            return False
        #print str1,count
    
    #If on completely traversing the input,if there is any bracket open the return False. 
    if(count!=0):
        return False
    return 'balanced'
            
t=int(input())
for i in range(t):
    str1=input()
    print(chk_parenthesis(str1))