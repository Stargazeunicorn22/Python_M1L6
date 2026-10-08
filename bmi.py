height = float(input("Enter your height in cm: "))
weight = float (input("Enter your weight in kg: "))
a = weight/(height/100)**2
if a <= 18.4:
    print("You are under weight.")
elif a <= 24.9:
    print("You are perfectly healthy!")
elif a <= 29.9:
    print("You are a little over weight.")
elif a <= 34.8:
    print ("You are severely OVER WEIGHT. Start dieting.")
elif a <=39.9:
    print("You are obsese.")
else:
    print("YOU ARE SEVERLY OBSESE AND YOU MUST DIET AND EXERCISE.")