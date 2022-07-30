TotItem = float(input("Please enter how much the item costs:  "))
TotGiven = float(input("Please enter the cash you are paying with:  "))

change = float(TotGiven - TotItem)

cents = change*100

onehunbill = 10000
fiftybill = 5000
twentybill = 2000
tenbill = 1000
fivebill = 500
toonie = 200
loonie = 100
quarter = 25
dime = 10
nickle = 5
penny = 1


Bill_100 = int(cents//onehunbill)
cents = cents-(Bill_100*onehunbill)

Bill_50 = int(cents//fiftybill)
cents = cents-(Bill_50*fiftybill)

Bill_20 = int(cents//twentybill)
cents = cents-(Bill_20*twentybill)

Bill_10 = int(cents//tenbill)
cents = cents-(Bill_10*tenbill)

Bill_5 = int(cents//fivebill)
cents = cents-(Bill_5*fivebill)

Coin_2 = int(cents//toonie)
cents = cents - (Coin_2*toonie)

Coin_1 = int(cents//loonie)
cents = cents - (Coin_1*loonie)

QuarterCoin = int(cents//quarter)
cents = cents - (QuarterCoin*quarter)

DimeCoin = int(cents//dime)
cents = cents - (DimeCoin*dime)

NickleCoin = int(cents//nickle)
cents = cents - (NickleCoin*nickle)

PennyCoin = int(cents//penny)
cents = cents - (PennyCoin*penny)

print("Give back: \n", Bill_100, "One Hundred Dollar Bill\n", Bill_50, "Fifty Dollar Bill\n", Bill_20, "Twenty Dollar Bill\n", Bill_10, 
"Ten Dollar Bill\n", Bill_5, "Five Dollar Bill\n", Coin_2,"Toonie\n", Coin_1, "Loonie\n", QuarterCoin,"Quarters\n", DimeCoin, "Dimes\n", 
NickleCoin, "Nickles\n", PennyCoin, "Pennies" )

