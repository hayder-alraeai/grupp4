first_name= str(input("Please enter your first name: "))
last_name=str(input ("Please enter your last name: "))
print(f"{first_name} {last_name}" )

print("Welcome! " + first_name + " " + last_name)

goal=str(input("What are you saving money for? "))
price= int(input( "What's the price for " + goal + "? "))


starting_capital=int(input("Put in your starting capital: "))
monthly_input=int(input("How much will you be saving monthly: "))
yearly_interest=int(input("How much percent do you expect to get in return yearly: "))

yearly_input= monthly_input * 12

total_years= float (price / starting_capital+yearly_input * yearly_interest)

print("It will take you ")+ total_years+ (" to get to your goal!" )