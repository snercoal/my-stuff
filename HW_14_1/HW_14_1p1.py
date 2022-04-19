import math;

initialCarbon = int(input("Enter the initial amount of carbon: "));
timeElapsed = int(input("Enter the amount of time: "));

constantA = ( (math.log(1/2) / 5730) );
calculate = ( (initialCarbon) * math.exp(constantA * timeElapsed));

for x in range(100, timeElapsed+1, 100):
    calculatee = ( (initialCarbon) * math.exp(constantA * x))
    print("After " +str(x)+ " years, the amount of Carbon-14 will be: " +str(calculatee));