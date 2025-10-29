#Name: Jude Martin
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
height = int(input("enter your height here in inches:"))
weight = int(input("enter your weight here pounds:"))
bmi = (weight/height ** 2) * 703
print(bmi)
if bmi < 18.5:
    print("you are under weight")
elif 18.5 <= bmi < 24.9:
    print("you average weight")
elif 25 <= bmi < 29.9:
    print("you are over weight")
else:
    print("you built like gorlock the destoyer")