#!/usr/bin/env python

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestXML.py
% TestXML.py >& TestXML.out
"""

# --- imports ---
import StringIO
import unittest
import xml.etree.ElementTree as ET
from XML import XML_read, compareWithPatern, get_count, XML_solve, XML_eval

xml1 = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n"\
        + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>"\
        + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n"\
        + "</THU>\n<Team><Cooly></Cooly></Team>"
xml2 = "<Group></Group>"
xml3 = "<data>\n<country>\n<hank></hank>\n<year></year>\n<gdppc></gdppc>\n<heighbor></heighbor>\n</country>\n<county>\n<hank></hank>\n<year></year>\n<gdppc></gdppc>\n</county>\n</data>\n<country><hank></hank></country>"


xml_short = "<Team><Cooly></Cooly></Team>"
xml_short2 = "<Team><Cooly></Cooly></Team>"

xml_short3 = "<Team><chacha></chacha></Team>"
xml_short4 = "<Team><chacha></chacha></Team>"

xml_short5 = "<Group></Group>"
xml_short6 = "<Group></Group>"


class TestXML (unittest.TestCase) :

    # -------
    # xmlRead
    # -------

    # may have to remove \n from the assert statements

    def test_Read1 (self) :
        r = StringIO.StringIO(xml1)
        b = XML_read(r)
        self.assert_(b == "<rootnode>" + xml1 + "</rootnode>")
    def test_Read2 (self) :
	r = StringIO.StringIO(xml2)
        b = XML_read(r)
        self.assert_(b == "<rootnode>" + xml2 + "</rootnode>")
    def test_Read3 (self) :
	r = StringIO.StringIO(xml3)
        b = XML_read(r)
        self.assert_(b == "<rootnode>" + xml3 + "</rootnode>")

    def test_compareWithPatern1 (self) :
	elemTree = ET.fromstring(xml_short)
	elemTree2 = ET.fromstring(xml_short2)
	for it in elemTree2.iter():
            last=it
	self.assert_(compareWithPatern(elemTree,elemTree2, last) == True)

    def test_compareWithPatern2 (self) :
	elemTree = ET.fromstring(xml_short3)
	elemTree2 = ET.fromstring(xml_short4)
	for it in elemTree2.iter():
            last=it
	self.assert_(compareWithPatern(elemTree,elemTree2, last) == True)

    def test_compareWithPatern3 (self) :
	elemTree = ET.fromstring(xml_short5)
	elemTree2 = ET.fromstring(xml_short6)
	for it in elemTree2.iter():
            last=it
	self.assert_(compareWithPatern(elemTree,elemTree2, last) == True)

    def test_getCount1(self) :
	elemTree = ET.fromstring(xml_short)
	elemTree2 = ET.fromstring(xml_short2)
	a = []
	get_count(elemTree,elemTree2,a)
	self.assert_(a[0] == 1)

    def test_getCount2(self) :
	elemTree = ET.fromstring(xml_short3)
	elemTree2 = ET.fromstring(xml_short4)
	a = []
	get_count(elemTree,elemTree2,a)
	self.assert_(a[0] == 1)

    def test_getCount3(self) :
	elemTree = ET.fromstring(xml_short5)
	elemTree2 = ET.fromstring(xml_short6)
	a = []
	get_count(elemTree,elemTree2,a)
	self.assert_(a[0] == 1)

    def test_eval1(self) :
	w= StringIO.StringIO()
	XML_eval("<rootnode><T1></T1>\n<T2></T2></rootnode>",w)
	self.assert_(w.getvalue() == "0\n")
    
    def test_eval2(self) :
    	w= StringIO.StringIO()
    	XML_eval("<rootnode>" +xml1 + "</rootnode>",w)
    	self.assert_(w.getvalue() == "2\n2\n7\n")
    
    def test_eval3(self) :
    	w= StringIO.StringIO()
    	XML_eval("<rootnode>" + xml3 + "</rootnode>",w)
	self.assert_(w.getvalue() == "1\n2\n")

    def test_solve1(self) :
	r = StringIO.StringIO("<T1></T1>\n<T2></T2>")
	w = StringIO.StringIO()
	XML_solve(r, w)
	self.assert_(w.getvalue() == "0\n")

    def test_solve2(self) :
	r = StringIO.StringIO(xml1)
	w = StringIO.StringIO()
	XML_solve (r,w)
	self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_solve3(self) :
	r = StringIO.StringIO(xml3)
	w = StringIO.StringIO()
	XML_solve (r,w)
	self.assert_(w.getvalue() == "1\n2\n")

 
 
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
