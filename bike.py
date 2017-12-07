class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "the price of the bike is " + str(self.price) + " the maximum speed of the bike is " + str(self.max_speed) + " total mileage is " + str(self.miles)
        return self
    def ride(self):
        self.miles = self.miles + 10
        print "we are riding and the speed is " + str(self.miles)
        return self
    def reverse(self):
        self.miles = self.miles - 5
        if self.miles <= 0:
            self.miles = 0
        print "we are taking a reverse and the speed is " + str(self.miles)
        return self




bike1 = Bike(200,"25mph",0)
bike2 = Bike(300,"35mph",0)
bike3 = Bike(500,"50mph",0)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
