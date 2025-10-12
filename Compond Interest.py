#Author: Candice Long
#Date: October 11 2025
#Purpose: Computing the monthly amount at the end of the term 

#declaring varibales


#Asking for input
PV_string=input("Enter the Starting Principle: ")
R=input("Enter the annual interest rate: ")
m_string=input("How many times per year is the interest compounded? ")
t_string=input("For how many years will the account earn interest? ")


#Converting to a float
principal=float(PV_string)
annual_rate= float(R)/100
compounding=float(m_string)
years=float(t_string)


#doing the multiplication
FV = principal *(1 + annual_rate / compounding)**(compounding * years)

#Result
print(f"At the end of the 2 years you will have $"+format(FV,'.2f'))
