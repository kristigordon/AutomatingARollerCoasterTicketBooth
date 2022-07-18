# AutomatingARollerCoasterTicketBooth
Created a program to automate a roller coaster ticketing booth through the process of assesing height and receiving payment for the ticket. 

```
print("Welcome to the one and only Kris Kodes Koaster. Step right up!")
height = input("Enter your height. \nFor example, 5ft 4inches would be entered a s 5.4\n")
missing = 4 - float(height)
grow = round(missing, 2)
if float(height) >= 4:
    print("You can purchase a ticket! That will be 1 bitcoin.")
else:
    print(f"Sorry, please grow {grow} inche(s) and get back to us")
    
```

<img width="1187" alt="Screen Shot 2022-07-18 at 3 17 21 PM" src="https://user-images.githubusercontent.com/66803124/179599968-82e5a4b0-0d24-427f-abe3-b9925bce8662.png">
