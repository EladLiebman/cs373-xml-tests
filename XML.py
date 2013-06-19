#!/usr/bin/env python
import xml.etree.ElementTree as ET

def search_xml():
   # tree = ET.parse('RunXML.in')
    # root = tree.getroot()
    #s = ET.tostringlist(root)
    with open ("RunXML.in", "r") as myfile:
        data = "<XML>\n" + myfile.read()+ "\n</XML>"
    # root = ET.fromstring('RunXML_as_string')
    # for child in root.iter():
    # print child.tag
    root = ET.fromstring(data)
    
    for child in root.iter(root):
        print child.tag
    
    s = ET.tostring(root)

    
    data = data.replace("<XML>\n", "")
    data = data.replace("\n</XML>", "")
    
    #print data
    
    i = len(data) - 1
    while data[i] != '\n' :#something : 
        # we haven't found the newline, keep looking
        # once you find newline
            # break
        i -= 1
    #print len(data)
  # print data[205]
   
    query = data[i:]
    query = query.replace("\n", "")
   # print query
    #print i
   # while i < len(data) :
    n = 0
    doc = ""
    while n < i :
        doc += data[n]
        n+=1
    print doc 
        
    
    
search_xml()
    
