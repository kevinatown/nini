# Python Notes

## Functions
* header - includes the 'def' keyword, the name of the function, and any parameters the function requires. Here's an example:
* optional comment - explains what the function does
* body - describes the procedures the function carries out. The body is indented, just like conditional statements.
* functions built into python
	def biggest_number(*args):
 		 print max(args)
  		return max(args)
	def smallest_number(*args):
		 print min(args)
  		return min(args)
	def distance_from_zero(arg):
 		 print abs(arg)
  		return abs(arg)

	biggest_number(-10, -5, 5, 10)
	smallest_number(-10, -5, 5, 10)
	distance_from_zero(-10)


## Commands
* `print"statement"` - python2
* `print("statement")` - python3
* % - modulo (returns remainder after division)
* `int()` - integer, if used on a floating point number, it will round the number down.
* `float()` - To preserve the decimal, use this
* `str()` - convert variables to a string
* `len()` - get length of a string
* `.lower()` - get rid of capital letters 
	- `variable.lower()`
* .`upper()` - capitalizes all characters in string
	- `variable.upper()`
* `.isalpha()` - checks to see if all characters are letters	
* `raw_input ()` - 
* `import` 
	- math - import the math modulo in Python
		- math.sqrt(n)
	- `from modulo import function` - import certain function from a modulo
	- `from modulo import *` - import all from the modulo
* `type()` - returns the type of data received by an argument

## Definitions 
* Strings - a series of letters, numbers, or symbols connected in order
	- print "This is a good string"
	- print 'You can use single quotes or double quotes for a string'
	- print "This is a" + "good string"
* Variables - define things that are subject to change
* float - A number with a decimal point
	- You can also define a float using scientific notation, with e indicating the power of 10
* boolean - only ever take one of two values. 
	- In Python, we define booleans using the keywords True and False
	-  A value of True corresponds to an integer value of 1, and will behave the same. A value of False corresponds to an integer value of 0.
* parameters - place holder variables
* arguments - inputs into a function

## Syntax 
* % - operator after the string is used to combine a string with variables
	- If you'd like to print a variable that is an integer, you can "pad" it with zeros using %02d. The 0 means "pad with zeros", the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative)
* Comparators
	- Note that == compares whether two things are equal, and = assigns a value to a variable
	- != - not equal to
	- < and > - less than and greater then
	- <= and >= - less than or eqaul to and greater than or equal to
* and, or, not
	- and, -  checks if both the statements are True;
    - or - checks if at least one of the statements is True;
    - not - gives the opposite of the statement.
* if - conditional statement that executes some specified code after checking if its expression is True.
	- else - complements the if statement. An if/else pair says: "If this expression is true, run this indented code block; otherwise, run this code after the else statement.
	- elif - "else if" otherwise, if the following expression is true, do this!

## Date and time

* from datetime import datetime - imports the datetime library so that we can use it.
* `print datetime.now()` - print out the current date and time.

## Questions
* Return vs print?
* 

