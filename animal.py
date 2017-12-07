class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def display_health(self):
        print "the health of the "+ self.name + " is " + str(self.health)
        return self

# animal1 = Animal("animal1")
# animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
    def display_health(self):
        print "I am a Dragon"
        super(Dragon,self).display_health()


dog1 = Dog("dog1")
dog1.walk().walk().walk().run().run().pet().display_health()

dragon1 = Dragon("dragon1")
dragon1.display_health()
dragon1.fly()
dragon1.display_health()
