#user-defined function with no argument
def scream():
    print("aaahhhhhhhh")

scream()

#user-defined function with 1 argument
def multiplyByTwo(number):
    print(number*2)

multiplyByTwo(6)

#user-defined function with 2 argument
def add(a,b):
    return (a+b)

answer = add(5,9)

multiplyByTwo(answer)

#function inside a function
def AddAndMultiplyByTwo(a,b):
    return multiplyByTwo(a+b)

AddAndMultiplyByTwo(4,9)

#recursive functions (this is bad do not do this)
def multiplyByThree(x):
    print(multiplyByThree(x*3))

multiplyByThree(3)




