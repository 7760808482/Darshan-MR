x=int(input("Enter the number:"))
if x%2==0:
    print("X is an even number")
else:
    print("X is an odd number")


#Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older,they get a senior citizen discount. Otherwise, they pay the full price.

age=int(input("Enter your age:"))
if age<=5:
    print("The bus pass is free")
elif age>=60:
    print("Your come under senior citizen discount")
else:
    print("Pay the full price")




#Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
#Breakfast: 8 AM
#Lunch: 13 PM
#Dinner: 20 PM
#If none of these times, print "It's not meal time."



time=input("Enter the the time:")
if time==8:
    print("Breakfast Time")
elif time==13:
    printf("Lunch time")
elif time==20:
    print("Dinner")
else:
    print("It is not a meal time")
