#!/usr/bin/env python

# -------------------------------
# projects/xml/TestXML.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET
from XML import xml_solve, xml_compare_trees

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ---------
    # xml_solve
    # ---------

    def test_xml_solve_1 (self) :
        string = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>"
        writer = StringIO.StringIO()
        xml_solve(string, writer)
        self.assert_(writer.getvalue() == "2\n2\n7\n")

    def test_xml_solve_2 (self) :
        string = "<and><back><and><forth><and><back></back><forth></forth></and></forth><back><and><forth></forth><back></back></and></back></and></back><forth><and><back><and><back></back><forth></forth></and></back><forth><and><back></back><forth></forth></and></forth></and></forth></and><back><and></and></back>"
        writer = StringIO.StringIO()
        xml_solve(string, writer)
        self.assert_(writer.getvalue() == "3\n2\n8\n14\n")

    def test_xml_solve_3 (self) :
        string = "<XML><Separates><Data><from><HTML></HTML></from></Data></Separates><Simplifies><Data><Sharing></Sharing><Transport></Transport></Data><Platform><Changes></Changes></Platform></Simplifies><Makes><Your><Data><More><Available></Available></More></Data><Life><More><Fun></Fun></More></Life></Your></Makes></XML><Makes><Your><Life></Life><Data></Data></Your></Makes>"
        writer = StringIO.StringIO()
        xml_solve(string, writer)
        self.assert_(writer.getvalue() == "1\n12\n")


    # -----------------
    # xml_compare_trees
    # -----------------
    def test_xml_compare_trees_1 (self) :
        string = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>"
        strXML = "<XML>\n"
        strXML += string
        strXML += "</XML>"
        root = ET.fromstring(strXML)
        self.assert_(xml_compare_trees(root[1], root[0][0]) == True)

    def test_xml_compare_trees_2 (self) :
        string = "<XML><Separates><Data><from><HTML></HTML></from></Data></Separates><Simplifies><Data><Sharing></Sharing><Transport></Transport></Data><Platform><Changes></Changes></Platform></Simplifies><Makes><Your><Data><More><Available></Available></More></Data><Life><More><Fun></Fun></More></Life></Your></Makes></XML><Makes><Your><Life></Life><Data></Data></Your></Makes>"
        strXML = "<XML>\n"
        strXML += string
        strXML += "</XML>"
        root = ET.fromstring(strXML)
        self.assert_(xml_compare_trees(root[1], root[0][2]) == True)

    def test_xml_compare_trees_3 (self) :
        string = "<and><back><and><forth><and><back></back><forth></forth></and></forth><back><and><forth></forth><back></back></and></back></and></back><forth><and><back><and><back></back><forth></forth></and></back><forth><and><back></back><forth></forth></and></forth></and></forth></and><back><and></and></back>"
        strXML = "<XML>\n"
        strXML += string
        strXML += "</XML>"
        root = ET.fromstring(strXML)
        self.assert_(xml_compare_trees(root[1], root[0][1]) == False)

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
