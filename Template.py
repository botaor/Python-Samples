#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show ..."

# This line must be at the beginning of the file
from __future__ import print_function

import sys

def main():
  "The main function called when the utility is run."
  

  print( 'Module test' )
  print()

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
