#first of all, breathe
#don't let this intimidate you. break it down a part at a time. You've done all of these separately and now we're just combining them.
'''
Instructions: Create a list with at least 8 numbers, and make sure you have a raandom dispersement between 0-50
Create a loop (which loop would be best given we know how long we're going [the length of the list]?) that runs through the entire list
Inside of your loop, have an if/elif/else that checks AT EACH INDEX OF THE LIST:
if the number is greater than 35: print ("greater than 35")
elif the number is between 20-35: print ("between 20-35")
elif the number is between 5-20: print ("between 5 and 20")
else (the number is less than 5)
'''

def main():
    num = [30, 23, 1, 44, 2, 45, 38, 7, 32, 49]
    for x in num:
        if x > 35:
            print("greater than 35")
        elif x >= 20: # i dont need to check the other conditional because of the nature if the if that preceded it :)
            print("between 20-35")
        elif x >= 5:
            print("between 5 and 20")
        else:
            print("num less than 5")
main()