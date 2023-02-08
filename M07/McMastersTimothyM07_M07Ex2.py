# Production worker clases *Note simililiar to Example One
# Timothy McMasters

class Employee:
    def __init__(self, employeeName, employeeNumber):
        self.employeeName = employeeName
        self.employeeNumber = employeeNumber
        
    def get_employeeName(self):
        return self.employeeName

    def get_employeeNumber(self):
        return self.employeeNumber
            # ^^^ Each return statemtn returns the different data atrributes when called. 
    
class ProductionWorker(Employee):
    def __init__(self, employeeName, employeeNumber, shiftNumber, hourlyPay):
        self.shiftNumber = shiftNumber
        self.hourlyPay = hourlyPay
        Employee.__init__(self, employeeName, employeeNumber)
        # ^^^This connects the subclass to the superclass.

    def get_shiftNumber(self):
        if self.shiftNumber.startswith('d'):
            self.shiftNumber = 1
            return self.shiftNumber
        else:
            self.shiftNumber = 2
            return self.shiftNumber
        #  ^^^^ This if statemnt is to differentiate between day and night shift and the set the shift number to the right number. 

    def get_hourlyPay(self):
        return self.hourlyPay

worker = ProductionWorker(input("What is the employee's name: "), input("Employee's number: "), input("Shift of employee?(eg. Day, Night): ").lower(), input("What is the employee's hourly pay? "))
# ^^^I take the input for every attribute of a production worker. Each new input starts on a new line. 

print(f"Employees name: {worker.get_employeeName()}\nEmployees number: {worker.get_employeeNumber()}\nEmployee's shift number: {worker.get_shiftNumber()}\nEmployee's hourly pay: ${worker.get_hourlyPay()}/hr")
# ^^^^^^ I use the f formating as this is the easiest way to format strings. Each attribute prints on a new line with \n.