balance = 999999
annualInterestRate = 0.18
remainingbalance = 1
epsilon = 0.01
lo = balance/12
hi = (balance*(1+annualInterestRate)**12)/12.0
lowpay = (lo + hi)/2

def allpayment(remainingbalance, annualInterestRate, lowpay, totalpaid):
    for i in range(1,12+1):
        unpaidbal = remainingbalance - lowpay
        interest = (annualInterestRate/12.0) * unpaidbal
        remainingbalance = unpaidbal + interest
	totalpaid = totalpaid + lowpay
    return remainingbalance

while (abs(remainingbalance) > epsilon):
    remainingbalance = allpayment(balance, annualInterestRate, lowpay, 0)
    if (remainingbalance <0):
        hi = lowpay
    else:
        lo = lowpay
    if (abs(remainingbalance) < epsilon):
        break
    else:
        lowpay = (lo + hi)/2
       
print("Lowest Payment: " + str(round(lowpay,2)))