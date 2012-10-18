#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show normal components in the main script file."

# This line must be at the beginning of the file
from __future__ import print_function

import sys


def Usage():  
  "Show the command line arguments of the utility"
  
  print( 'usage: MainApp [args] [-t] [-o]' )
  print()
  print( '\tt   - Change value of option T' )
  print( '\to   - Change value of option O' )

optionT = 0
optionO = 0  

def CheckArgs( args ): 
  "Check the parameters that are passed to the utility"
  global optionT, optionO

  if len( args ) < 1:
    Usage()
    return 1

  for a in args:
    if a[0] == '-' or a[0] == '/':
      if a[1] == '?' or a[1] == 'H' or a[1] == 'h':
        Usage()
        return 1
      elif a[1] == 't' or a[1] == 'T':
        optionT = 1
      elif a[1] == 'o' or a[1] == 'O':
        optionO = 1
      else:
        Usage()
        return 1

  return 0
  
  
def main():
  "The main function called when the utility is run"
  global optionT, optionO

  print( 'Main application  V0.00                                    Rui Botão, Portugal' )
  print()

  args = sys.argv[1:]
  if CheckArgs( args ) != 0:
    return 1
    
  for a in args:
    print( a )

  print()
  print( "OptionT", optionT )
  print( "OptionO", optionO )
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
