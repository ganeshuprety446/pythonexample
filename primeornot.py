num=int(input("enter a number to ccheck if its prime or not"))
if num>1:
 for i in range(2,num):
  if(num%i)==0:
   print(num,"is not a prime no")
   break
 else: 
  print(num,"'is prime no")
else:
 print(num,"is not a prime no")
