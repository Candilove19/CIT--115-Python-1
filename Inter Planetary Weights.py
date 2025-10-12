#Author: Canidce Long
#Date: 10/1/2025
#Purpose: Inter Planetary Weights

#declared variables
f_mercury=0.38
f_venus=0.91
f_moon=0.165
f_mars=0.38
f_jupiter=2.34
f_saturn=0.93
f_uranus=0.92
f_neptune=1.12
f_pluto=0.066

#Asked user for input
s_name=input("Please enter your name: ")
i_weight=input("Please enter your earth weight: " )
print(s_name + " here are you weights on our solar systems planets:")

#converted string to float 
weight =float(i_weight)

#Did the multiplication between the two variables
f_mer = f_mercury*weight
f_ven = f_venus*weight
f_moo = f_moon*weight
f_mar = f_mars*weight
f_jup = f_jupiter*weight
f_sat = f_saturn*weight
f_ura = f_uranus*weight
f_nep = f_neptune*weight
f_plu = f_pluto*weight
#printed the results
print(f"Weight on Mercury:    {f_mer}")
print(f"Weight on Venus :     " + format(f_ven, '.2f'))
print(f"Weight on Moon  :     " + format(f_moo,'.2f'))
print(f"Weight on Mars  :     {f_mar}")
print(f"Weight on Jupiter :   {f_jup}")
print(f"Weight on Saturn :    " + format(f_sat, '.2f'))
print(f"Weight on Uranus :    {f_ura}")
print(f"Weight on Neptune :   " + format(f_nep, '.2f'))
print(f"Weight on Pluto :     " + format(f_plu, '.2f'))


