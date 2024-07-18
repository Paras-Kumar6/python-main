
def myfunction():
    userInput = "yes"
    while userInput == "yes":
        firstNumber= int(input("Enter one number acccording to your wish:"))
        secondNumber= int(input("Enter one number acccording to your wish:"))
        thirdNumber= int(input("Enter one number acccording to your wish:"))

        list = [firstNumber, secondNumber, thirdNumber]

        sum = list[0] + list[1] + list[2]  

        if sum < 50:
            print("Sum is lesser than 50")
        elif sum > 50:
            print("Sum is greater than 50")
        else:
            print("your answer is equal to 50")

        userInput = input("would you like to contninue? yes or no ")

myfunction()
    


firstNumber= int(input("Enter one number acccording to your wish:"))
secondNumber= int(input("Enter one number acccording to your wish:"))
thirdNumber= int(input("Enter one number acccording to your wish:"))

def myfunction2(a,b,c):
    userInput = "yes"
    while userInput == "yes":

        list = [a, b, c]

        sum = list[0] + list[1] + list[2]  

        if sum < 50:
            print("Sum is lesser than 50")
        elif sum > 50:
            print("Sum is greater than 50")
        else:
            print("your answer is equal to 50")

        userInput = input("would you like to contninue? yes or no ")
        
   

