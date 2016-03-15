balance = 3855

annualInterestRate = 0.15

lowpay = 0

remainingbalance = 1

def allpayment(remainingbalance, annualInterestRate, lowpay, totalpaid):
    for i in range(1,12+1):
        unpaidbal = remainingbalance - lowpay
        interest = (annualInterestRate/12.0) * unpaidbal
        remainingbalance = unpaidbal + interest
	totalpaid = totalpaid + lowpay
        #print ("lowpay = " + str(lowpay))
        #print ("month = " + str(i))
        #print ("balance = " + str(remainingbalance))
        #print ("totalpaid = " + str(totalpaid))
    return remainingbalance

while (remainingbalance > 0):
    lowpay = lowpay + 10
    remainingbalance = allpayment(balance, annualInterestRate, lowpay, 0)
    
print("Lowest Payment: " + str(lowpay))
    