class PayrollDeduction:

    def __init__(self, description, date, charge_amount, employeeID):
        self.__description = description
        self.__date = date
        self.__charge_amount = charge_amount
        self.__employeeID = employeeID

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge_amount(self):
        return self.__charge_amount

    def get_employeeID(self):
        return self.__employeeID
    
    
    def print_NetPay(self):
        #net_pay = self.__monthly_salary - self.__charge_amount
        #net_pay = self.__monthly_salary - self.__charge_amount
        print("Net Pay:",self.__charge_amount)
    