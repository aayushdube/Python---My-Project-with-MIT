counter=0
x=10
a=0
n=balance
while a==0:
    unpaid=balance-x
    interest=(annualInterestRate/12.0)*unpaid
    balance=unpaid+interest
    if balance<=0 and counter<=11:
        break
    elif balance>0 and counter <11:
        counter+=1
    elif balance>0 and counter>=11:
        counter=0
        x+=10
        balance=n
print 'Lowest Payment: '+str(x)

