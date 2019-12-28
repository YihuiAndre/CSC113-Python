##Name: Yihui A. Wuchen
##Session: Afternoon2
##11300–InclassAssignment2

import math

##Part A
##float???
def min_to_millisecond(a):
	return str(a*60000)
a = float(input("Enter minutes: "))
print("There are ", min_to_millisecond(a), "millisecond in ", a, "minutes")

##Answer: if user input 4 minutes, it will return 240000.0 millisecond
##Answer: if user input 10 minutes, it will return 600000.0 millisecond

print("-----------------------------------------------------")

##Part B
def average_of_two_score(a, b):
	return str((a+b)/2)
a = float(input("Enter one exam scores: "))
b = float(input("Enter another exam scores: "))
print("The average of two exam scores are", average_of_two_score(a, b),)

##Answer: if user input two scores: 10 and 10, it will return the average of the scores as 10.0
##Answer: if user input two scores: 50 and 30, it will return the average of the scores as 40.0

##Part C
def root(a, b, c):
	root_one = (-b+math.sqrt(b**2-4*a*c))/(2*a)
	root_two = (-b-math.sqrt(b**2-4*a*c))/(2*a)
	return root_one, root_two
a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))
root_one, root_two = root(a,b,c)
print("the roots of the quatratic equation is", root_one, "and", root_two)

##Answer: if user input a as 1, b as 5 and c as 6, it will return two roots: -2.0 and -3.0
##Answer: if user input a as 1, b as -3 and c as 2, it will return two roots: 2.0 and 1.0

#Part D
def Kelvin_to_Reaumur(a):
	return (a-273.15)*0.8
def Kelvin_to_Celsius(c):
	return Kelvin_to_Reaumur(c)*1.25
a = float(input("Enter Kelvin: "))
print(a, "Kelvin is equal to ", Kelvin_to_Celsius(a), "Celsius")

##Answer: if user input Kelvin as 13, it will return Celsius as -260.15
##Answer: if user input Kelvin as 200, it will return Celsius as -73.14999999999998

'''
#Part E
This one I got wrong
def marbles_fit_in_cube(n):
	square_volume = n**3
	return int(square_volume/((n/4)**3))
a = int(input("enter square side: "))
print("There are ", marbles_fit_in_cube(a), "marbles in the cube")
##Answer: if user input side of square as 2, it will return number as 64
##Answer: if user input side of square as 5, it will return number as 64
'''

#Part F
def print_i():
	print ("i	 i	  i	   i	    i")
def print_top():
	print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
def combine():
	print_top()
	print_i()
	print_i()
	print_i()
	print_i()

def print_graph():
	combine()
	combine()
	combine()
	combine()
	print_top()	

print_graph()

