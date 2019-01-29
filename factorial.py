#this is the example of for loop statement

num=int(input('enter a number to calculate its factorial'))
factorial = 1
for i in range(1,num + 1):
 
      factorial = factorial*i
   
print("The factorial of",num,"is",factorial)
