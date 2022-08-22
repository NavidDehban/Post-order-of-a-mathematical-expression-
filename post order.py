

def print_rev(s):
    l = len(s)
    for i in range(l-1,-1,-1):
        a = s.pop()
        if a == '(':
            break
        print(a, end = '')

def prio(a,b):
    priority = [['(',')'],['*','/','%'],['+','-'],['**']]
    for i in range(len(priority)):
        for j in priority[i]:
            if a == j:
                a = i
            if b ==j:
                b = i
    if a < b : 
        return 1 
    else: 
        return 0

def check(x,s):
    l = len(s)
    if len(s) == 0 or s[l-1] == '(':
        s.append(x)
    else:
        for i in range(l-1,-1,-1):
            if prio(x,s[i])==1:
                s.append(x)
                break
            else:
                if s[i] in ['(',')'] :
                    s.append(x)
                    break
                else:
                    print(s.pop(),end='')
                    if  len(s)== 0:
                        s.append(x)
                


operation = ['*','/','%','+','-','**']
input_ = input()
s = []
for x in input_:
    if x in operation: 
        check(x,s)
    elif x == '(':
        s.append(x)
    elif x == ')':
        print_rev(s) 
    else:
        print(x, end = '')
    # print('-------------')
    # print(s)
    # print('-------------')

for i in range(len(s)-1,-1,-1):
    if s[i] in ['(',')']:
        continue
    print(s[i], end = '')
    
    
