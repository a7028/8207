def f(x,y): 
    p = x+y 
    return p 
 
n = int(input("Enter the no. of iterations n= ")) 
 
x0 = float(input("Enter the initial value of x0 = " )) 
y0 = float(input("Enter the initial value of y0 = " )) 
 
x1 = float(input("Enter the value of x1 = ")) 
h = (x1-x0)  
h = round(h,3) 
 
print("h = ", h) 
 
# Calculate y value for 1st iteration using predictor formula 
y1 = y0 + h*f(x0,y0) 
y1 = round(y1,3) 
print('y1 = ', y1) 
 
# Using corrector formula calculate y1 for next iteration by using above 
y1 
# Itration 1 
for i in range(0,n): 
    y1 = y0 + (h/2)*(f(x0,y0) + f(x1,y1)) 
    y1 = round(y1,4) 
    print('y1 = ', y1)
