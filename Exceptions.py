#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show how to handle exceptions"

# This line must be at the beginning of the file
from __future__ import print_function

import sys

def GenericException():
  "Generic and simple use of exceptions"
  try:
    a = 10 / 0
  except:
    print( "Exception" )
    
def GenericExceptionMessage():
  "Catch exception and print exception message"
  try:
    a = 10 / 0
  except Exception as e:
    print( "Exception:", e )
    
def GenericExceptionMultiple( value ):
  "Catch several exceptions"
  try:
    a = 10 / value
  except (TypeError, ZeroDivisionError) as e:
    print( "Specific Exception:", type(e), e )
    return
  except Exception as e:
    print( "generic Exception:", type(e), e )
    return
  else:
    print( "Execute if no exception" )
  finally:
    print( "Always execute at end of try clause" )
    
  print( "Return" )


def RaiseGenericException( str ):  
  try:
    raise Exception( str )
  except Exception as e:
    print( "Exception:", e )
  
def IgnoreException():  
  try:
    t = 1 / 0
  except:
    pass
    
  print( "Still here" )

def RethrowException():  
  try:
    try:
      t = 1 / 0
    except:
      print( "Caught first exception" )
      raise
  except Exception as e:
    print( "second exception", e )
    
  print( "Still here" )
  
  
# Define exceptions raised by this module

class ModuleError(Exception):
    "Base class for exceptions in this module. So the we can catch all exceptions of the module"
    pass

class UserError(ModuleError):
    """Exception example.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, value):
        self.value = value
        
    def __str__(self):
       return repr( "UserError with value '" + self.value + "'" )


def RaiseUserException():
  try:
    raise UserError( "My exception" )  
  except Exception as e:
    print( "Exception:", e )

def main():
  "The main function called when the utility is run."
  

  print( 'Exceptions test' )
  print()
  
  GenericException()
  print()
  GenericExceptionMessage()
  print()
  GenericExceptionMultiple( "qq" )
  print()
  GenericExceptionMultiple( 0 )
  print()
  GenericExceptionMultiple( 1 )
  print()
  
  RaiseGenericException( "My Exception" )
  print()
  IgnoreException()
  print()
  RethrowException()
  print()
  
  RaiseUserException()
  print()
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
