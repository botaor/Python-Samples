#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show usage of Date and Time functions"

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import datetime
import time

def main():
  print( 'Date and Time test' )
  print()
  
  print( "Now:", datetime.date.today() )
  print( "Now:", datetime.datetime.today() )
  print( "Now:", datetime.datetime.time( datetime.datetime.today() ) )
  print()
  
  print( "Special Date:", datetime.date( 2000, 1, 1 ) )
  print( "Special Hour:", datetime.datetime( 1999, 12, 31, 23, 59, 59 ) )
  print()

  print( "Datetime from string:", datetime.datetime.strptime( "09 10 2011 15:16:17", "%d %m %Y %H:%M:%S" ) )
  print( "Time from string:", time.strptime( "15:16:17", "%H:%M:%S" ) )
  print( "Date from string:", datetime.datetime.strptime( "09 10 2011", "%d %m %Y" ) )
  print()

  print( "Formatted string:", datetime.datetime.today().strftime( "%Y.%m.%d %H:%M:%S" ) )
  print()
  
  print( "five days from now:", datetime.date.today() + datetime.timedelta(days=5) )
  print()

  dt = datetime.datetime.now()
  print( "Year:", dt.year )
  print( "Month:", dt.month )
  print( "Day:", dt.day )
  print( "Weekday: (0-monday..6-sunday)", dt.weekday() )
  print( "Hour:", dt.hour )
  print( "Minute:", dt.minute )
  print( "Second:", dt.second )
  print()
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
