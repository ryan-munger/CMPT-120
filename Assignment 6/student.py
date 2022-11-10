#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random

class student:
    def __init__(self, name, studentID, year, major, gpa):
        self.name = name
        self.studentID = studentID
        self.year = year
        self.major = major
        self.gpa = gpa
    
    def honors(self):
        if self.gpa > 3.5:
            return True
        else:
            return False

    def freeLunch(self):
        # hi melissa dont worry about this im just being extra for no reason
        randID = ""
        for x in range(4):
            randID = randID + str(random.randint(0, 9))
            # print(randID)
        randID = int(randID)
        if(self.studentID == randID):
            return "winner! student", self.name, "gets free lunch!"
        else:
            return "loser"
    
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    ryan = student("Ryan", 9767, "f", "Cyber Comp Sci", 4.0)
    student2 = student("Moth", 4444, "s", "Cyber", 2.3)
    george = student("George", 5690, "j", "Business", 0.2)
    
    # yes i am this lazy deal with it
    students = [ryan, student2, george]
    for s in students:
        if s.honors():
            print(s.name, "can do honors")
        else:
            print(s.name, "cannot do honors")
        print(s.freeLunch())


main()
