#!/usr/bin/python


#
# Welcome to you first programming lesson use this file to write python functions
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