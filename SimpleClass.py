#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show creation of very simple class"

# This line must be at the beginning of the file
from __future__ import print_function

import sys

class Person:
  def __init__( self, name, age ):
    self.name = name
    self.age = age

  def IsAdult( self ):
    return self.age >= 18
    
  def ChangeAge( self, newAge ):
    self.age = newAge
    
  def Populatetags( self, all_tags ):
    for t in self.tags:
      if t in all_tags:
        all_tags[t] += 1 ;      
      else:
        all_tags[t] = 1 ;
  
  def __str__( self ):
    return self.name + " (" + str(self.age) + " years old)"
    
  def __repr__( self ):
    return self.__str__()

    
def main():
  "The main function called when the utility is run."
  

  print( 'Very simple class' )
  print()
  
  p = Person( "John", 21 )
  print( "Is John an adult?", p.IsAdult() )
  p.ChangeAge( 4 )
  print( "Change the age:", p )
  print( "Is John an adult?", p.IsAdult() )

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
    