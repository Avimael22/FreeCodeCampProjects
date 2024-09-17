def main():
    print("Welcome to our loan calculator")
    loan_amount = input("What is the loan amount you intend to apply for? ")
    principal = int(loan_amount)
    loan_period = int(input("in how many months do you intend to pay off the loan"))
    applied_interest = contractual_interest_rate()
    monthly_installment = monthly_payment()
    installment_count = 1

    print("Installment principal interest total principal balance")

    while installment_count <= loan_period:
        effective_installment_interest = principal*applied_interest
        principal_contribution = monthly_installment-effective_installment_interest
        principal_balance = principal - principal_contribution

        print(f"{installment_count} {principal_contribution} {effective_installment_interest} {monthly_installment} {principal_balance}")
        principal -= principal_contribution
        installment_count += 1
        





def monthly_payment():
    weekly_salary = input("What is your weekly salary? ")
    monthly_salary = int(weekly_salary) * 4
    monthly_installment = monthly_salary *.33 #your loan installment cant be more than 33% of your monthly net salary
    return monthly_installment

def contractual_interest_rate():
    yearly_interest_rate = input("what is the yearly interest rate? Enter a number: ")
    monthly_interst_rate = (float(yearly_interest_rate)/12)/100
    return  monthly_interst_rate

main()