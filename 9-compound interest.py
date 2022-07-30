invested_amount = float(input("Please enter your intital investment:  "))
term = int(input("Please enter how many years you will keep your investment in the bank:  "))
total = invested_amount

for i in range(term):
    total = total*1.04

print("%.2f" %total)


