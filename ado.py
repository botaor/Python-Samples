#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Module to show the usage of ADO in Windows. Good to access MSAccess databases...

This module depends on the pywin32 module.

Be carefull with 64 bit systems. Normally odbc drivers are only 32 bits. So you might need to install python 32 bits. 

If you already have python 64 bits installed, there is no problem. Install the 32 bits version in a 
different directory (eg: python_32) and in the installation screen 'Customize Python 2.7.3' select 
'Register Extensions' and select 'Entire feature will be unavailable', so that this version will not be the default one.

You will then have to install pywin32 module. If you install the 32 bit version it will correctly discover the
32 bit installation of python.

Be carefull also with possible non ascii characters in values. You will have to convert them to unicode.
"""

# This line must be at the beginning of the file
from __future__ import print_function

import sys
import adodbapi

class Database:
  def __init__( self, database ):
    "Constructor. Just give the filename of the database"  
    self.conn = adodbapi.connect( 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=' + database )
    self.cur = self.conn.cursor()
    
  def Close( self ):
    "Closes the connection to the database"  
    self.cur.close()
    self.conn.close()
    
  def ExecuteSQL( self, sql ):
    "Executes an SQL statement and returns a list with all the results"  
    self.cur.execute(sql)
    return self.cur.fetchall()

  def __str__( self ):
    "String representation of the object"  
    return "Database Object"
    
  def __repr__( self ):
    "String representation of the object"  
    return self.__str__()


def main():
  "The main function called when the utility is run."
  
  print( 'Module ADO in windows' )
  print()

  db = Database( "samples/Test.mdb" )

  result = db.ExecuteSQL( "SELECT People.name, Types.description FROM People INNER JOIN Types ON People.type = Types.code order by people.name" )
  for item in result:
    print( unicode( item[0] ), '-', unicode( item[1] ) )

  print()
  
  result = db.ExecuteSQL( "SELECT name FROM People WHERE age>20 order by people.name" )
  for item in result:
    print( unicode( item[0] ) )

  db.Close()

  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
