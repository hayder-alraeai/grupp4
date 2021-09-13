first_name = "Bernard"
last_name = "Bruna"
print(f"{first_name} {last_name}")

amount = 100 # befintlig summa
increase = 1.2 # ökningen 
total = amount * increase ** 99 # uträkning samt antal år
print (total) # här skrivs variabeln "total" ut

years = int(input("How many years?"))

total_amount = amount * increase ** years
print(total_amount)
