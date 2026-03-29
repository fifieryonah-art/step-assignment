#clculate the net pay of the employee who gets 2000000 as the gross pay
#gross Pay = (Gross pay * tax rate)
def salary():
    gross = 2000000
    return gross
    
# am calculating the payee which is 0.3 of the salary
def payee():
    return salary() * 0.3
    
payee() 
print(payee())

#am calculating the nssf which is 0.05 of the salary
def nssf():
    return salary() * 0.05
nssf()
print(nssf())

# Am calculatng the other deductions like insuarance and bank charges which will take 5% of the gross pay
def other_deductions():
    return salary() * 0.05
other_deductions()
print(other_deductions())

# Am calculating the the total taxes of the employee which will be added together
def total_taxes():
    return (payee() + nssf() + other_deductions())
total_taxes()   
print(total_taxes())

# Am calculating the net pay of the employee which will be (grosspay - total_taxes)
def net_pay():
    return salary() - total_taxes()
    return net_pay
net_pay()
print(net_pay())
    
