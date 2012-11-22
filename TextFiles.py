#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show how to handle text files"

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import codecs

def ReadFileComplete( filename ):
  "Read the whole contents of the file to a variable"
  f = open( filename, 'rU' )
  lines = f.read()
  f.close()
  
  return lines
  
def ReadFileList( filename ):
  "Read the file and return a list of lines. Each line has '\n' at the end"
  f = open( filename, 'rU' )
  lines = f.readlines()
  f.close()

  return lines
  
def ReadFileLinesFor( filename ):
  "Read the file and return a list of lines. The lines do note end with '\n'. Use a for loop"
  f = open( filename, 'rU' )
  lines = []
  for line in f:
    lines.append( line[:-1] )
  f.close()
  
  return lines
  
def ReadFileLinesWhile( filename ):
  "Read the file and return a list of lines. The lines do note end with '\n'. Use a while loop"
  f = open( filename, 'rU' )
  lines = []
  while True:
    line = f.readline()
    if not line:
      break
    lines.append( line[:-1] )
  f.close()

  return lines
  
def ReadFileUnicode( filename ):
  "Read a unicode file. The result is a list of unicode strings"
  f = codecs.open( filename, 'rU', 'cp1252' )
  lines = f.readlines() 
  f.close()

  return lines  
  
def WriteFile( filename, lines ):
  "write a list of strings to a text file"
  f = open( filename, 'w' )
  for li in lines:
    f.write( li )
    if li[-1] != '\n':
      f.write( '\n' ) ;
  f.close()
  
def AppendFile( filename, lines ):
  "Append a list of strings to a text file"
  f = open( filename, 'a' )
  for li in lines:
    f.write( li )
    if li[-1] != '\n':
      f.write( '\n' ) ;
  f.close()

def WriteFileUnicode( filename, lines ):
  "write a list of unicode strings to a text file"
  f = codecs.open( filename, 'w', 'cp1252' )
  for li in lines:
    f.write( li )
    if li[-1] != '\n':
      f.write( '\n' ) ;
  f.close()
  
  
def main():
  "The main function called when the utility is run."

  print( 'Text files test' )
  print()
  

  lines = ReadFileComplete( "samples/text.txt" )
  print( lines )
  print()
  
  lines = ReadFileList( "samples/text.txt" )
  print( lines )
  print()
  
  lines = ReadFileLinesFor( "samples/text.txt" )
  print( lines )
  print()
  
  lines = ReadFileLinesWhile( "samples/text.txt" )
  print( lines )
  print()
  
  lines = ReadFileUnicode( "samples/text.txt" )
  print( lines )
  print()
  
  lines = ['1', '2', 'abc', 'ãÉ0' ]
  WriteFile( 'out.txt', lines )
  AppendFile( 'out.txt', lines )

  lines = ReadFileUnicode( "samples/textutf8.txt" )
  WriteFileUnicode( 'outunicode.txt', lines )
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
