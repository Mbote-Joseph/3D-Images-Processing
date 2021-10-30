import random
 
amount = random.randint(0,20)+round(random.randint(0,100)/100,2)
 
#Show random amount generated on screen
print("Amount owed:"+str(amount))
 
#Ask the user for amount he is paying
payment = float(input("Enter payment amount:"))
 
#Calculate the change
change = payment - amount
 
if(change > 0):
    #Calculate the dollars that are to be paid to customer by converting it into integer
    dollar = int(change)
 
    #Calculate the change after dollars have been calculated
    change = change - dollar
 
    #Set quarter, dimes and nickel to 0
    quarter = 0
    dimes = 0
    nickel = 0
 
    #Calculate quarter, dimes and nickel if change is greater than 0
    if(change > 0):
        quarter = int(change/0.25)
        dimes = int((change - quarter * 0.25)/0.1)
        nickel = int((change - quarter * 0.25 - dimes * 0.1)/0.05)
        change = change - quarter * 0.25 - dimes * 0.1- nickel * 0.05
        nickel = int(nickel + round(change*2,1)*10)
 
    if(dollar == 0 and quarter == 0 and dimes == 0 and nickel == 0):
        print("No change owed") #Due to rounding to nearest nickel, no change is owed
    else:
        print("You got "+str(dollar)+" dollars, "+str(quarter)+" quarters, "+str(dimes)+" dimes and "+str(nickel)+" nickels back in change")
else:
    print("No change owed")