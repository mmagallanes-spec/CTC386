#Mariio Magallanes
# class 9
# GitHub test comment


#this is a function for option 5
def temperature_c_to_f():

    f = float(input("Please enter the current temperature in degrees fahrenheit: "))
    c = (f-32)*(5/9)
    print("YOur current temparute in degrees Celsius is ",c)


#option 0
option = 0

name = input("What is your name:")
print("Greeetings", name, "Please select a choice from the following menu.")

print("***************")
print("\U0001F602"*9)
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("***************")
print("\U0001F602"*9)

option = int(input("Option:" ))

#option 1
if option == 1:
    print("Why do scientist trust atoms?")
    print("beacuse they make up everything!")

#option 2
if option == 2:
    for i in range(15):
        print("Hello", name)

#option 3
if option == 3:
    number = int(input("Enter a number:"))
    for i in range(number):
        print("Do, or Do not. There is no try.")

#option 4
if option == 4: 
    g = -1
    n = 25
    print("This is a Lucky Number Game.")
    print("Your entry must be between 0-100.")

    while g != n:
        g = int(input("Enter your lucky guess: "))
        
        if (g < 0 ) or (g > 100):
            print("Your number is out of range")
#            g = int(input("Enter your lucky guess: "))

        elif (g > n):
            print("Your guess is too big! Please try again.")

        elif (g < n):
            print("Your guess is too small! Please try again.")
    
        else:
            print("Thank you, your guess is the Lucky Number.")

#option 5 
if option == 5:
    
    celsius = temperature_c_to_f()
    

