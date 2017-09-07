'''
Create a class to define a car with the following :
 The class should have atleast 1 class variable ( think of an attribute which remains the same across all cars ).
 A car should require the attributes Make,Model,Year,Color, Engine
Create a method 'start' to start the car. When the method is called, the car's 'status' attribute should be 'ON'
Create a method 'accelerate', which should take the argument speed. When the method is called the attribute 'speed' should increase by the specified speed passed to the method
Create a method 'decelerate', which should take the argument speed. When the method is called the attribute 'speed' should decrease by the specified speed passed to the method
Create a method 'break'. When called the speed attribute should become 0
Create a method 'Off'. When called the car's 'status' attribute should become 'FF'
Rules to implement ( make use of try, except or if else statements ) :
The car cant be started if its already ON
The car cant accelerate, decelerate, break or turned OFF if its not ON
Maximum speed of the car is 130
The car cant decelerate if the speed is 0

'''

class car:
    'Creating a car class'

    #Glabal variable number of wheels, will always be 4
    number_of_wheels = 4

    #Defining a constructor, requires make, model, year, color, engine and defaults status to OFF
    def __init__(self,make,model,year,color,engine):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.status = 'OFF'

    #start method to turn the car ON if its OFF and set the speed to 0
    def start(self):
        if self.status == 'OFF':
            self.status = 'ON'
            self.speed = 0
            print 'Car started'
        else:
            print 'Car is already ON'


    #accelerate method to accept speed as input and increase speed by the specified number. Will not increase speed over 130
    def accelerate(self,speed):
        if self.status == 'ON':
            if self.speed + speed <= 130:
                self.speed = self.speed + speed
                print 'Car speed is increased to : ' , self.speed
            else:
                print 'Maximum speed limit reached'
        else:
            print 'Turn the car on before accelerating'

    #decelerate method to accept speed as input and decrease speed by the specified number. Will not decrease speed to less than 0
    def decelerate(self,speed):
        if self.status == 'ON':
            if self.speed != 0 and ( self.speed - speed >= 0):
                self.speed = self.speed - speed
                print 'car speed reduced to : ', self.speed
            else:
                self.speed = 0
                print 'Cant decelerate any further, car speed is 0'
        else:
            print 'Cant decelerate, car is OFF '

    #breaks method ( cant use break as the method name since its a keyword) sets the speed to 0
    def breaks(self):
        self.speed = 0
        print 'Car Stopped'

    #off method turns the car status to off
    def off(self):
        self.status = 'OFF'
        print 'Car has been turned off'





#Implementation

bmw3 = car('bmw','3 series', '335i', 'blue', '4 cylinder')
bmw3.start()
bmw3.accelerate(10)
bmw3.accelerate(10)
bmw3.decelerate(10)
bmw3.decelerate(20)
bmw3.accelerate(50)
bmw3.breaks()
bmw3.accelerate(10)
bmw3.off()
bmw3.decelerate(10)


