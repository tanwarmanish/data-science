import math


run = "ques4"


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
