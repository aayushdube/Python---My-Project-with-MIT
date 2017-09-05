#This code uses bisection search to make the system fastest
counter=0
a=0
n=balance
lower=balance/12
upper=(((1+annualInterestRate/12.0)**12)*balance/12.0)
x=((upper+lower)/2)
while a==0:
    unpaid=balance-x
    interest=((annualInterestRate/12.0)*unpaid)
    balance=unpaid+interest
    if abs(balance)>0 and abs(balance)<0.01:
        break
    elif balance<0 and counter<=11:
        counter=0
        upper=x
        x=((upper+lower)/2)
        balance=n
    elif balance>0 and counter<11:
        counter+=1
    elif balance>0 and counter>=11:
        counter=0
        lower=x
        x=((upper+lower)/2)
        balance=n
print 'Lowest Payment: '+str(round(x,2))
