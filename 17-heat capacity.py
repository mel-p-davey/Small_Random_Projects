Mass = float(input("Please enter the number of militers of water you are using:  "))
Change = float(input("Please enter the change in temperature you wish to see:    "))

HeatCapacity = 4.186

Energy = Mass*HeatCapacity*Change
print("That will take %d Joules of Energy" %Energy)

Kwatts = Energy/3600000

cost = Kwatts*8.9
print("That will cost %.2f dollars" % cost)

