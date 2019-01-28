# calls problem being viewed!
def main():
    # problem1()
    # problem2()
    problem3()


# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. Print the result returned from your function.
#
# BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
#
# def in1to10(n, outside_mode):
#
# Examples of Expected Output:
#
# in1to10(5, False) → True
#
# in1to10(11, False) → False
#
# in1to10(11, True) → True
def problem1():
    n = int(input("Enter a number\n"))
    outsideMode = input("If your number is less than or equal to 10 enter false , else enter true\n")

    print(in1to10(n, outsideMode))
def in1to10(n, outsideMode):
    if outsideMode == "false":

        if n <= 10 and n >= 1:
            return (True)
        else:
            return (False)
    else:
        if n < 1 or n > 10:
            return(False)
# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
# Once the user enters the equal sign to quit,
# print all the strings that were entered as one line with each word separated by a comma and space.
# Example of Expected Output:
# You, Entered, These, Words, Today
def problem2():
    userInputArray = []
    userInput = ""

    while userInput != '=':
        userInput= input("Enter something\n")
        if userInput != '=':
            userInputArray.append(userInput)
    print(','.join(userInputArray))

# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Print the result from your function.
#
# BONUS: Get the number from User input instead of hardcoding it
#
# def near_ten(num):
#
# Examples of Expected Output:
#
# near_ten(12) → True
#
# near_ten(17) → False
#
# near_ten(19) → True
def problem3():
    n = int(input("Enter a number\n"))
    print(near_ten(n))
def near_ten(n):
    numArray = []
    numArray.append(n-1)
    numArray.append(n+1)
    numArray.append(n+2)
    numArray.append(n-2)
    flag10= False
    for ea in numArray:
        if ea % 10 == 0:
            flag10 = True
    return (flag10)












if __name__ == '__main__':
    main()
