import EmployeeClass as ec
import PayrollDeductionClass as pd

def main():

    #EmployeeClass interaction
    name = "Jimmy Smith"
    IDnumber = "58475"
    department = "Information Systems"
    job_title = "Developer"
    monthly_salary = 6800

    Employee1 = ec.Employee(name,IDnumber,department,job_title,monthly_salary)

    Employee1.print_Employee()

    #PayrollDeductionClass interaction
    description1 = "food court"
    date1 = "8/14/2022"
    charge_amount1 = 22.50
    employeeID1 = 39119

    description2 = "gift contribution"
    date2 = "8/12/2022"
    charge_amount2 = 25.00
    employeeID2 = 58475

    description3 = "food court"
    date3 = "8/17/2022"
    charge_amount3 = 15.25
    employeeID3 = 21547

    description4 = "vending machine"
    date4 = "8/22/2022"
    charge_amount4 = 3.00
    employeeID4 = 58475

    description5 = "vending machine"
    date5 = "8/5/2022"
    charge_amount5 = 2.75
    employeeID5 = 58475

    OVRcharge_amount = charge_amount2+charge_amount4+charge_amount5

    net_pay = monthly_salary - OVRcharge_amount

    PayrollDeduction1 = pd.PayrollDeduction(description1, date1, charge_amount1, employeeID1)
    PayrollDeduction2 = pd.PayrollDeduction(description2, date2, charge_amount2, employeeID2)
    PayrollDeduction3 = pd.PayrollDeduction(description3, date3, charge_amount3, employeeID3)
    PayrollDeduction4 = pd.PayrollDeduction(description4, date4, charge_amount4, employeeID4)
    PayrollDeduction5 = pd.PayrollDeduction(description5, date5, charge_amount5, employeeID5)
    #overall deduction:
    PayrollDeduction = pd.PayrollDeduction(description1, date1, net_pay, employeeID1)
    PayrollDeduction.print_NetPay()

    #print()
    #print()
    #print()

main()