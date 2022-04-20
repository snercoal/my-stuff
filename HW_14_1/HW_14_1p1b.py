import math;

initialCarbon = int(input("Enter the initial amount of carbon: "));
desiredCarbon = float((input("Enter the desored amount of carbon: ")));
constantA = ( (math.log(1/2) / 5730) );

year = 0;
currentCarbon = initialCarbon;

while(currentCarbon > desiredCarbon):
    currentCarbon = ( (initialCarbon) * math.exp(constantA * year));
    if(desiredCarbon > currentCarbon):
        print("C(t) = " + str(currentCarbon) + " and the years passed = " + str(year));
        break
    if(year % 100 == 0):
        print("The expected amount of Carbon-14 at year: " + str(int(year)) + " is: " + str(currentCarbon));
    year += 100;