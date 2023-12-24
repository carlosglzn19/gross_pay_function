# Function to calculate the gross pay
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    elif hours > 40:
        pay = rate * 40 + (rate * 1.5 * (hours - 40))
        return pay

#Input function to ask for the hours and rates    
hours_input = input("Enter Hours: ")
hours = float(hours_input)

rate_input = input("Enter rate: ")
rate = float(rate_input)

# Invoking the function
gross_pay = computepay(hours, rate)

# Printing the result
print("Pay", gross_pay)