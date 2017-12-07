class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def tax(self, tax):
        self.price = (self.price * (tax/100)) + self.price
        return self.price

    def item_return(self,state):
        if state == "defective":
            self.status = "defective"
            self.price = 0
        elif state == "like new":
            self.status = "new"
            self.price = self.price
            self.status = "For Sale"
        elif state == "used":
            self.status = "used"
            self.price = .80 * self.price
        else:
            print "please select a valid reason"
        return self

    def display_info(self):
        print "Price: ", self.price
        print "Name: ", self.name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status
        return self

prod1 = Product(5,"cap","1lb","Nike")
prod2 = Product(100,"bag","3lb","Addidas")
prod3 = Product(500,"mobile phone","2lb","apple")

prod1.display_info()
prod1.tax(10.)
prod1.sell().display_info()
prod1.item_return("used").display_info()

prod2.display_info()
prod2.tax(8.)
prod2.item_return("like new").display_info()

prod3.tax(8.)
prod3.display_info()
