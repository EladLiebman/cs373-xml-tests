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

# renamed from search_xml()
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

    numMatches = 0

    # First step
    # Find all occurrences of the top level element
    # of the query in the xml document

    topLevelElem = docRoot.findall('.//' + queryList[0])  # '//Team'
        
    elementID = []
    i = 0

    # elementID contains the indices of where query occurs
    # keys for dictionary, ID of 'Team'
    while i < len(docList) : 
        if docList[i] == queryList[0] :
            elementID.append(i + 1)
        i += 1
    
    dictionary = dict()
    
    m = 0 
    while m < len(topLevelElem):
        dictionary[topLevelElem[m]] = elementID[m]
        m += 1
    #print dictionary.items()
    output = []
    #print len(queryList)
   
    n = 0
    # Find top-level element from query, i.e. Team
    b = 1 
    queryChildren= []
    while b < len(queryList):
        queryChildren.append(queryList[b])
        b+=1
    occur = 0   
    limit = len(queryChildren)
    
    #for q in queryChildren:
    #    print q
 
    #iterates over Cooly for now 
    for element in topLevelElem:        
        numMatches = 0
        # print count
        # Second step
        for child in element.iter():     
            print child.tag
            
           
            # If find cooly, increment first line of output
            #print " Index is %d" % n
            for query in queryChildren:
                
                if child.tag == query :  # "Cooly"                
                    numMatches += 1
                    if numMatches == limit:
                        occur+=1
                        output.append(dictionary.get(element))
                        numMatches = 0
                 
   
    #print numMatches 
    
    # array for storing results
    # Split into xml_print, new function to write unit tests for
    # print occur
    for num in output:
        print num
        
    results = []
    results.append(occur)
    for occurencePlace in output:
        results.append(occurencePlace)
    return results
    
# Searches the subtree of the query root, iterating of all children, returns boolean

   
print xml_eval("RunXML.in")