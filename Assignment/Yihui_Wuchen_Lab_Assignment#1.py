##Name: Yihui A. Wuchen
##Session: Afternoon2
##11300–InclassAssignment1

import math

##Part A
print("There are", 42*60 + 42, "seconds.")
##Answer: 2562 Seconds

print("-----------------------------------------------------")

##Part B
print("The volume of a sphere with radius 4 is", 4/3*math.pi*4**3)
#Answer: 268.082573106329
print("The volume of a sphere with radius 6 is", 4/3*math.pi*6**3)
#Answer: 904.7786842338603

print("-----------------------------------------------------")

#Part C
print("If the temperature of Celsius is -40, then the temperature of Fahrenheit is", (-40*9/5)+32)
#Answer: -40.0
print("If the temperature of Fahrenheit is -40, then the temperature of Celsius is", (-40-32)*5/9)
#Answer: -40.0

print("-----------------------------------------------------")

#Part D
a = int(input("Enter the side length of the cube? "))
print("There are", int((a*2*a*3*a)/(a**3)), "cubes C in rectangular prism R.")
#Answer: 6
