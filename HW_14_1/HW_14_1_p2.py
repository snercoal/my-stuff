dailyDeposit = float(input("Enter the amount of your daily deposit: "));
interestRate = ((float(input("Enter your interest rate: "))) / 100);
desiredBal = float(input("Enter your desired final Balance: "));
currentBal = 0;
day = 0;
while(currentBal < desiredBal):
    currentBal = (currentBal + (currentBal * interestRate) + dailyDeposit);
    day += 16;
finalBal = round(currentBal, 2)
years = (day / 365);
print("Your Balance of " + str(finalBal) + " will be reached in " + str(round(years, 3)) + " years");


