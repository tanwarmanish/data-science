
#### Why Python
- Design Philosophy
- Batteries Included 
- General Purpose
- Libraries/Community

#### Why Python for Data Science
- Easy to learn
- Proximity with Maths
- Community

<hr>

### Input
- The `input()` function pauses program execution to allow the user to type in a line of input from the keyboard. 
- Once the user presses the Enter key, all characters typed are read and returned as a string
``` python
user_input = input("What is your name?")
print(user_input)
```

#### Output
- You can display program data to the console in Python with `print()`.
- To display objects to the console, pass them as a comma-separated list of arguments to `print()`.
``` python
print(<obj1>, <obj2>, <obj3>, ..., sep="-",end="\n")
# obj1-obj2-obj3... <Next Line>
```


<hr>

#### Data Types

##### 1. Number
``` python
print(8)
# 1*10^308
print(1e309)
```

##### 2. Decimal/Float
``` python
print(8.55)
print(1.7e309)
```

##### 3. Boolean
``` python
print(True)
print(False)
```

##### 4. String
``` python
print("Hello World")
```

##### 5. Complex
``` python
print(5+6j)
```

##### 6. List
``` python
print([1,2,3,4,5,6])
```

##### 7. Tuple
``` python
print((1,2,3,4,5,6))
```

##### 8. Sets
``` python
print({1,2,3,4,5})
```

##### 9. Dictionary
``` python
print({'name':'Manish Tanwar', id:101})
```


##### type
``` python
a = True
type(a) # returns Boolean 
```

<hr>

``` python

# Dynamic Typing
a = 5

# Static Typeing
int a = 5;

```

``` python

# Dynamic Binding
a = 5
print(a)
a = "Manish"
print(a)

# Static Binding
int a = 5
# cant be changed to some other variable now
```

``` python

a,b,c = 1,2,3

a = b = c = 5
```


##### Comments
``` python

# single line comment

# ```
 Mutli 
 line 
 comment
 Ignore the # here
# ```
```

<hr>

##### Keywords
- Reserved words are called keywords e.g. for, if etc.
- Keywords should not be used as an Identifier

##### Identifiers
- Variable, function & class names are called identifiers
- Rules:
	- Should not start with a digit
	- Only lowercase, uppercase, digits and "_"  can be used.
	- Cannot be keywords

<hr>

##### Input
``` python
# Static vs Dynamic
input("Message Here")

value = input("Input Here...")
# all inputs are in string
# need to be converted explicitly
```

##### Type Conversion
- Two types :
	- Implicit Type Conversion ( Done automatically by Python )
	- Explicit Type Conversion ( Done by user )

##### Explicit Type Conversion
``` python
# int
int("4.5")
#4

# float
float(4)
# 4.0

```


##### Literals
- Value stored in a variable is called literal.
``` python
a = 0b1010 # binary literal
b = 100    # decimal literal
c = 0o310  # octal literal
d = 0x12   # hexadecimal literal
e = 3.14j  # complex literal


# float literal
f = 10.5
g = 1.5e2  # 1.5 * 10^2
h = 1.5e-3 # 1.5 * 10^(-3)

# complex literal
i = 2 + 5j
print(i.real, i.imag) # (2, 5)
```

##### Strings
``` python
string1 = 'This is Python'
string2 = "This is Python"
char = "C"
multilineString = """ This is a multiline string """
unicode = u"U0001f600"
rawString = r"Raw \t String"
```


``` python
# Misc

a = True + 4   # 5
b = False + 10 # 10
```

##### None
- Similar to null in javascript.
- Python don't allow us to declare a variable without initialising it.

``` 
# It is a special type
# Similar to null in javascript
# It means variable type is nothing
a = None
a # var cannot be declared like this
```



 




