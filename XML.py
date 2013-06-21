#!/usr/bin/env python
import xml.etree.ElementTree as ET

def search_xml():   
    # Read entire file into a string
    with open ("RunXML.in", "r") as myfile:
        data = myfile.read() 
    
    # Find the beginning of the Query Document, Store in string
    i = len(data) - 1
    
    while data[i] != '\n' :
        i -= 1   
   
    query = data[i:]
    query = query.replace("\n", "")
    
    # Copy the xml document were searching into its own string
    n = 0
    doc = ""
    
    while n < i :
        doc += data[n]
        n += 1
    # print query
    # print doc 
    
    # Create roots for 2 element trees, query and doc
    queryRoot = ET.fromstring(query)
    docRoot = ET.fromstring(doc)

    queryList = []
    docList = []
    
 
    for child in queryRoot.iter():
        queryList.append(child.tag)
        
  
    
    for child in docRoot.iter():
        docList.append(child.tag)


    numMatches = 0 # number of matches        
    # First step
    a = docRoot.findall('.//' + queryList[0]) #'//Team'
    query_elements_toMatch = len(queryList)-1
    
    elementID = []
    i = 0
    while i < len(docList) : 
        # do something
        if docList[i] == queryList[0] :
            elementID.append(i+1)
        i += 1
    
       
    output = []
      
    count = -1
    for element in a:        
        count+= 1
        # print count
        for child in element.iter():     
            print child.tag
            # Second step
            # If find cooly, increment first line of output
            if child.tag == queryList[1] : # "Cooly"
                
                numMatches += 1
                output.append(elementID[count])     
            
   
    print numMatches 
    
    # array for storing results
   
    for num in output:
        print num
    
    
   
search_xml()