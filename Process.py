#!/usr/bin/python
# -*- coding: latin-1 -*-
"""How to launch other processes from a python script
More information and other use cases from:
http://docs.python.org/library/subprocess.html#module-subprocess
"""

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import subprocess

def CallExternal( cmd ):
  "Call an external program, wait for completion and return error code."
  return subprocess.call( cmd, shell = False )

def CallShell( cmd ):
  "Call a shell command, wait for completion and return error code. Output is written to stdout."
  return subprocess.call( cmd, shell = True )
  
def CallShellNoOutput( cmd ):  
  "Call a shell command, wait for completion and return tupple with error code and output."
  rc = 0
  out = ""
  try:
    out = subprocess.check_output( cmd, shell=True )
  except subprocess.CalledProcessError as e:
    rc = e.returncode
    out = e.output
    
  return (rc, out)

def main():
  "The main function called when the utility is run."

  print( 'Process test' )
  print()

  tt = CallExternal( 'notepad.exe' )
  print( 'rc=', tt )

  tt = CallShell( 'dir abc' )
  print( 'rc=', tt )

  tt = CallShellNoOutput("dir /B *")
  print( "ret =", tt[0] )
  print( "out:" )
  print( tt[1] )

  tt = CallShellNoOutput("copy")
  print( "ret =", tt[0] )
  print( "out:" )
  print( tt[1] )

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
