class Employee:

    def __init__(self, name, IDnumber, department, job_title, monthly_salary):
        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__job_title = job_title
        self.__monthly_salary = monthly_salary

    def get_name(self):
        return self.__name

    def get_IDnumber(self):
        return self.__IDnumber

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def get_monthly_salary(self):
        return self.__monthly_salary

    def print_Employee(self):
        print("*** Employee Pay ***")
        print("Name:", self.__name)
        print("ID Number:",self.__IDnumber)
        print("Department:",self.__department)
        print("Gross Pay:", self.__monthly_salary)
        #print("")

'''
class PayrollDeducation(Employee):

    def __init__(self, description, date, charge_amount, employeeID):
        Employee.__init__(self, name, IDnumber, department, job_title, monthly_salary)
        self.__description = description
        self.__date = date
        self.__charge_amount = charge_amount
        self.__employeeID = employeeID

    def print_PayrollDeduction(self):
        net_pay = self.__monthly_salary - self.__charge_amount
        print("Net Pay:",net_pay)
'''