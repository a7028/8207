 
def f(x): 
    y=x*x+8*x+1 
    return y 
 
n=int(input("enter the number of Strips 'n' = ")) 
 
x0=float(input("enter x0 value= ")) 
 
xn=float(input("enter xn value= ")) 
print() 
 
if n%2==0: 
    n=n 
else: 
    n=n*2 
 
h=(xn-x0)/n 
print("h=",h) 
 
print() 
x=[ ] 
for i in range(0,n+1): 
    z=x0 +i*h 
    x.append(z) 
print("x= ",x) 
 
y=[ ] 
for i in range(0,n+1): 
    m=f(x[i]) 
    y.append(m) 
print("y= ",y) 
 
print() 
sum1=sum2=A=0 
 
for i in range(1,n): 
    if i % 2 !=0: 
        sum1+=y[i] 
    else: 
        sum2+=y[i] 
print("sum of odd ordinates : ", sum1) 
print("sum of even ordinates : " ,sum2) 
print() 
A=(h/3)*(y[0]+y[n] + 4*sum1 + 2*sum2) 
print("Total area under curve is : ",A)    