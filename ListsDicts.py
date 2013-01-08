#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show usage of lists and dicts"

# This line must be at the beginning of the file
from __future__ import print_function

import sys

def ReverseSort( a, b ):
  return b-a
  
def Lists():
  print( 'Lists' )

  list = []
  
  list.append( 1 )
  list.append( 3 )
  list.append( 2 )
  
  print( 'sorted:', sorted(list) )
  print( 'elements:', list )
  list.sort()
  print( 'sorted in place:', list )

  other = [ 10, 40, 30, 80, 50, 60, 20 ]
  print( "Whole list [len="+str(len(other))+"]", other )
  print( "First three elements of the list", other[:3] )
  print( "Last two elements of the list", other[-2:] )
  print( "From the second to the fifth element", other[2:5] )
  
  other.insert( 3, 99 )
  print( "Insert a new element", other )
  
  list.extend( other )
  print( "Join the two lists", list )

  e = list.pop(7)
  print( "Remove seventh element ["+str(e)+"]", list )
  
  e = list.remove(99)
  print( "Remove the number 99", list )
  
  print( "Sorted in reverse order", sorted( list, cmp=ReverseSort ) )
  
  print()
  
def Dicts():
  print( 'Dictionaries' )

  dict = {}
  
  dict['a'] = 0
  dict['b'] = 1
  
  if 'c' in dict:
    dict['c'] += 1
  else:
    dict['c'] = 1

  print( 'Keys  :', dict.keys() ) 
  print( 'Values:', dict.values() ) 

  print( 'Keys sorted :', sorted(dict.keys()) ) 
  print( 'Items:', dict.items() )

  print()
  
    
def main():
  "The main function called when the utility is run."
  

  print( 'Lists and Dicts test' )
  print()
  
  Lists()
  Dicts()

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
