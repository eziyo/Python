
"""
ISSE Calculator

"""


print("Hi")

salary = float(input("Please enter salary per month: "))
home_sqr = float(input("Please enter your house square meter (if you have not, type 0): "))
family_size = int(input("Please enter your family size: "))

salary_per_year = salary * 12 
salary_in_eu = salary_per_year / 55000    # you can change the IRANIAN RIAL value here, if you want..
salary_in_euu = salary_per_year / 5000
real_home = home_sqr * .2
home_value = real_home * 500

if family_size == 1:
   real_size = 1

elif family_size == 2:
   real_size = 1.57

elif family_size == 3:
   real_size = 2.04

elif family_size == 4:
   real_size = 2.46

elif family_size == 5:
   real_size = 2.85  

else:
   real_size = 0

isse = salary_in_eu + home_value
issee= salary_in_euu + home_value

if real_size != 0:
   final_isse = isse / real_size
   print("You'r isse (rial to euro : 55,000): ", final_isse)
else:
   print("Family size not in range 1 to 5.") 

if real_size != 0:
   final_issee = issee / real_size
   print("You'r isse (rial to euro : 5000): ", final_issee)
else:
   print("Family size not in range 1 to 5.") 