

def tip_amount (bill_amount,tip_percentage):
	tip=bill_amount * tip_percentage * 0.01
	return tip

# # print tip_amount (100,10)

def total_bill (bill_amount, tip):
	total = bill_amount + tip
	return total 

# # print total_bill(100,tip_amount(100,10))

def split_bill(total_bill,people):
	split = total_bill/people
	return split

# # print split_bill (total_bill(200, tip_amount(200,20)), 5)

# print split_bill(total_bill(bill_amount,tip_amount (bill_amount,tip_percentage)),people)


def main(): 

	choice = int(raw_input ("Enter 1 if you want to Calculate Tip or Enter 2 to Split the bill"))

	if choice == 1 :
		bill_amount = int(raw_input("Enter bill amount"))
		tip_percentage = int(raw_input ("What is tip percentage"))
		print tip_amount(bill_amount,tip_percentage)
		tip=tip_amount(bill_amount,tip_percentage)
		print total_bill (bill_amount, tip)

		response = raw_input ("Would you like your bill split?")
		if response == "yes" :
			people = int(raw_input("how many ways do you want to split the bill?"))
			print split_bill(total_bill(bill_amount, tip),people)

	elif choice == 2:
			total_bill_amount = int(raw_input("Enter total bill amount"))
			people = int(raw_input("How many ways do you want to split the bill?"))

			print total_bill_amount/people

if __name__ == '__main__':
   main()


