stack=[1,2,3,4,5]
choice=1
while choice!=0:
 choice=int(input("enter 1 for push 2 for pop and 3 for display")
 if (choice==1):
  item=int(input("enter item"))
  stack.append(item)
  print('push is done')
 elif (choice==2):
  print("item popped")
 elif (choice==3):
  print(stack)
else:
 break
 choice=(choice+1):
 

