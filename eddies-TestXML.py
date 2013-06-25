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
from XML import xmlEval, xmlQueryToRegex, xmlPrint, xmlRead, xmlSolve, et

xml1 = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n"\
        + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>"\
        + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n"\
        + "</THU>\n<Team><Cooly></Cooly></Team>"
xml_whitespace = "<THU>\n <Team>  \n\n <Cooly>\t</Cooly>\n </Team>\n </THU>"\
        + "\n<Team><Cooly>\t </Cooly> </Team>"
xml_text = "<THU>\n<Team>\n<Cooly>test text</Cooly>\n</Team>\n</THU>\n<Team>"\
        + "<Cooly>more test text</Cooly></Team>"
xml_easy = "<Team></Team>"

xml_child_source = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n"\
        + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>"\
        + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n"\
        + "</THU>"
xml_child_query = "<Team><Cooly></Cooly></Team>"

class TestXML (unittest.TestCase) :

    # -------
    # xmlRead
    # -------

    # may have to remove \n from the assert statements

    def test_xmlRead (self) :
        r = StringIO.StringIO(xml1)
        b = xmlRead(r)
        self.assert_(b == "<XML>" + xml1 + "</XML>")

    def test_xmlRead_empty (self) :
        r = StringIO.StringIO("")
        b = xmlRead(r)
        # the below may be bad because we allow blank lines in input
        self.assert_(b == "<XML></XML>")

    def test_xmlRead_whitespace (self) :
        r = StringIO.StringIO(xml_whitespace)
        b = xmlRead(r)
        self.assert_(b == "<XML>" + xml_whitespace + "</XML>")

    def test_xmlRead_text (self) :
        r = StringIO.StringIO(xml_text)
        b = xmlRead(r)
        self.assert_(b == "<XML>" + xml_text + "</XML>")


    # --------
    # xmlPrint
    # --------

    def test_xmlPrint_empty (self) :
        w = StringIO.StringIO()
        ans = () # parens or empty tuple?
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "\n")

    def test_xmlPrint_tuple_1 (self) :
        w = StringIO.StringIO()
        ans = (1, 4)
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "1\n4\n\n")

    def test_xmlPrint_tuple_2 (self) :
        w = StringIO.StringIO()
        ans = (2, 2, 7)
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_xmlPrint_tuple_trash (self) :
        w = StringIO.StringIO()
        ans = (2, "trash", [1])
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "2\ntrash\n[1]\n\n")

    # --------
    # xmlSolve
    # --------

    def test_xmlSolve_1 (self) :
        r = StringIO.StringIO(xml1)
        w = StringIO.StringIO()
        xmlSolve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_xmlSolve_whitespace (self) :
        r = StringIO.StringIO(xml_whitespace)
        w = StringIO.StringIO()
        xmlSolve(r, w)
        self.assert_(w.getvalue() == "1\n2\n\n")

    def test_xmlSolve_text (self) :
        r = StringIO.StringIO(xml_text)
        w = StringIO.StringIO()
        xmlSolve(r, w)
        self.assert_(w.getvalue() == "1\n2\n\n")

    # --------
    # xmlEval
    # --------

    def test_xmlEval_easy (self) :
        sourceRoot = et.fromstring(xml_easy)
        queryRoot = et.fromstring("<Team></Team>")
        result = xmlEval(sourceRoot, queryRoot)
        self.assert_(result == [1, 1])

    def test_xmlEval_sphere (self) :
        sourceRoot = et.fromstring(xml_child_source)
        queryRoot = et.fromstring(xml_child_query)
        result = xmlEval(sourceRoot, queryRoot)
        self.assert_(result == [2, 2, 7])

    def test_xmlEval_siblings (self) :
        sourceRoot = et.fromstring(xml_child_source)
        queryRoot = et.fromstring("<Team><Cooly></Cooly><Dragon></Dragon></Team>")
        result = xmlEval(sourceRoot, queryRoot)
        self.assert_(result == [1, 7])

    def test_xmlEval_grandchildren (self) :
        sourceRoot = et.fromstring(xml_child_source)
        queryRoot = et.fromstring("<Team><Cooly><Amber></Amber></Cooly></Team>")
        result = xmlEval(sourceRoot, queryRoot)
        self.assert_(result == [1, 7])

    def test_xmlEval_mixed (self) :
        sourceRoot = et.fromstring(xml_child_source)
        queryRoot = et.fromstring("<Team><Cooly><Amber></Amber></Cooly><Dragon></Dragon></Team>")
        result = xmlEval(sourceRoot, queryRoot)
        self.assert_(result == [1, 7])

    # ----------------
    # xmlQueryToRegex
    # ----------------
    def test_xmlQueryToRegex_1 (self) :
        query = "<T></T>"
        queryroot = et.fromstring(query)
        result = xmlQueryToRegex(queryroot)
        self.assert_(result == ".//T")

    def test_xmlQueryToRegex_2 (self) :
        query = "<T> <C> <D> </D> </C> </T>"
        queryroot = et.fromstring(query)
        result = xmlQueryToRegex(queryroot)
        self.assert_(result == ".//T/C/D/../..")

    def test_xmlQueryToRegex_3 (self) :
        query = "<T> <C> </C> <D> </D> </T>"
        queryroot = et.fromstring(query)
        result = xmlQueryToRegex(queryroot)
        self.assert_(result == ".//T/C/../D/..")

    def test_xmlQueryToRegex_4 (self) :
        query = "<T> <C> <D> </D> </C> <J> </J> </T>"
        queryroot = et.fromstring(query)
        result = xmlQueryToRegex(queryroot)
        self.assert_(result == ".//T/C/D/../../J/..")

    def test_xmlQueryToRegex_text (self) :
        query = "<T> <C> test </C> more text <D> even more text </D> </T>"
        queryroot = et.fromstring(query)
        result = xmlQueryToRegex(queryroot)
        self.assert_(result == ".//T/C/../D/..")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
