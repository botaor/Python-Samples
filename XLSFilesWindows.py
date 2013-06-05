#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Shows how to interact with an excel file.
Only works in a windows environment with Microsoft excel installed.
It is possible to read and write values to the excel workbook.

This module depends on the win32com module.
"""

# This line must be at the beginning of the file
from __future__ import print_function

from win32com.client import Dispatch
import sys, os


class XLSFile:
  def __init__( self ):
    "Constructor"  
    try:
      self.excel = Dispatch('Excel.Application')
    except:
      raise Exception( "Could not open excel object" )

  def Visible( self, show ):    
    "To show or hide the excel application window"  
    self.excel.Visible = show
      
  def Open( self, filename, sheetname ):    
    "To actually open the file and select one worksheet"  
    # filename must be a complete path
    self.workbook = self.excel.Workbooks.Open( os.path.abspath( filename ) )
    self.ActivateSheet( sheetname )
    
  def OpenSimple( self, filename, sheetname ):    
    "Open the file as read only and only for simple usage. Some other functions may fail..."  
    # filename must be a complete path
    self.workbook = self.excel.Workbooks.Open( os.path.abspath( filename ), False, True )
    self.sheet = self.workbook.Sheets( sheetname )
    self.sheet.Activate()

  def Close( self ):
    "Close the currently opened workbook"  
    self.workbook.Close(SaveChanges=0) #to avoid prompt

  def Dispose( self ):
    "Dispose all system resources. Do not use this object anymore!"  
    try:
      self.excel.Quit()
      self.excel.Visible = 0
      #must make Visible=0 before del self.excelapp or EXCEL.EXE remains in memory.
      del self.excel
    except:
      raise Exception( "Could not close Excel properly (maybe running this script as administrator?). Please close it." )

  def PrintPDF( self, pdfName ):
    "Print current sheet to a PDF file"
    self.sheet.ExportAsFixedFormat( 0, os.path.abspath( pdfName ) )
      
  def Save( self ):
    "Save currently opened workbook"
    self.workbook.Save()
    self.workbook.Saved = 0 #p.248 Using VBA 5
      
  def ActivateSheet( self, name ):
    "Select and activate a sheet by name"  
    self.sheet = self.workbook.Sheets( name )
    self.sheet.Activate()
    self.nCols = self.sheet.Cells(1,1).SpecialCells(11).Column
    self.nRows = self.sheet.Cells(1,1).SpecialCells(11).Row
      
  def NumberOfRows( self ):
    "How many rows are filled in the present worksheet"
    return self.nRows
    
  def NumberOfCols( self ):
    "How many columns are filled in the present worksheet"
    return self.nCols
    
  def ReadCell( self, row, col ):
    "Read the value of a cell (coordinates are zero based)"
    v = self.sheet.Cells( row+1, col+1 ).Value
    return v if v != None else ""
    
  def WriteCell( self, row, col, value ):
    "Change the value of a cell (coordinates are zero based)"
    self.sheet.Cells( row+1, col+1 ).Value = value


def main():
  "The main function called when the utility is run."
  
  print( 'Module XLS Files in a Windows environment' )
  print()

  #Create the excel object
  xls = XLSFile()

  xls.OpenSimple( r"Samples\xls2.xls", "Sheet1" )
  # Save as PDF
  xls.PrintPDF( r"Samples\xx.pdf" )
  #Close the workbook
  xls.Close()
  
  #open a workbook
  xls.Open( r"Samples\xls2.xls", "Sheet1" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  
  #get a value
  print( "B4", xls.ReadCell( 3, 1 ) )

  #change a value
  xls.WriteCell( 3, 1, "Her" ) 
  
  #save the book
  xls.Save()
  
  #Close the workbook
  xls.Close()

  xls.Open( r"samples\xls1.xls", "Update" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  print( "A1", xls.ReadCell( 0, 0 ) )
  
  xls.ActivateSheet( "Notes" )
  print( "Space in use:", xls.NumberOfRows(), "x", xls.NumberOfCols() )
  print( "A8", xls.ReadCell( 7, 0 ) )

  xls.Close()
  
  #Destroy the object
  xls.Dispose()
  
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
      