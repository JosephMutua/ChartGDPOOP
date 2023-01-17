"""
Create a class called "Car" that has the following properties: make, model, year, and speed. 
The class should have a method called "accelerate" that increases the speed of the car by 
10 mph, and a method called "brake" that decreases the speed of the car by 7 mph.
"""
class Car:
    
    def __init__(self,make,model,year,speed):
        # This is a constructor that is always called when the object of the class is intatiated

        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate (self):
        # This method increases the speed of the car by 10mph

        return self.speed + 10

    def brake (self):

        # This method decreases the speed of the car by 7mph

        return self.speed - 7


car 1