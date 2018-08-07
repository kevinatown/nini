#!/usr/bin/python


#
# Welcome to your first programming lesson use this file to write python functions
#

def onePlusOne():
  #add comments
  # do work
  return 1 + 1

def stringToInts(array):
  """
  Takes an array, convets all potential ints
  
  Arguments: 
  array -- list of items

  Returns:
  an array with all items as ints, and none ints removes
  """
  returnArray = []
  for item in array:
    # this is a simple for loop, python makes it easy to iterate over each item in a list
    try:
      # this is a try catch statement, dont worry about it now
      num = int(item)
      returnArray.append(num)
    except ValueError:
      print('%s is not an int' % item)
  return returnArray

def removeDuplicates(array):
  """
  Removes duplicates from a list

  Arguments: 
  array -- list of items

  Returns:
  an array with duplicates removed
  """
  pass

def sumArray(array):
  """
    Takes an array of numbers and sums it.
    
    Arguments:
    array -- list of ints
    
    Returns:
    sum -- int
  """
  pass



def main():
  """main function put your other functions in here so that you can run this as a script"""
  
  returnVal = onePlusOne()
  print returnVal

  l0 = ['1', 2, 'three', '6']
  l0n = stringToInts(l0)

  # expected [1, 2, 6] and 9
  print(l0n, sum(l0n))

  # create other test cases
  l1 = [1, 2, 3, 4, 5, 6]
  r1 = sumArray(l1)
  # I expect this to be 21
  print(r1)

  r2 = sum(l1)
  validate1 = r2 == r1

  # expected 21, true
  print(r2, validate1)

  # removing duplicates, write test cases here


# dont worry about this yet
if __name__ == '__main__':
  main()


# Grade converter
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade < 70 and grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print "92 = " + grade_converter(92)

# This should print a "C"
print "70 = " + grade_converter(70)

# This should print an "F"
print "61 = " + grade_converter(61)


# What's your name
name = raw_input ("What's your name?")
if len (name) > 0:
  print "Hello, " + name + "!"
else:
  print "You didn't tell me your name."


# Pig Latin Translator
print 'Welcome to the Pig Latin Translator!'

pyg = "ay"
original = raw_input("Enter a word: ") 

if len(original) > 0 and original.isalpha(): 
  #checks if all character are letters
  word = original.lower() 
    # changes all characters to lowercase
  first = word[0] 
    # sets variable first to be first letter of word
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)] 
    # sets new_word to leave out first letter
  print original + " in Pig Latin is " + new_word

else:
  original_2 = raw_input("Please try again. Do not include any spaces or numbers: ") 

  if len(original_2) > 0 and original_2.isalpha(): 
    #checks if all character are letters
    word = original_2.lower() 
      # changes all characters to lowercase
    first = word[0] 
      # sets variable first to be first letter of word
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)] 
      # sets new_word to leave out first letter
    print original_2 + " in Pig Latin is " + new_word

 # I'd like to create a loop so they could continue to input words
  else:
    print "Fine. Don't listen to me. Good bye."




