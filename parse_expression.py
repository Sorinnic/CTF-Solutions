from pwn import *

r = remote("2018shell1.picoctf.com", 22973)



def degree(S): 
    current_max = 0
    max = 0
    n = len(S) 
  
    # Traverse the input string 
    for i in xrange(n): 
        if S[i] == '(': 
            current_max += 1
  
            if current_max > max: 
                max = current_max 
        elif S[i] == ')': 
            if current_max > 0: 
                current_max -= 1
            else: 
                return -1
  
    # finally check for unbalanced string 
    if current_max != 0: 
        return -1
  
    return max

while(1):
    x= r.recvall()
    if "pico" in x:
        print(x)
        break
    
    else:
        current = x[:-6]
        i=1
        while(i):
            print("IN WHILEEE")
            print(i)
            if(x[-i]=="!"):
                break
            else:
                i+=1
        x=x[i:]
        current = x.split(" + ")

        while(len(current)>1):
            a=current[0]
            b=current[1]
            if(degree(a) > degree(b)):
                c = a[:-1] + b + ")"
                d=[]
                for i in range(len(current)):
                    if(i==0):
                        d.append(c)
                    elif(i>=2):
                        d.append(current[i])
                current = d
            
            elif(degree(a)==degree(b)):
                c = a + b
                d=[]
                for i in range(len(current)):
                    if(i==0):
                        d.append(c)
                    elif(i>=2):
                        d.append(current[i])
                current = d
            
            elif(degree(a) < degree(b)):
                c = "(" + a + b[1:]
                d=[]
                for i in range(len(current)):
                    if(i==0):
                        d.append(current[i])
                    elif(i>=2):
                        d.append(current[i])
                current = d
    
    r.sendline(current[0])
        