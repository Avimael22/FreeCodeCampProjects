
def main():
    answer = "yes"
    while answer == "yes":
        name = input("what is your name: ")
        total_hours = float(input("How many hours did you work this week? "))
        hourly_rate = float(input("what is your hourly rate? "))
        social_security_number = input("Social number: ")
        current_loan_balance = float(input("Current loan balance? "))
        loan_deductions = float(input("loan deductions? "))
        new_balance = current_loan_balance - loan_deductions
        gross_wage, tax, personal_relief, tips, holiday, overtime = income_tax(total_hours, hourly_rate)
        employeeContribution, employerContribution, percentage_employee, percentage_employer = employee_contributions(gross_wage)
        net_salary = gross_wage - (employeeContribution + tax) - loan_deductions
        pay_period = "Dec 4th - Dec 10th, 2023"
        with open("./pay_slips_2023/December_2023/Week1.txt", "a") as week3:
            print("", file=week3)
            print("%-22s %s" %("PAY SLIP", "Weezie's Oceanfront Hotel and Garden Cottages"), file=week3)
            print("%-14s %-25s %s" %(f"SSN: {social_security_number}", f"Name: {name}", f"{pay_period}"), file=week3)
            print("", file=week3)
            print("%-20s %-20s %-20s %-s" %("Total Hours", "Holiday","tips", "Over time"), file=week3)
            print("", file=week3)
            print("%-20s %-20s %-20s %-s" %(f"{total_hours}", f"${holiday: .2f}",f"${tips: .2f}", f"${overtime: .2f}"), file=week3)
            print("", file=week3)
            print("%-55s %s" %("Your take home salary was based on:", f"Loan"), file=week3)
            print("%-20s %-30s %s" %(f"Gross wage:", f"${gross_wage: .2f}", f"Loan balance: {current_loan_balance}"), file=week3)
            print("%-20s %-30s %s" %(f"Social:", f"-${employeeContribution: .2f}", f"Loan deductions: {loan_deductions}"), file=week3)
            print("%-20s %-30s %s" %(f"tax:", f"-${ tax: .2f}", f"New balance: {new_balance}"), file=week3)
            print("", file=week3)
            print("%-20s %-20s %s"%(f"Net Salary:", f"${net_salary: .2f}", "Received by: ____________"), file=week3)
            print("", file=week3)
            print("_______________________________", file=week3)
           
           
        answer = input("Do you wish to continue? ")


def income_tax(total_hours, hourly_rate):
    hours_per_week = 45
    tax_rate = .25
    weeks_in_year = 52
    tax_credit = 100
    overtime = total_hours - hours_per_week
    holiday = float(input("Holiday extra? "))
    tips = float(input("Any tips/service charge? "))
    overtime_pay = (overtime*hourly_rate*1.5)
    gross_wage = (hours_per_week*hourly_rate) + overtime_pay + holiday + tips
    if total_hours < 45:
        overtime = 0
        overtime_pay = 0
        gross_wage = (total_hours*hourly_rate) + overtime_pay + holiday + tips
    if gross_wage >= 557.69:
        personal_relief = 19600
        withheld = (((((gross_wage*weeks_in_year)-personal_relief)* tax_rate) - tax_credit)/weeks_in_year)
    elif gross_wage >= 519.23:
        personal_relief = 22600
        withheld = (((((gross_wage*weeks_in_year)-personal_relief)* tax_rate) - tax_credit)/weeks_in_year)
    elif gross_wage >= 500:
        personal_relief = 24600
        withheld = (((((gross_wage*weeks_in_year)-personal_relief)* tax_rate) - tax_credit)/weeks_in_year)
    else:
        personal_relief = 25600
        withheld = 0
    return gross_wage, withheld, personal_relief, tips, holiday, overtime_pay

def employee_contributions(gross_wage):
    emloyer_rate_of_contribution = 0
    employee_rate_of_contribution = 0
    if gross_wage >= 500:
        employer_rate_of_contribution = .055
        employee_rate_of_contribution = .045
        weekly_insurable_earning = 520
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 460:
        employer_rate_of_contribution = .0565
        employee_rate_of_contribution = .0435
        weekly_insurable_earning = 480
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 420:
        employer_rate_of_contribution = .0581
        employee_rate_of_contribution = .0419 
        weekly_insurable_earning = 440
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 380:
        employer_rate_of_contribution = .0596
        employee_rate_of_contribution = .0404
        weekly_insurable_earning = 400
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 340:
        employer_rate_of_contribution = .0612
        employee_rate_of_contribution = .0388
        weekly_insurable_earning = 360
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 300:
        employer_rate_of_contribution = .0627
        employee_rate_of_contribution = .0373
        weekly_insurable_earning = 320
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 260:
        employer_rate_of_contribution = .0645
        employee_rate_of_contribution = .0355
        weekly_insurable_earning = 280
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 220:
        employer_rate_of_contribution = .0669
        employee_rate_of_contribution = .0331
        weekly_insurable_earning = 240
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 180:
        employer_rate_of_contribution = .0703
        employee_rate_of_contribution = .0297
        weekly_insurable_earning = 200
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 140:
        employer_rate_of_contribution = .0754
        employee_rate_of_contribution = .0246
        weekly_insurable_earning = 160
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 110:
        employer_rate_of_contribution = .0813
        employee_rate_of_contribution = .0188
        weekly_insurable_earning = 130
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    elif gross_wage >= 70:
        employer_rate_of_contribution = .0813
        employee_rate_of_contribution = .0188
        weekly_insurable_earning = 90
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    else:
        employer_rate_of_contribution = .0813
        employee_rate_of_contribution = .0188
        weekly_insurable_earning = 55
        employee_contribution = weekly_insurable_earning * employee_rate_of_contribution
        employer_contribution = weekly_insurable_earning*employer_rate_of_contribution
    return employee_contribution, employer_contribution, employee_rate_of_contribution, employer_rate_of_contribution
    

main()