#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show creation of very simple class"

# This line must be at the beginning of the file
from __future__ import print_function

import sys

class Person( object ):
  def __init__( self, name, sex, age ):
    self.__name = name
    self.__sex = sex
    self.__age = age

  def IsAdult( self ):
    return self.__age >= 18
    
  @property  
  def Age( self ):
    return self.__age
    
  @Age.setter  
  def Age( self, newAge ):
    self.__age = newAge
    
  def __str__( self ):
    return self.__name + " (" + str(self.__age) + " years old)"
    
  def __repr__( self ):
    return self.__str__()

    
class Man( Person ):
  def __init__( self, name, age ):
    Person.__init__( self, name, 'M', age )

  def IsAdult( self ):
    # Different way to access the base class
    if super( Man, self ).Age > 100:
      # very old people are kids again (just to show usage of super)
      return False
      
    return Person.IsAdult( self )
    
  def __str__( self ):
    return "Man - " + Person.__str__( self )

    
def main():
  "The main function called when the utility is run."
  

  print( 'Very simple class' )
  print()
  
  p = Person( "John", 'M', 21 )
  print( "Is John an adult?", p.IsAdult() )
  p.Age = 4
  print( "Change the age:", p )
  print( "Is John an adult?", p.IsAdult() )

  print()
  
  p = Man( "John", 156 )
  print( "p =", p )
  print( "Is John an adult?", p.IsAdult() )
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
    