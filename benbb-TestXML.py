#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.cElementTree as etree
import sys

from XML import xml_read, xml_eval, xml_print, xml_solve

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_blanks (self) :
        r = StringIO.StringIO(" [blank line]\n     <THU>\n <Team>\n                    </Team>\n </THU><Team>    <Cooly>\n</Cooly></Team>")
        b = xml_read(r)
        self.assert_(b[0].tag == "THU")
        self.assert_(b[1].tag ==  "Team")
        
    def test_read_standard (self) :
        r = StringIO.StringIO("<THU>	<Team>\n		<ACRush></ACRush>\n		<Jelly></Jelly>\n		<Cooly></Cooly>\n	</Team>\n	<JiaJia>\n		<Team>\n			<Ahyangyi></Ahyangyi>\n			<Dragon></Dragon>\n			<Cooly><Amber></Amber></Cooly>\n		</Team>\n	</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        b = xml_read(r)
        self.assert_(b[0].tag == "THU")
        self.assert_(b[1].tag ==  "Team")
    
    def test_read_all_one_line(self) :
    	r = StringIO.StringIO("<THU><Team></Team></THU><Team><Cooly></Cooly></Team>")
        b = xml_read(r)
        self.assert_(b[0].tag == "THU")
        self.assert_(b[1].tag ==  "Team")

    # ----
    # eval
    # ----
	
    def test_eval_simple (self) :
        root = etree.Element("THU")
        some_ele = etree.SubElement(root, "Team")
        some_ele_child = etree.SubElement(some_ele, "Cats")
        self.assert_(xml_eval(root,some_ele_child) == True)
	
    def test_eval_string_false (self) :
        root = etree.fromstring("<THU>\n <Team>\n                    </Team>\n </THU>")
        kid = etree.fromstring("<Team>    <Cooly>\n</Cooly></Team>")
        self.assert_(xml_eval(root,kid) == False)
    
    def test_eval_string_true (self) :
        root = etree.fromstring("<THU>\n <Team>\n                    </Team>\n </THU>")
        kid = etree.fromstring("<Team>    \n</Team>")
        self.assert_(xml_eval(root,kid) == True)
	
    def test_eval_find_root (self) :
        root = etree.Element("THU")
        some_ele = etree.SubElement(root, "Team")
        some_ele_child = etree.SubElement(some_ele, "Cats")
        self.assert_(xml_eval(root,root) == True)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        elemLocations = [4,5,10,20,54,63,11,100]
        elemLocations.sort()
        xml_print(elemLocations, w)
        self.assert_(w.getvalue() == "8\n4\n5\n10\n11\n20\n54\n63\n100\n")

    # -----
    # solve
    # -----
	
    def test_solve_blanks (self) :
        r = StringIO.StringIO(" [blank line]\n     <THU>\n <Team>\n                    </Team>\n </THU><Team>    <Cooly>\n</Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "0\n")
     
    def test_solve_standard (self) :
        r = StringIO.StringIO("<THU>	<Team>\n		<ACRush></ACRush>\n		<Jelly></Jelly>\n		<Cooly></Cooly>\n	</Team>\n	<JiaJia>\n		<Team>\n			<Ahyangyi></Ahyangyi>\n			<Dragon></Dragon>\n			<Cooly><Amber></Amber></Cooly>\n		</Team>\n	</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "2\n2\n7\n")
    
    def test_solve_all_one_line(self) :
    	r = StringIO.StringIO("<THU><Team></Team></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "0\n")
	
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."

