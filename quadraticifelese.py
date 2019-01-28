# Solve the quadratic equation
import math
a = float(input('Enter a: '))

b = float(input('Enter b: '))

c = float(input('Enter c: '))


d = (b*b) - (4*a*c)


print('value for drscriminant is',d)
if d < 0:
 print ('This equation has no real solution')
elif d == 0:
 sol1= (-b+math.sqrt(d))/2*a
 print ('This equation has one solutions: ', sol1)
else:
 sol2 = (-b+math.sqrt(d))/2*a
 sol3 = (-b-math.sqrt(d))/2*a
 print ('This equation has two solutions: ', sol2, 'and', sol3)
