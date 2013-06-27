#!/usr/bin/env python

# ---------------------------
# projects/xml/XML.py
# Copyright (C) 2013
# Arturo Lemus
# Andres Echeverria
# ---------------------------

# ------------
# xml_eval
# ------------

import xml.etree.ElementTree as ET


def xml_eval(filename):  
     
    # Read entire file into a string
    with open (filename, "r") as myfile:
        data = myfile.read() 
    
    # Find query document by traversing the input from the end
   
    i = len(data) - 1    
    while data[i] != '\n' :
        i -= 1   
    query = data[i:]
    query = query.replace("\n", "")
    
    
    # Find XML document, represent it as string
    n = 0
    doc = ""
    
    while n < i :
        doc += data[n]
        n += 1
    
    # Create roots for 2 element trees, query and doc
    queryRoot = ET.fromstring(query)
    docRoot = ET.fromstring(doc)

    # Create lists containing the elements of 
    # each of the newly created element trees
    
    queryList = []
    docList = []
     
    for child in queryRoot.iter():
        queryList.append(child.tag)
    
    for child in docRoot.iter():
        docList.append(child.tag)

    elementMatch = 0

    # First step
    # Find all occurrences of the top level element
    # of the query in the xml document
    #returns a list

    topLevelElem = docRoot.findall('.//' + queryList[0])  # '//Team'
        
    elementID = []
    i = 0

    # elementID contains the indices of where query root occurs
    # keys for dictionary, ID of 'Team'
    while i < len(docList) : 
        if docList[i] == queryList[0] :
            elementID.append(i + 1)
        i += 1
    
    dictionary = dict()
    
    m = 0 
    #Populating dictionary with mapping of root element's found in the document based on the query pattern
    #With the elementID that is associated with them
    # (Team, 2), ('Team', 7)
    while m < len(topLevelElem):
        dictionary[topLevelElem[m]] = elementID[m]
        m += 1
  
    ID_Output = [] #Contains the ID's of the element queries with a matching pattern, stores n lines of our output
    
   
    n = 0
    
    # Find top-level element from query, i.e. Team
    b = 1 
    
    queryChildren= []
    while b < len(queryList):
        queryChildren.append(queryList[b])
        b+=1
        
        
    occur = 0 # Stores the value for our 1st line of output
    limit = len(queryChildren)
      
    #Start at the nodes of the tree containing the root as a starting point
    
    for element in topLevelElem:      
        elementMatch = 0   #Reset counter when we switch subtrees    
        # Second step: Iterate over the root's subtree
        for child in element.iter():                  
            #Once in a subtree checks for all remaining elements of the query pattern ( the list queryChildren)
            #If the number of element matches is equal to the query's length excluding the root (the variable limit)
            #Increment occur counter                        
            for query in queryChildren:                
                if child.tag == query :                
                    elementMatch += 1
                    if elementMatch == limit:
                        occur+=1
                        ID_Output.append(dictionary.get(element))
                        elementMatch = 0 #Also reset counter when there is an occurrence
                 
   
    
    # List for storing results including Number of occurrence and ID lines
    
    # Split into xml_print, new function to write unit tests for
    # print occur  
        
    results = [] #Stores all items of solution
    results.append(occur) #Adding 1st line
    for occurencePlace in ID_Output:
        results.append(occurencePlace) #Adding the rest of the ID lines of matching queries
    return results
    
# Searches the subtree of the query root, iterating of all children, returns boolean
def print_XML_output(filename):
    out = xml_eval(filename)
    for x in out:
        print x
   
import sys
xml_eval(sys.stdin)