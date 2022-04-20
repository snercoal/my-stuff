import math;

initialCarbon = int(input("Enter the initial amount of carbon: "));
timeElapsed = int(input("Enter the amount of time: "));

constantA = ( (math.log(1/2) / 5730) );
currentCarbon = ( (initialCarbon) * math.exp(constantA * timeElapsed));

for year in range(100, timeElapsed+1, 100):
    currentCarbon = ( (initialCarbon) * math.exp(constantA * year))
    print("After " +str(year)+ " years, the amount of Carbon-14 will be: " +str(currentCarbon));