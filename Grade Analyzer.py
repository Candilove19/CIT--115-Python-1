#Authour: Candice Long
#Date: 11/2/2025
#Purpose: buildinga grade ananalyzer

s_name = (input("Please enter your name: "))
print ("Please enter your four test scores:" )
int_test1 = int(input("Test 1: "))
int_test2 =  int(input("Test 2: "))
int_test3 =  int(input("Test 3: "))
int_test4 =  int(input("Test 4: "))
#making sure all numbers are whole numbers 
if int_test1 < 0 or int_test2 < 0 or int_test3 < 0 or int_test4 < 0:
    print("Test scores must be greater than 0. ")
    exit()
#asking f drop grade is wanted 
strDrop_lowest(input("Do you want to drop your lowest grade? Y of N?" ))

if strDrop_lowest not in ('Y','N'):
    print("Enter Y or N to drop the lowest grade.")
    exit()
#calculating scores for lowest grade dropped
fltAver = 0.0
if strDrop_lowest == 'Y':
    if int_test1 <= int_test2 and int_test1 <= and int_test3 and int_test1 <= int_test4:
    fltAver = (int_test2 + int_test3 + int_test4)/3
    elif int_test2 <= int_test1 and int_test2 <= and int_test3 and int_test2 <= int_test4:
    fltAver = (int_test1 + int_test3 + int_test4)/3
    elif int_test3 <= int_test1 and int_test3 <= and int_test2 and int_test3 <= int_test4:
    fltAver = (int_test1 + int_test2 + int_test4)/3
    else:
        fltAver = (int_test1 + int_test2 + int_test3)/3
#finding the average sore
else:
    fltAver = (int_test1 + int_test2 + int_test3 + int_test4)/4

#letter grades

strGrade = ""
if fltAver >= 97.0:
    strGrade = "A+"
elif fltAver >= 94.0:
    strGrade = "A"
elif fltAver >= 90.0:
    strGrade = "A-"
elif fltAver >= 87.0:
    strGrade = "B+"
elif fltAver >= 84.0:
    strGrade = "B"
elif fltAver >= 80.0:
    strGrade = "B-"
elif fltAver >= 77.0:
    strGrade = "c+"
elif fltAver >= 74.0:
    strGrade = "C"
elif fltAver >= 70.0:
    strGrade = "C-"
elif fltAver >= 67.0:
    strGrade = "D+"
elif fltAver >= 64.0:
    strGrade = "D"
elif fltAver >= 60.0:
    strGrade = "D-"
else:
    strGrade = "F"


print(s_name + "test Average is: "  +format (fltAver: '.1f'))
print("Letter grade for test is: " +format (strGrade))

    

    


 

