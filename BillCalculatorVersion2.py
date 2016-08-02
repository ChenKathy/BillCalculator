tip_amount = 0
total_bill = 0
split_number = 0

def calculate_bill(original_bill_amount,tip_percentage=18,split_number=1):
	 global tip_amount
	 tip_amount=original_bill_amount * tip_percentage * 0.01
	

	 global total_bill 
	 total_bill = original_bill_amount + tip_amount
	

	 global split_amount
	 split_number = total_bill/split_number
	 return split_number

print calculate_bill(100)
print calculate_bill(100,20)
print calculate_bill(100,20,3)
print calculate_bill(100,split_number=3)