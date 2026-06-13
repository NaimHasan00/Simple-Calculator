#Hello there! I'm Naim Hasan. I made this simple calculator from my curiosity to learn Python.
#As this is a very simple calculator, I tried my best to make this calculator as best as possible.
#Feel free to conact me on FB- https://www.facebook.com/ewwnaim or Website: https://naimhasan99.netlify.app  
#Thanks! 

#Declaring variables
#--------------------
#welcome area

wlc_grt = "Welcome to Basic Calculator "
wlc_ask = "Your name Mr. "
wlc_fnl = "Okay Mr. {}! What do you want to do today? "

#mathmetical operations
opt = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Power", "6. Root", "0. Quit"]

#result
rslt = "The result is: "
err = "Invalid choice! Try again!"

#----------------------

#Main work

def wlc():
    
    print(wlc_grt)
    print(wlc_ask)
    id_ = input()
    print(wlc_fnl.format(id_))
    for option in opt:
        print(option)
        
        
def options():
    
  while True:
      
        user = int(input("Which operation you want to do? : "))
        if user == 1:   #addition
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            print(rslt, ask1 + ask2)
            
        elif user ==2: #subtraction
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            print(rslt, ask1 - ask2)
        
        elif user ==3:  #multiplication
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            print(rslt, ask1 * ask2)
            
        elif user ==4:  #division
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            
            if ask2 == 0:
                print("A real number can't be divided by zero (0) ! Try again buddy!")
                continue
            
            print(rslt, ask1 / ask2)
            
         
        elif user == 5:  #to the power of
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            print(rslt, ask1 ** ask2)
            
         
        elif user == 6: # nth root
            ask1 =int(input(" Enter the first number: "))
            ask2 =int(input("Enter the second number: "))
            print(rslt, ask1 ** (1/ask2))
        
        elif user == 0 : #Exit
            print("Thanks for using this 'Simple Calulator by Naim'. See ya again! ")
            break
        
        else: 
            print(err)
       
#calling functions

wlc()
options()

