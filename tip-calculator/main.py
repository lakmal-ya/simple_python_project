#If the bill was 150.00, split between 5 people, with 12% tip
#Each person should pay (150.00/5) * 1.12
#Round the resualt to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, r 15? "))
num_people = int(input("Number of people you want split the bill? "))

#First we will calculate the tip as percentage
tip_as_percent = tip/100

#Then calculate total tip amount from the bill
total_tip_ammount = total_bill * tip_as_percent

# Then add to total tip amount to bill
total_bill_before_round = total_bill + total_tip_ammount

# Then devid number of people
each_person_pay = total_bill_before_round/num_people

#Then each person will floting point number we will used round function for round up the number
final_amount = round(each_person_pay, 2)

# Then add two decimal point for round number using format 
final_amount = "{:.2f}".format(final_amount)

# Print out the value each person should pay
print(f"Each person should pay : ${final_amount}")