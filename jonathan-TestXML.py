#!/usr/bin/env python

# -------------------------------
# projects/XML/TestXML.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestXML.py > TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py > TestXML.out
"""

# -------
# imports
# -------

import os
import StringIO
import unittest
import xml.etree.ElementTree as ET
from XML import xml_read, xml_populate_trees, xml_make_string, xml_compare, xml_compare_helper, xml_print, xml_solve, xml_make_string


# -------
# TestXML
# -------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
	"""
	Reads in a blank line
	"""
	r = StringIO.StringIO("")
	a = [0, 0]
	b = xml_read(r, a)
	self.assert_(a[0] == 0)
	self.assert_(a[1] == 0)


    def test_read_2 (self) :
	"""
	Splits a <begin> and </end> tag
	"""
	r = StringIO.StringIO("<Begin></Begin>")
	a = []
	b = xml_read(r, a)
	self.assert_(b == False)
	self.assert_(a[0] == "<Begin> ")
	self.assert_(a[1] == "</Begin> ")


    def test_read_3 (self) :
	"""
	Splits a nested tag with spaces into slots in the array
	"""
	r = StringIO.StringIO("<Begin>  <End>   </End>  </Begin>")
	a = []
	b = xml_read(r, a)
	self.assert_(b == False)
	self.assert_(a[0] == "<Begin> ")
	self.assert_(a[1] == "<End> ")
	self.assert_(a[2] == "</End> ")
	self.assert_(a[3] == "</Begin> ")

    def test_read_4 (self) :
	"""
	Splits multiple lines into respective spots
	"""
	r = StringIO.StringIO("<Begin>  <End> <Junk> </Junk>  </End>  </Begin>\n<Yolo><Swag></Swag></Yolo>")
	a = []
	b = xml_read(r, a)
	self.assert_(b == False)
	self.assert_(a[0] == "<Begin> ")
	self.assert_(a[1] == "<End> ")
	self.assert_(a[2] == "<Junk> ")
	self.assert_(a[3] == "</Junk> ")
	self.assert_(a[4] == "</End> ")
	self.assert_(a[5] == "</Begin> ")
	self.assert_(a[6] == "<Yolo> ")
	self.assert_(a[7] == "<Swag> ")
	self.assert_(a[8] == "</Swag> ")
	self.assert_(a[9] == "</Yolo> ")

    
    #-------------------
    # xml_populate_trees
    #-------------------

    def test_populate_trees_1 (self) :
	"""
        Creates 2 identical trees for the main and key and compares
	"""
	tag_list = []

	#These are for the main tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	#these are for the key tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	tree_list_1 = []

	xml_populate_trees(tag_list, tree_list_1)
		
	self.assert_(tree_list_1[0].tag == tree_list_1[1].tag)
	self.assert_(ET.tostring(tree_list_1[0]) == ET.tostring(tree_list_1[1]))


    def test_populate_trees_2 (self) :
	"""
	Creates a key and a main tree and checks for validity via their string methods
	"""
	tag_list = []

	#These are for the main tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("<A>")#Grandchild of outer
	tag_list.append("</A>")
	tag_list.append("<B></B>")#Grandchild of outer MIGHT ERROR!
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	#these are for the key tree
	tag_list.append("<Outer>")
	tag_list.append("<In>")
	tag_list.append("</In>")
	tag_list.append("<Soup>")
	tag_list.append("</Soup>")
	tag_list.append("</Outer>")

	tree_list_2 = []
	
	xml_populate_trees(tag_list, tree_list_2)

	self.assert_( ET.tostring(tree_list_2[1]) == "<Outer><In /><Soup /></Outer>")
	self.assert_( ET.tostring(tree_list_2[0]) ==  "<Outer><Inner><A /><B /></Inner></Outer>")
	self.assert_(tree_list_2[0].tag == tree_list_2[1].tag)	


    def test_populate_trees_3 (self) :
	"""
	Tests multiple tree creations
	"""

	tag_list = []

	#mainTree 1
	tag_list.append("<Mone>")
	tag_list.append("</Mone>")

	#keyTree 1
	tag_list.append("<Kone>")
	tag_list.append("</Kone>")

	#mainTree 2
	tag_list.append("<Mtwo>")
	tag_list.append("</Mtwo>")

	#keyTree 2
	tag_list.append("<Ktwo>")
	tag_list.append("</Ktwo>")

	#mainTree 3
	tag_list.append("<Mthree>")
	tag_list.append("</Mthree>")

	#keyTree 3
	tag_list.append("<Kthree>")
	tag_list.append("</Kthree>")

	#mainTree 4
	tag_list.append("<Mfour>")
	tag_list.append("</Mfour>")

	#keyTree 4
	tag_list.append("<Kfour>")
	tag_list.append("</Kfour>")

	tree_list_3 = []
	


	xml_populate_trees(tag_list, tree_list_3)



	self.assert_(len(tree_list_3) == 8)
	self.assert_(ET.tostring(tree_list_3[0]) == "<Mone />");
	self.assert_(ET.tostring(tree_list_3[1]) == "<Kone />");
	self.assert_(ET.tostring(tree_list_3[2]) == "<Mtwo />");
	self.assert_(ET.tostring(tree_list_3[3]) == "<Ktwo />");
	self.assert_(ET.tostring(tree_list_3[4]) == "<Mthree />");
	self.assert_(ET.tostring(tree_list_3[5]) == "<Kthree />");
	self.assert_(ET.tostring(tree_list_3[6]) == "<Mfour />");
	self.assert_(ET.tostring(tree_list_3[7]) == "<Kfour />");
	



    # ------------------
    # xml_compare_helper
    # ------------------

    def test_compare_helper_1 (self) :
	"""
	compares 2 different trees and returns False
	"""
	tag_list = []

	#These are for the main tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	#these are for the key tree
	tag_list.append("<Outer>")
	tag_list.append("<Fatboy>")
	tag_list.append("</Fatboy>")
	tag_list.append("</Outer>")

	tree_list_1A = []

	xml_populate_trees(tag_list, tree_list_1A)

	result = xml_compare_helper(tree_list_1A[0], tree_list_1A[1])
	
	self.assert_(result == False)



    def test_compare_helper_2 (self) :
	"""
	compares 2 identical trees and returns True
	"""
	tag_list = []

	#These are for the main tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	#these are for the key tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	tree_list_1B = []

	xml_populate_trees(tag_list, tree_list_1B)

	result = xml_compare_helper(tree_list_1B[0], tree_list_1B[1])
	
	self.assert_(result == True)


    def test_compare_helper_3 (self) :
	"""
	finds a match deep into the tree w/ siblings
	"""
	tag_list = []

	#These are for the main tree
	tag_list.append("<Outer>")
	tag_list.append("<Inner>")
	tag_list.append("<A>")
	tag_list.append("<B>")
	tag_list.append("</B>")
	tag_list.append("<C>")
	tag_list.append("</C>")
	tag_list.append("</A>")
	tag_list.append("</Inner>")
	tag_list.append("</Outer>")

	#these are for the key tree
	tag_list.append("<A>")
	tag_list.append("<C>")
	tag_list.append("<F>")
	tag_list.append("</F>")
	tag_list.append("</C>")
	tag_list.append("</A>")


	tree_list_1C = []

	xml_populate_trees(tag_list, tree_list_1C)

	result = xml_compare_helper(tree_list_1C[0], tree_list_1C[1])
	
	self.assert_(result == False)




    # -----------
    # xml_compare
    # -----------

    def test_compare_1 (self) :
        """
        Finds two matches
        """
	tag_list = []

	#mainTree
	tag_list.append("<Z>")
	tag_list.append("<A>")
	tag_list.append("<C>")
	tag_list.append("<D>")
	tag_list.append("</D>")
	tag_list.append("<E>")
	tag_list.append("</E>")
	tag_list.append("</C>")
	tag_list.append("</A>")
	tag_list.append("</Z>")

	#keyTree
	tag_list.append("<A>")
	tag_list.append("<C>")
	tag_list.append("<D>")
	tag_list.append("</D>")
	tag_list.append("</C>")
	tag_list.append("</A>")

	tree_list = []
	


	xml_populate_trees(tag_list, tree_list)
	
	matches = []

	xml_compare(tree_list[0], tree_list[1], matches)

	self.assert_(len(matches) == 1)
	self.assert_(matches[0] == 2)


    def test_compare_2 (self) :
        """
        finds one match at the 2nd element
        """

	tag_list = []

	#mainTree
	tag_list.append("<Z>")
	tag_list.append("<A>")
	tag_list.append("<C>")
	tag_list.append("<D>")
	tag_list.append("</D>")
	tag_list.append("<E>")
	tag_list.append("</E>")
	tag_list.append("</C>")
	tag_list.append("</A>")
	tag_list.append("</Z>")

	#keyTree
	tag_list.append("<A>")
	tag_list.append("<C>")
	tag_list.append("<D>")
	tag_list.append("</D>")
	tag_list.append("</C>")
	tag_list.append("</A>")

	tree_list = []
	


	xml_populate_trees(tag_list, tree_list)
	
	matches = []



	xml_compare(tree_list[0], tree_list[1], matches)

	self.assert_(len(matches) == 1)
	self.assert_(matches[0] == 2)

	

    def test_compare_3 (self) :
        """
        Finds a key with two siblings
        """

	tag_list = []

	#mainTree
	tag_list.append("<A>")
	tag_list.append("<Very>")
	tag_list.append("<Bad>")
	tag_list.append("</Bad>")
	tag_list.append("<Story>")
	tag_list.append("</Story>")
	tag_list.append("</Very>")
	tag_list.append("</A>")

	#keyTree
	tag_list.append("<Very>")
	tag_list.append("<Bad>")
	tag_list.append("</Bad>")
	tag_list.append("<Story>")
	tag_list.append("</Story>")
	tag_list.append("</Very>")

	tree_list = []
	

	xml_populate_trees(tag_list, tree_list)
	
	matches = []


	xml_compare(tree_list[0], tree_list[1], matches)



	self.assert_(len(matches) == 1)
	self.assert_(matches[0] == 2)

	


    # -----
    # print
    # -----


    #basic test
    def test_print_1 (self) :
	"""
	Tests print case of 3 elements
	"""
	w = StringIO.StringIO()
	matches = [2, 5, 6]
	
	xml_print(w, matches)
	self.assert_(w.getvalue() == "3\n2\n5\n6")



    #basic
    def test_print_2 (self) :
	"""
	Tests 6 cases to print
	"""
	x = StringIO.StringIO()
	matches = [3, 6, 34, 15, 19, 35]
	
	xml_print(x, matches)

	self.assert_(x.getvalue() == "6\n3\n6\n34\n15\n19\n35")


    #edge case of no matches found
    def test_print_3 (self) :
	"""
	Tests case of 0 matches
	"""	
	w = StringIO.StringIO()
	matches = []
	
	xml_print(w, matches)
	self.assert_(w.getvalue() == "0")

    #basic case
    def test_print_4 (self) :
	"""
	Prints 4 numbers
	"""
	w = StringIO.StringIO()
	matches = [99, 14, 51, 64]
	
	xml_print(w, matches)
	self.assert_(w.getvalue() == "4\n99\n14\n51\n64")

    #basic case
    def test_print_5 (self) :
	"""
	Prints 1 element found @ pos 1
	"""
	w = StringIO.StringIO()
	matches = [1]
	
	xml_print(w, matches)
	self.assert_(w.getvalue() == "1\n1")


    # ---------------
    # xml_make_string
    # ---------------

    def test_make_string_1 (self) :
	"""
	Constructs one string from 3 indices
	in a list
	"""
	stringList = []
	stringList.append("<One></One>")
	stringList.append("<Two></Two>")
	stringList.append("<Three></Three>")

	retString = xml_make_string(0,2,stringList)
	self.assert_(retString == "<One></One><Two></Two><Three></Three>")


    def test_make_string_2 (self) :
	"""
	Constructs a string from 1 index
	"""
	stringList = []
	stringList.append("<Pickles></Pickles>")

	retString = xml_make_string(0,0,stringList)
	self.assert_(retString == "<Pickles></Pickles>")


    def test_make_string_3 (self) :
	"""
	Constructs one string from 6 indices
	in a list
	"""
	stringList = []
	stringList.append("<One></One>")
	stringList.append("<Two></Two>")
	stringList.append("<Three></Three>")
	stringList.append("<Four></Four>")
	stringList.append("<Five></Five>")
	stringList.append("<Six></Six>")


	retString = xml_make_string(0,5,stringList)
	self.assert_(retString == "<One></One><Two></Two><Three></Three><Four></Four><Five></Five><Six></Six>")



    # ---------
    # xml_solve
    # ---------

    def test_solve_1 (self) :
	"""
	Simple test case where there is a match at pos 2
	"""
        r = StringIO.StringIO("<A><B><C></C></B></A>\n<B><C></C></B>")
	w = StringIO.StringIO()
	xml_solve(r, w)

	self.assert_(w.getvalue() == "1\n2")


    def test_solve_2 (self) :
	"""
	Tests 3 levels deep with 2 siblings	
	"""
        r = StringIO.StringIO("<A><B><C><D></D><E></E></C></B></A>\n<B><C><D></D><E></E></C></B>")
	w = StringIO.StringIO()
	xml_solve(r, w)

	self.assert_(w.getvalue() == "1\n2")



    def test_solve_3 (self) :
	"""
	Finds 2 matches at different levels
	"""
        r = StringIO.StringIO("<A><B><D><E></E><F></F></D></B><C><D><E></E><F></F></D></C></A>\n<D><E></E><F></F></D>")
	w = StringIO.StringIO()
	xml_solve(r, w)

	self.assert_(w.getvalue() == "2\n3\n7")




# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
