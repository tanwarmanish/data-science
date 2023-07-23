run = "ques2"


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
