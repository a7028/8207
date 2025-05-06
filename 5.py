 
n= int(input("enter number of data points n =  " )) 
print("enter  x values " , 
      end = " ") 
 
x= [ ]  
 
for i in range (0,n): 
    z=input( 'x' + str(i) + '=' ) 
    x.append(float(z)) 
print (x) 
 
print("enter  y values " , 
      end = " ")  
 
y= [ ]  
 
for j in range(0,n): 
    m=input( 'y' + str(j) + '=' ) 
    y.append(float(m)) 
print (y) 
 
xr= int (input( " enter the value of xr = ") ) 
sum=0 
for i in range (0,n): 
    prod=1 
    for j in range (0,n): 
        if i!=j : 
            prod= prod* ( (xr-x[j]) / (x[i]- x[j]) ) 
             
    sum= sum  + prod * y[i] 
           
print(" f (x) = " , sum ) 
 
 
 
