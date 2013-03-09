#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show usage of argparse standard module"

# This line must be at the beginning of the file
from __future__ import print_function

import sys, math
import argparse

def perfect_square( arg ):
  v = int( arg )
  sqrt = math.sqrt( v )
  if sqrt != int( sqrt ):
    raise argparse.ArgumentTypeError( "%r is not a perfect square" % arg )

  return v


def main():
  "The main function called when the utility is run."
  parser = argparse.ArgumentParser(description="Examples of argparse usage", epilog="With a message at the end" )  

  # Simple argument that must always be present
  parser.add_argument( "echo", help="echo the string you use here" )

  # List of arguments that must always be present
  # '+' can also be '*' or an integer for a fixed quantity
  parser.add_argument( "words", help="Words to be written", nargs='+' )

  # An argument that can be omitted, and thus has a default value
  parser.add_argument( "times", help="number of times to display string (def=3)", nargs='?', type=int, default=3 )

  # A True or False option
  parser.add_argument( "-u", "--upper", help="Convert to upper case", action='store_true' )

  # An option that also needs a value
  parser.add_argument( "-n", help="Counter", default=5, type=int )

  # An option that also needs a value that can be omitted 
  parser.add_argument( "-v", "--value", help="A sample value", nargs='?', const='val', default='not present' )

  # An option that also needs a value but is restricted to a few choices
  parser.add_argument( "-t", "--type", help="Type of work to be done.", default=1, type=int, choices=[1,2,3] )

  # An option that will be counted on the command line
  parser.add_argument( "-c", "--count", help="Number of counts.", action="count", default=0 )

  # An option that must be present in the command line
  parser.add_argument( "-r", "--required", help="Required option", required=True )

  # An option that is validated by a user function
  parser.add_argument( "-p", "--perfect_square", help="A perfect square", type=perfect_square )

  # Two mutually exclusive options
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-x1", "--exone", action="store_false" )
  group.add_argument("-x2", "--extwo", action="store_true" )

  # Two mutually exclusive options that are mandatory
  group = parser.add_mutually_exclusive_group( required=True )
  group.add_argument("-x10", "--exten", action="store_false" )
  group.add_argument("-x20", "--extwenty", action="store_true" )

  args = parser.parse_args()

  print( 'argparse test' )
  print()
 
  if args.upper:
    v = args.echo.upper()
  else:
    v = args.echo
    
  print( v, args.times, "times" )
  print( "Counter is", args.n )
  print( "Work    is", args.type )
  print( "Value   is", args.value )
  print( "Counts are", args.count )
  print( "Words  are", args.words )
  print( "Exclusive one/two:", args.exone, args.extwo )
  print( "Exclusive required one/two:", args.exten, args.extwenty )
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
