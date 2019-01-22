#Generate electricity bill from the following conditions If meter reading is more then 100 charagble amount will be 6.95 Rs per unitand  If meter reading is less then 100 charagble amount will be 5.95 Rs per unit.

#program for calculating electricity bill 
units=int(input("please enter the number of units you consumed in a month"))
if(units<=100):
    payAmount=units*6.95
elif(units>100):
    payAmount=(100*5.95)
    
Total=payAmount;
print("\nElecticity bill",Total)
