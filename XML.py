#!/usr/bin/python
# -*- coding: latin-1 -*-
"Module to show how to handle XML files"

# This line must be at the beginning of the file
from __future__ import print_function

import sys
from xml.dom import minidom

def GetTag( elem, name, ref ):
  e = elem.getElementsByTagName( name )
  if not e:
    if ref:
      raise Exception( "'" + name + "' tag not present in " + "'" + ref + "'." )
    else:
      raise Exception( "'" + name + "' tag not present in XML" )
  return e[0]
    
def CheckTag( elem, name ):
  e = elem.getElementsByTagName( name )
  if not e:
    return None
  return e[0]
    
def GetData( elem, name, ref ):
  return GetTag( elem, name, ref ).firstChild.data

def CheckData( elem, name ):
  e = CheckTag( elem, name )
  if not e:
    return None
  return e.firstChild.data

def GetAttribute( elem, name, ref ):
  try:
    return elem.attributes[name].value
  except KeyError, e:
    raise Exception( "'" + name + "' attribute not present in " + "'" + ref + "'." )
    
def CheckAttribute( elem, name ):
  try:
    return elem.attributes[name].value
  except KeyError, e:
    return None

def GetListOfNodes( node, name ):
  return node.getElementsByTagName( name )
    

def main():
  "The main function called when the utility is run."

  print( 'XML Files' )
  print()

  # First parse the XML file
  try:
    xmldoc = minidom.parse( r"Samples\xml.xml" )
  except Exception, e:
    print( "Parsing error:", e )
    print( "\t.....Aborting!" )
    return 3
 
  id = GetTag( xmldoc, 'identification', None )
  print( "Name:", GetData( id, "name", 'identification' ), " - version:", GetData( id, "version", 'identification' ) )
  print()

  for mod in GetListOfNodes( xmldoc, 'module' ):
    ver = CheckData( mod, 'version' )
    name = GetAttribute( mod, 'id', 'device' )
    print( "Module:", name, " -", ver if ver else "<no version>" )
  
    copies = GetTag( mod, 'copyFiles', 'Device ' +  name )
    for d in copies.getElementsByTagName( 'dir' ):
      id = GetAttribute( d, 'id', name )
      wc = CheckAttribute( d, 'wildcard' )
      if not wc:
        wc = '*'

      print( "id:", id, ", dir:", d.firstChild.data, ", files", wc ) ;
  
    print()
    
  return 0
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  rc = main()

  # This function will set the result value of this utility
  sys.exit( rc )
