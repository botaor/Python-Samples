#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show normal components in the main script file."

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import argparse


def main():
  "The main function called when the utility is run"
  print( 'Main application  Vx.rr                                    Rui Botão, Portugal' )
  print()
  
  parser = argparse.ArgumentParser(description="<Put application description here>" )  
  
  parser.add_argument( "folder", help="Folder name" )
  parser.add_argument( "-o", "-option", help="One option", default="No", type=str )
  
  args = parser.parse_args()
  
  print( "Folder", args.folder )
  print( "Option", args.o )
  

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
