#Improvise further and use Python to not allow users to enter anything other than an int/float and 
#ask for input until entered

#Sum 2 numbers using functions
def add_two_numbers():
    while True:
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            break
        except ValueError:
            print("Please enter only integer values!")

    c = a + b
    print(f"The sum is: {c:.2f}") 

add_two_numbers()