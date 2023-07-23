import math


run = "ques9"

"""
### Q1 :- Print the given strings as per stated format.

**Given strings**:
```
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
```
**Output**:
```
Data-Science-Mentorship-Program-started-By-CampusX
```
Concept- [Seperator and End]
"""

if run=="ques1":
    print("Data","Science","Mentorship","Program",sep="-",end="-")
    print("By",'CampusX',sep="-",)



# Q2:- Write a program that will convert celsius value to fahrenheit.
if run=="ques2":
    # (0°C × 9/5) + 32 = 32°F
		temperatureF = 33;
		temperatureC = (temperatureF*9)/5 + 32
		print(temperatureC)


"""
Q3:- Take 2 numbers as input from the user.
Write a program to swap the numbers without using any special python syntax.
"""
if run=="ques3":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    number3 = number2
    number2 = number1
    number1 = number3
    print([number1,number2])


# Q4:- Write a program to find the euclidean distance between two coordinates.
# Take both the coordinates from the user as input.
if run=="ques4":
  x1,y1 = [int(x) for x in input("Enter first coordinate: ").split(" ")]
  x2,y2 = [int(x) for x in input("Enter second coordinate: ").split(" ")]
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  print(distance)


# Ques 5 Write a program to find the simple interest 
# when the value of principle,rate of interest and time period is provided by the user.
if run=="ques5": 
  principle = int(input("Enter principle amount: "))
  roi = int(input("Enter rate of interest: "))
  timePeriod = int(input("Enter time period: "))
  simpleInterest = (principle * roi * timePeriod)/100
  print(simpleInterest,simpleInterest+principle)


# Q6:- Write a program that will tell the number of dogs and chicken are there 
# when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2
if run=="ques6":
      heads = 4
      legs = 18
      chicken = heads
      legs -= heads*2
      dogs = int(legs/2)
      chicken -= dogs
      print(f"Dogs:{dogs}, Chicken:{chicken}")
        

# Ques 7: Write a program to find the sum of squares of first n natural numbers 
# where n will be provided by the user.     
if run=="ques7":
  number = int(input("Enter a number: "))
  total = 0
  for i in range(1,number):
       total += i**2
  print(total)


 # Ques 8: Given the first 2 terms of an Arithmetic Series.
 # Find the Nth term of the series. Assume all inputs are provided by the user
if run=="ques8":
  first = int(input("Enter first term: "))
  second = int(input("Enter second term: "))
  n = int(input("Enter term to calculate: "))
  d = second-first
  termN = first + (n-1)*d
  print(termN)


# Q9:- Given 2 fractions, find the sum of those 2 fractions.
# Take the numerator and denominator values of the fractions from the user.
if run=="ques9":
    firstN,firstD = [int(x) for x in input("Enter first fraction: ").split(" ")]
    secondN,secondD = [int(x) for x in input("Enter second fraction: ").split(" ")]
    total = firstN/firstD + secondN/secondD
    print(total)