# Debug.py
# instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix them. (Run them yourself and see what the output is!)
# also, we have some input practice!
def main():
    # this is a nice solid working one!
    name = input("your name is? ")
    print("Hello,", name)

    # this isn't printing anything :( so sad. what's wrong with her? Why she not printing out?
    color = input("what's your favorite color? ")
    print("Your favorite color is", color)

    # I thought i did this right :( can you fix it for me?
    age = input("how old are you? ")
    print("You are " + str(age) + " years old")

    # Start with this one! We have a compilation error :(
    # Side note: you can put these statements in parentheses or not. it's up to you.
    if (5 > 3):
        print("5 is greater than 3")

    # There are multiple correct answers and adjustments to this one
    isFive = 5
    if isFive > 5:
        print("isFive is greater than 5")
    else:
        print("isFive is less than or equal to 5")

    # more multiple correct answers. Similar to the first. Adjust as perceived
    toCheck = 4
    if toCheck > 5:
        print(toCheck, "is greater than 5.")
    elif toCheck < 3:
        print(toCheck, "is less than 3")
    else:
        print(toCheck, "is between 3 and 5")

    # Is it really printing the BEST option though? Rearrange these as you see fit
    toCheck = 5
    if toCheck > 7:
        print("toCheck is greater than 7")
    elif toCheck == 5:
        print("toCheck is 5")
    elif toCheck < 6:
        print("toCheck is less than 6")
    else:
        print("toCheck is invalid")


main()
