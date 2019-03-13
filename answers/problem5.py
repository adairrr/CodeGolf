def p(s):
    if len(s)>0:
        print(s)
        p(s[:-1])
        if len(s)!=1: print(s) 
p(input())