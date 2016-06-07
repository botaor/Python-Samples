#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show usage of Regular expressions"

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import re

def SimpleCheck( regex, str ):
  match = re.search( regex, str )
  if match:
    print( 'found -> ', '[' + match.group() + ']' )
  else:
    print( 'did not find' )

def GroupCheck( regex, str, n ):
  match = re.search( regex, str )
  if not match:
    print( 'did not find' )
    return

  print( 'all -> ', '[' + match.group() + ']' )
  for i in xrange(n+1):
    print( 'group', i, '->', match.group(i) )

def AllCheck( regex, str ):
  match = re.findall( regex, str )
  if not match:
    print( 'did not find' )
    return

  for s in match:
    print( 'found ->', s )

def main():
  print( 'Regular expressions' )
  print()

  str = "here is a value:a12."
  SimpleCheck( r'value:\w\w\w', str )       # \w - word characters
  SimpleCheck( r'value:\w\w\w\w', str )
  SimpleCheck( r'\d+', str )                # \d - digits
  SimpleCheck( r'..\d+', str )              # +  - one or more times
  SimpleCheck( r'\s*va', str )              # \s - space characters, * - zero or more times
  SimpleCheck( r'^va', str )                # ^  - start of line
  SimpleCheck( r'^here', str )
  SimpleCheck( r'12.$', str )               # $  - end of string
  SimpleCheck( r'1a?2', str )               # ?  - 1 or 0
  SimpleCheck( r'[12]+', str )              # [] - group of characters

  str = "My email address is: my-self@g.gmail.com. Please use it. You can also use i-other@gmail.com."
  SimpleCheck( r'\w+@\w+', str )                      # Simple email
  SimpleCheck( r'[\w.-]+@[\w.-]+', str )              # More complex email
  SimpleCheck( r'[\w.-]+@[\w.-]+\.\w+', str )         # Even more complex email
  GroupCheck( r'([\w.-]+)@([\w.-]+\.\w+)', str, 2 )   # Even more complex email
  AllCheck( r'([\w.-]+)@([\w.-]+\.\w+)', str )        # Find all emails

  SimpleCheck( r'@.*\.', str )                        # The usual greedy behaviour (match as much as possible)
  SimpleCheck( r'@.*?\.', str )                       # Match as little as possible

  # Substitution example
  print( re.sub(r'([\w.-]+)@([\w.-]+\.\w+)', r'\1@new.com', str) )


  print()

  return 0


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
