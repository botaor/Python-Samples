#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Shows how to interact with an excel file.
Works in any environment.

This module depends on the xlrd module (https://github.com/python-excel/xlrd).
"""

# This line must be at the beginning of the file
from __future__ import print_function

import sys, os
import xlrd


class XLSFile:
  def __init__( self ):
    "Constructor"  

  def Open( self, filename, sheet ):    
    "To actually open the file and select one worksheet (by name or number)"  
    self.workbook = xlrd.open_workbook( filename )
    self.ActivateSheet( sheet )
    
  def Close( self ):
    "Close the currently opened workbook"  
    # Still have to figure out how to do this.
    # But for smallscripts it is not necessary...

  def ActivateSheet( self, sheet ):
    "Select and activate a sheet by name or by index"  
    if isinstance( sheet, str ):
      self.sheet = self.workbook.sheet_by_name( sheet )
    else:
      self.sheet = self.workbook.sheet_by_index( sheet )
      
  def NumberOfRows( self ):
    "How many rows are filled in the present worksheet"
    return self.sheet.nrows
    
  def NumberOfCols( self ):
    "How many columns are filled in the present worksheet"
    return self.sheet.ncols
    
  def NumberOfSheets( self ):
    "How many sheets exist in the workbook"
    return self.workbook.nsheets
    
  def SheetNames( self ):
    "Return a list with the names of the sheets in the workbook"
    return self.workbook.sheet_names()
    
  def ReadCell( self, row, col ):
    "Read the value of a cell (coordinates are zero based)"
    v = self.sheet.cell_value( row, col )
    return v


def main():
  "The main function called when the utility is run."
  
  print( 'Module XLS Files environment' )
  print()

  #Create the excel object
  xls = XLSFile()
  
  #open a workbook
  xls.Open( r"Samples\xls2.xls", "Sheet1" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  
  #get a value
  print( "B4", xls.ReadCell( 3, 1 ) )

  #Close the workbook
  xls.Close()

  xls.Open( r"samples\xls1.xls", "Update" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  print( "A1", xls.ReadCell( 0, 0 ) )
  print( "A2", repr(xls.ReadCell( 1, 0 )) )
  
  xls.ActivateSheet( "Notes" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  print( "A8", xls.ReadCell( 7, 0 ) )

  print( "Number of sheets", xls.NumberOfSheets() )
  print( "Names of sheets", xls.SheetNames() )

  xls.Close()
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
      