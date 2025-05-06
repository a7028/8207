n=int(input("enter degree of equation =")) 
a = [ ] 
for i in range (0,n+1): 
    x= input ("a[" +str(i)+ "] =") 
    a.append(int(x)) 
print (a) 
 
r0 = float(input("enter initial root = ")) 
k=int(input("enter number of iterations = ")) 
 
for j in range (1,k+1): 
    b=[ ] 
    b.append(a[0]) 
     
    for i in range(1,n+1): 
        x=round((a[i]+r0*b[i-1]),4) 
        b.append(float(x)) 
    print (b) 
     
    c=  [ ] 
    c.append(a[0]) 
     
    for i in range (1,n+1): 
       x=round((b[i]+r0*c[i-1]),4) 
       c.append(float(x)) 
    print (c) 
     
    r1=round((r0-(b[n]/c[n-1])),4) 
    print() 
    print("approximate root is =" , r1) 
    r0=r1 
     
print ("approximate root after ", k,"iterations =" , r0)  