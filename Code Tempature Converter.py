#Authour: Candice Long
#Date: 10/17/2025
#Purpose: creating a pyhon program that allows nmeric entery of a tempature

#greeted user
print("Hello,I'm Candice Long and this is a Tempature Conversion Project :)" )

#asked user for input
fltTemperature = float(input("Please enter a tempature: "))
strDegree = (input("What was the tempature, F for Fahrenheit or C for Celsius? "))

#wrong input termination of program
if strDegree not in ("F","C"):
    print("Enter a F or C")
    exit()

#Fahrenheit Conversion to Celsius
if strDegree == ("F"):
    if fltTemperature > 212:
        print ("Temp can not be > 212")
    else:
        fltCelsius = (5.0/9.0) * (fltTemperature - 32)
        print("The Celsius equivalent is : " +format(fltCelsius,'.1f'))

#Celsius Conversion To Fahrenheit
if strDegree == ("C"):
    if fltTemperature > 100:
        print("Temp can not be > 100")
    else:
        fltFahrenheit = ((9.0/5.0)* fltTemperature + 32)
        print("The Fahrenheit equivalent is: " +format(fltFahrenheit,'.1f'))
    
