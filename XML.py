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
    print "QUERY:"
    queryList = []
 
    for child in queryRoot.iter():
        queryList.append(child.tag)
        
  
    print "DOC:"  
    for child in docRoot.iter():
        child.tag
        
    a = docRoot.findall('.//' + queryList[0]) #'//Team'
    print "Search for 1st query element:"
    for element in a:
        for child in element.iter():            
            print child.tag
        

    print queryList
search_xml()
    
