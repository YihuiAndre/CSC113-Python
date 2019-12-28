##Name: Yihui A. Wuchen
##Session: Afternoon2
##11300–InclassAssignment3

#Q1

try:
    num = int(input("Enter a number: "))
    total = 0
    for i in range(1,num):
            if num % i == 0:
                    total += i
    if total == num and num != 0:
            print("perfect number")
    else:
            print("not perfect number")
except ValueError:
	print("Invaild Input!")
except:
	print("Error happend")
print("---------------------------------------------------")

#Q2

try:
    while input("Press q to Exit, otherwise press any keys ") != "q":
        num =int(input("Enter number: "))
        print("All positive integer divisor of", num ,"are:", end=" ")
        if num < 0:
            num = -num
        for k in range(1 , num+1):
            if num % k == 0:
                print(k, end = " ")
        print("\n")

except ValueError:
    print("Invaild Input!")
except:
    print("Error happend")

print("---------------------------------------------------")

#Q3

try:
    while input("Press q to Exit, otherwise press any keys ") != "q":
        x1, y1 = [int(x) for x in input("enter first coordinate x1 and y1 (seperate with space): ").split()]
        x2, y2 = [int(x) for x in input("enter second coordinate x2 and y2 (seperate with space): ").split()]
        x3, y3 = [int(x) for x in input("enter third coordinate x3 and y3 (seperate with space): ").split()]
        if(abs((x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1)/2) != 0):
            print("can form a triangle")
        else:
            print("It can't form a triangle")
except ValueError:
    print("Invaild Input!")
except:
    print("Error happend")

print("---------------------------------------------------")

#Q4

try:
    while input("Press q to Exit, otherwise press any keys ") != "q":
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        if a > b:
            tmp = a
            a = b
            b = tmp
        for k in range(a , b+1):
            if k >= 2:
                isprime = True
                for n in range(2,k):
                    if k % n == 0:
                        isprime = False
                        break
                if isprime:
                    print(k, end = " ")
        print("")
except ValueError:
    print("Invaild Input!")
except:
    print("Error happend")

print("---------------------------------------------------")

#Q5

def factorial(x):
    total = 1
    for i in range(2, x+1):
        total *= i
    return total

try:
    while input("Press q to Exit, otherwise press any keys ") != "q":
        a = int(input("number of people: "))
        b = int(input("number of people can seat on the table: "))
        if a < b:
            print("There is 1 way to seat on the table")
        else:
            print("There are" , int(factorial(a)/(factorial(b)*factorial(a-b))), "way to seat on the table" )
except ValueError:
    print("Invaild Input!")
except:
    print("Error happend")

