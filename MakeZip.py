#!/usr/bin/python
# -*- coding: latin-1 -*-
"Zip a folder with the possibility to exclude some files."

# This line must be at the beginning of the file
from __future__ import print_function

import os
import sys
import fnmatch
import argparse
import zipfile

def _IsIgnoreFolder( name, ignoreList ):
  for n in ignoreList:
    if n[-1] != '/':
      continue
  
    if fnmatch.fnmatch( name, n[:-1] ):
      return True
      
  return False
  
  
def _IsIgnoreFile( name, ignoreList ):
  for n in ignoreList:
    if n[-1] == '/':
      continue

    if fnmatch.fnmatch( name, n ):
      return True
      
  return False
      

def ReadIgnoreFromFile( fname ):
  "Read an ignore list from a text file. The format is the same as .gitignore"
  "  fname - name of text file."
  "  returns the list"
  if not fname:
    return []
    
  ignores = []
  
  try:
    f = open( fname, 'rU' )
  except (IOError) as e:
    return []

  for line in f:
    if line[0] == '#':
      continue
      
    if len( line[:-1].strip() ) == 0:
      continue
      
    ignores.append( line[:-1] )
    
  f.close()
  
  return ignores


def ReadIgnoreFromString( str ):
  "Take a string of comma separated wildcards and create an ignore list."
  "  str - string with comma separated wildcards."
  "  returns the list"
  if not str:
    return []

  tmp = str.split( ',' )
  ignores = []
  for s in tmp:
    ignores.append( s.strip() )
  
  return ignores


def zipdir( zipname, folder, ignore=[]):
  "Create a zip file of a folder (including subfolders)."
  "  zipname - name of zip file to create."
  "  folder  - folder to zip."
  "  ignore  - list of wildcards to ignore."
  
  zipf = zipfile.ZipFile( zipname, 'w', zipfile.ZIP_DEFLATED )
  
  ignoreFolders = []
  tot = 0
  for root, dirs, files in os.walk(folder):
    for dir in dirs:
      if _IsIgnoreFolder( dir, ignore ):
        ignoreFolders.append( os.path.join( root, dir ) )

    if root in ignoreFolders:
      continue

    for file in files:
      if _IsIgnoreFile( file, ignore ):
        continue
        
      zipf.write(os.path.join(root, file))
      tot += 1

  zipf.close()  

  return tot

            
def main():
  "The main function called when the utility is run"
  print( 'Zip folder     V1.00                                    Rui Botão, Portugal' )
  print()
  
  parser = argparse.ArgumentParser(description="<Put application description here>" )  
  
  parser.add_argument( "zipfile", help="Name of zip file to create" )
  parser.add_argument( "folder", help="Folder to zip" )
  parser.add_argument( "-iF", "-ignoreFile", help="File with ignore wildcards (like .gitignore)", type=str )
  parser.add_argument( "-iS", "-ignoreString", help="List of ignore wildcards (comma separated)", type=str )
  
  args = parser.parse_args()

  ignores = ReadIgnoreFromFile( args.iF )  
  ignores = ignores + ReadIgnoreFromString( args.iS )  

  print( "Zip filename:", args.zipfile )
  print( "Zip folder:", args.folder )
  print( "Ignores", ignores )
  
  print( "Working..." )
  tot = zipdir( args.zipfile, args.folder, ignores )
  print( "Compressed", tot, "files." )

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
