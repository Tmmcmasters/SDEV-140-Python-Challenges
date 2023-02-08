# UNDERSTANDING CLASSES
# Timothy McMasters
class Person:
    def __init__(self, name, address, tele):
        self.name = name
        self.address = address
        self.tele = tele

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address

    def get_tele(self):
        return self.tele

        # I use get so that I can print each attribute if I want to later. 

class Customer(Person):
    def __init__(self, name, address, tele, customerNumber, mailingList):
        self.customerNumber = customerNumber
        self.mailingList = mailingList
        Person.__init__(self, name, address, tele)
        # ^^^^ This calls the super class
        
    def get_customerNumber(self):
            if self.mailingList.startswith('y'): #I use startswith to make typing erros less likely
                self.mailingList = True
                return self.mailingList
            elif self.mailingList.startswith('n'):
                self.mailingList == False
                return self.mailingList
            else:
                print("They did not reply yes or no.")
                self.mailingList = False
                return self.mailingList
    
    def get_mailingList(self):
        return self.mailingList

    

customer1 = Customer(input("Your name: "), input("Your address: "), input("Your telephone number: "), input("The customer number: "), input("Would you like to be on the mailingList?(eg. Yes, No): ").lower()) # I user lower so that it ensures my later if statement will work. 
print(customer1.get_name())
print(customer1.get_customerNumber())

# I take the input and then print one from each including the customer number which has an if statement. 



