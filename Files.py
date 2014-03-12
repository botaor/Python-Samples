#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show Handling of files"

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import os
import glob

def ShowFilesInDirectory( dir ):
  "Browse through all the files in a given directory"
  for f in os.listdir( dir ):
    if os.path.isdir( f ):
      print( "Directory:", f )
      continue
      
    (name_file, name_ext) = os.path.splitext( f )  
    name_full = os.path.join( dir, f )
    print( "File:", f, " - name", name_file, ", extension", name_ext, ", full name", name_full )

def ShowFilesWildcard( wildcard ):
  "Browse through all the files that match a certain wildcard"
  for f in glob.glob( wildcard ):
    print( f, os.path.basename( f ) )

def SpliFileName( filename ):
  "Split a filename into its basic components"
  print( "fullname:", filename )
  print( "dir     :", os.path.dirname( filename ) )
  print( "file    :", os.path.basename( filename ) )

  (name, ext) = os.path.splitext( os.path.basename( filename ) )  
  print( "split   :", name, ext )
  
def CheckIfExists( fname ):
  print( "File", fname, "Exists" if os.path.isfile( fname ) else "does NOT exist" )
  

def main():
  "The main function called when the utility is run."
  

  print( 'Module Files' )
  print()
  
  ShowFilesInDirectory( "Samples" )
  print()
  ShowFilesWildcard( "Samples/*.txt" )
  print()
  SpliFileName( "Samples/file.ext" )
  print()
  SpliFileName( "file.ext" )
  print()
  CheckIfExists( "Samples/text.txt" )
  CheckIfExists( "Samples/nofile.ext" )

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
