print("Welcome to the one and only Kris Kodes Koaster. Step right up!")
height = input("Enter your height. \nFor example, 5ft 4inches would be entered a s 5.4\n")
missing = 4 - float(height)
grow = round(missing, 2)
if float(height) >= 4:
    print("You can purchase a ticket! That will be 1 bitcoin.")
else:
    print(f"Sorry, please grow {grow} inche(s) and get back to us")

