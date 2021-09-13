first_name = str(input("Enter first name: "))
last_name = str(input("Enter last name: "))
print(f"{first_name} {last_name}")

amount = int(input("Enter your starting capital: "))
increase = int(input("Enter your yearly interest in percentage/%: "))

years = int(input("How many years? "))

real_increase = (increase / 100) + 1 

total_amount = amount * real_increase ** years
print("Your interest after " + str(years) + " years is: " + str(total_amount))