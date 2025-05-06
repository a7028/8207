
 
 
 
n =int(input("enter number of data points n = ")) 
print("enter  x values ", 
      end=" ") 
 
x = [] 
 
for i in range(0, n): 
    z = input('x' + str(i) + '=') 
    x.append(float(z)) 
print(x) 
 
print("enter  y values ", 
      end=" ") 
 
y = [] 
 
for j in range(0, n): 
    m = input('y' + str(j) + '=') 
    y.append(float(m)) 
print(y) 
 
xx = [] 
for w in range(0, n): 
    (xx.append(x[w] * x[w])) 
print(" xx = ", xx) 
 
xy = [] 
for t in range(0, n): 
    (xy.append(x[t] * y[t])) 
print(" xy = ", xy) 
sumx = sumy = sumx2 = sumxy = 0 
for i in range(0, n): 
    sumx = sumx + x[i] 
    sumy = sumy + y[i] 
    sumx2 = sumx2 + xx[i] 
    sumxy = sumxy + xy[i] 
print(" Sum_x = ", sumx) 
print(" Sum_y = ", sumy) 
print(" Sum_xx = ", sumx2) 
print(" Sum_xy = ", sumxy) 
 
Dx=(sumy*sumx)-(sumxy*n) 
Dy=(sumx*sumxy)-(sumx2*sumy) 
D =(sumx*sumx)-(sumx2*n) 
 
a =round((Dx/D),4) 
b =round((Dy/D),4) 
print(" Value of a = ", a ) 
print(" Value of b = ", b ) 
 
print (" The straight line using Least Square Method is : " , "y = " , a 
, "+" , b,"x")