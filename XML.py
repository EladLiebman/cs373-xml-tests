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


    numMatches = 0  # number of matches        
    # First step
    a = docRoot.findall('.//' + queryList[0])  # '//Team'
    
    
    elementID = []
    i = 0
    # keys for dictionary, ID of 'Team'
    while i < len(docList) : 
        # do something
        if docList[i] == queryList[0] :
            elementID.append(i + 1)
        i += 1
    
    dictionary = dict()
    
    m = 0 
    while m < len(a):
        dictionary[a[m]] = elementID[m]
        m += 1
    print dictionary.items()
    output = []
    print len(queryList)
   
    n = 0
    # Find top-level element from query, i.e. Team
    b = 1 
    queryChildren= []
    while b < len(queryList):
        queryChildren.append(queryList[b])
        b+=1
    occur = 0   
    limit = len(queryChildren)
    
    for q in queryChildren:
        print q
 
    #iterates over Cooly for now 
    for element in a:        
        numMatches = 0
        # print count
        # Second step
        for child in element.iter():     
            print child.tag
            
           
            # If find cooly, increment first line of output
            print " Index is %d" % n
            for query in queryChildren:
                
                if child.tag == query :  # "Cooly"                
                    numMatches += 1
                    if numMatches == limit:
                        occur+=1
                        output.append(dictionary.get(element))
                        numMatches = 0
                 
   
    #print numMatches 
    
    # array for storing results
    print occur
    for num in output:
        print num
    
# Searches the subtree of the query root, iterating of all children, returns boolean

   
search_xml()
