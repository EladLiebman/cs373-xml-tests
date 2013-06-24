#!/usr/bin/env python

# ----------------------------
# cs373-xml/TestXML.py
# (C)2013 Stephen Chiang
# ----------------------------

'''
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
'''

# -------
# imports
# -------
import StringIO, unittest
import xml.etree.ElementTree as ET
from XML import xml_read, xml_eval, xml_solve


# -------
# TestXML
# -------
class TestXML (unittest.TestCase):
    # ----
    # read
    # ----
    def test_read_example_whitespace(self):
        xml = "<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "THU")
        self.assertEqual(treeList[1].tag, "Team")
        
    def test_read_example_no_whitespace(self):
        xml = "<Hello><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n<Team><Cooly></Cooly></Team></Hello><GoodBye></GoodBye>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "Hello")
        self.assertEqual(treeList[1].tag, "GoodBye")
        
    def test_read_multiple_inputs_no_whitespace(self):
        xml = "<one><five></five></one><two></two><three></three><four></four>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "one")
        self.assertEqual(treeList[1].tag, "two")
        self.assertEqual(treeList[2].tag, "three")
        self.assertEqual(treeList[3].tag, "four")
        
    def test_read_multiple_inputs_whitespace(self):
        xml = "<one><five>\n\n\t</five>\t\t\t\t\n</one><two>\n</two>\t\n<three></three>\n\t\n<four></four>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "one")
        self.assertEqual(treeList[1].tag, "two")
        self.assertEqual(treeList[2].tag, "three")
        self.assertEqual(treeList[3].tag, "four")
        
    def test_read_nested_tags(self):
        xml = "<THU><Team><THU><Cooly><Team></Team></Cooly></THU></Team></THU><Team><Cooly></Cooly></Team>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "THU")
        self.assertEqual(treeList[1].tag, "Team")
        
    def test_read_ordered_with_spaces(self):
        xml = "<THU><Team><Cooly></Cooly>    <JiaJia></JiaJia>     </Team>     <ACRush></ACRush> </THU> <Team><Cooly></Cooly><JiaJia></JiaJia></Team>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "THU")
        self.assertEqual(treeList[1].tag, "Team")
        
    def test_read_unordered_with_spaces(self):
        xml = "<THU> <Team>    <JiaJia></JiaJia>    <Cooly></Cooly>    </Team>     <ACRush></ACRush> </THU> <Team><Cooly></Cooly><JiaJia></JiaJia></Team>"
        treeList = xml_read(xml)
        self.assertEqual(treeList[0].tag, "THU")
        self.assertEqual(treeList[1].tag, "Team")
        
    # ----
    # eval
    # ----
    def test_eval_example_1(self):
        haystack = ET.fromstring("<THU>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</THU>")
        needle = ET.fromstring("<THU><Cooly></Cooly></THU>")
        val = xml_eval(needle, haystack)
        self.assertEqual(val, 1)

    def test_eval_example_2(self):
        haystack = ET.fromstring("<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>")
        needle = ET.fromstring("<Team><Cooly></Cooly></Team>")
        val = xml_eval(needle, haystack)
        self.assertEqual(val, 1)
        
    def test_eval_unordered_children(self):
        haystack = ET.fromstring("<Team><JiaJia></JiaJia><Cooly></Cooly></Team>")
        needle = ET.fromstring("<Team><Cooly></Cooly><JiaJia></JiaJia></Team>")
        val = xml_eval(needle, haystack)
        self.assertEqual(val, 1)
        
    def test_eval_not_found(self):
        haystack = ET.fromstring("<Team><Cooly></Cooly></Team>")
        needle = ET.fromstring("<Team><notFound></notFound></Team>")
        val = xml_eval(needle, haystack)
        self.assertEqual(val, 0)

    # -----
    # solve
    # -----
    def test_solve_root_found(self):
        r = StringIO.StringIO("<Team></Team><Team></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "1\n1\n\n")

    def test_solve_root_not_found(self):
        r = StringIO.StringIO("<THU></THU><Team></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "0\n\n")

    def test_solve_whitespace(self):
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "2\n2\n7\n\n")

    def test_solve_no_whitespace(self):
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "2\n2\n7\n\n")
        
    def test_solve_ordered(self):
        r = StringIO.StringIO("<THU><Team><Cooly></Cooly><JiaJia></JiaJia></Team><ACRush></ACRush></THU><Team><Cooly></Cooly><JiaJia></JiaJia></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "1\n2\n\n")
        
    def test_solve_unordered(self):
        r = StringIO.StringIO("<THU><Team><JiaJia></JiaJia><Cooly></Cooly></Team><ACRush></ACRush></THU><Team><Cooly></Cooly><JiaJia></JiaJia></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "1\n2\n\n")
        
    def test_solve_not_found(self):
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team><notFound></notFound>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "0\n\n")
        
    def test_solve_multiple_inputs(self):
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team><notFound></notFound><Team><Cooly></Cooly></Team><Team></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEqual(w.getvalue(), "0\n\n1\n1\n\n")

# ----
# main
# ----
print "TestXML.py"
unittest.main()
print "Done."
