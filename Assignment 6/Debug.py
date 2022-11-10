from hashlib import new


class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    # MELISSA U ARE NOT DUMB SHSUSH 
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def isReliable(self):
        if self.model.find("Honda") or self.model.find("Toyota"):
            return "This car is reliable"
        else:
            return "This car sucks bro"

    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Sandy" , 13)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Smith", 6969, "Based Department")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    cakedUP = Cake("Marble", "Buttercream")
    
    print("This cake is:", cakedUP.flavor, cakedUP.frosting)
    #and now create another cake and print it out
    boringCake = Cake("Vanilla", "Sugar")
    print("This cake is:", boringCake.flavor, boringCake.frosting)
    
    #create a cat!
    cat1 = Cat("Meowth", 90, "Medium")
    #create another cat!
    pussy = Cat("Butthead", 1, "Short")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    vroom = Car("Honda Civic", "2008", "Silver")
    #Now print out the function you made for car :)
    print(vroom.isReliable())


main()
