#!/usr/bin/env python

# ------------------------------
# projects/xml/TestXML.py
# Rogelio R. Sanchez
# rosuto82
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

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    from xml.etree.cElementTree import XML, fromstring, tostring, ElementTree
except ImportError:
    from xml.etree.ElementTree import XML, fromstring, tostring, ElementTree

from XML import xml_print, xml_read, xml_separate, xml_eval, xml_solve


# ----------
# Test Support Data
# ----------

default_string = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n" \
                 + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>" \
                 + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n" \
                 + "</THU>\n<Team><Cooly></Cooly></Team>"

default_string2 = "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n" \
                 + "</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon>" \
                 + "</Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n" \
                 + "</THU>\n<Cooly><Amber></Amber></Cooly>"

default_query = "<Team><Cooly></Cooly></Team>"

easy_string = "<FIRST><LAST></LAST></FIRST>"

whitespace_string = "<When> <Does> \n <The> \n <Narwhale>" \
                    + "<Bacon> \n     <At>       <Midnight>" \
                    + "</Midnight></At>  </Bacon>\n  </Narwhale> </The>" \
                    + "</Does></When>"

pretty_print_string = """
                      <This>
                            <Is>
                                <Pretty>
                                        <Print>
                                        </Print>
                                </Pretty>
                            </Is>
                        </This>
                        <Query><Done></Done></Query>
                        """
singles_string = """
                <First>
                </First>
                <Last></Last>
                """

output_list_1 = [1, 2, 3]

output_list_2 = [0, 0, 0, '']

output_list_nothing = []


# ----------
# TestXML
# ----------
class TestXML(unittest.TestCase):

    # ----------
    # read
    # ----------
    def test_read(self):
        r = StringIO.StringIO(easy_string)
        tree = xml_read(r)
        b = '<XML_root>\n' + easy_string + '</XML_root>'
        b = ElementTree(fromstring(b))
        bt = b.getroot()
        b0 = bt[0].tag
        b00 = bt[0][0].tag
        treet = tree.getroot()
        tree0 = treet[0].tag
        tree00 = treet[0][0].tag
        self.assert_(b0 == tree0)
        self.assert_(b00 == tree00)

    def test_read_default_string(self):
        r = StringIO.StringIO(default_string)
        tree = xml_read(r)
        b = '<XML_root>\n' + default_string + '</XML_root>'
        b = ElementTree(fromstring(b))
        bt = b.getroot()
        b0 = bt[0].tag
        b00 = bt[0][0].tag
        b000 = bt[0][0][0].tag
        treet = tree.getroot()
        tree0 = treet[0].tag
        tree00 = treet[0][0].tag
        tree000 = treet[0][0][0].tag
        self.assert_(b0 == tree0)
        self.assert_(b00 == tree00)
        self.assert_(b000 == tree000)

    def test_whitespace_string(self):
        r = StringIO.StringIO(whitespace_string)
        tree = xml_read(r)
        b = '<XML_root>\n' + whitespace_string + '</XML_root>'
        b = ElementTree(fromstring(b))
        bt = b.getroot()
        b0 = bt[0].tag
        b00 = bt[0][0].tag
        b000 = bt[0][0][0].tag
        treet = tree.getroot()
        tree0 = treet[0].tag
        tree00 = treet[0][0].tag
        tree000 = treet[0][0][0].tag
        self.assert_(b0 == tree0)
        self.assert_(b00 == tree00)
        self.assert_(b000 == tree000)


    # ----------
    # separate
    # ----------
    def test_separate_default(self):
        test_list = []
        r = StringIO.StringIO(default_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        self.assert_(test_list[0].tag == 'THU')
        self.assert_(test_list[1].tag == 'Team')

    def test_separate_pretty(self):
        test_list = []
        r = StringIO.StringIO(pretty_print_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        self.assert_(test_list[0].tag == 'This')
        self.assert_(test_list[1].tag == 'Query')

    def test_separate_singles(self):
        test_list = []
        r = StringIO.StringIO(singles_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        self.assert_(test_list[0].tag == 'First')
        self.assert_(test_list[1].tag == 'Last')

    def test_only_one(self):
        test_list = []
        r = StringIO.StringIO(easy_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        self.assert_(test_list[0].tag == 'FIRST')

    # ----------
    # eval
    # ----------
    def test_eval_default(self):
        solve_list = [0]
        test_list = []
        r = StringIO.StringIO(default_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        xml_eval(test_list, solve_list)
        self.assert_(solve_list[0] == 2)
        self.assert_(solve_list[1] == 2)
        self.assert_(solve_list[2] == 7)

    def test_eval_no_result(self):
        solve_list = [0]
        test_list = []
        r = StringIO.StringIO(pretty_print_string)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        xml_eval(test_list, solve_list)
        self.assert_(solve_list[0] == 0)

    def test_eval_default_2(self):
        solve_list = [0]
        test_list = []
        r = StringIO.StringIO(default_string2)
        tree = xml_read(r)
        xml_separate(tree, test_list)
        xml_eval(test_list, solve_list)
        self.assert_(solve_list[0] == 1)
        self.assert_(solve_list[1] == 5)

    # ----------
    # print
    # ----------
    def test_print_easy(self):
        w = StringIO.StringIO()
        xml_print(output_list_1, w)
        self.assert_(w.getvalue() == "1\n2\n3\n")

    def test_print_nothing(self):
        w = StringIO.StringIO()
        xml_print(output_list_nothing, w)
        self.assert_(w.getvalue() == "")

    def test_print_easy2(self):
        w = StringIO.StringIO()
        xml_print(output_list_2, w)
        self.assert_(w.getvalue() == "0\n0\n0\n\n")

    # -------------
    # xml_solve
    #-------------
    def test_solve_default(self):
        f = StringIO.StringIO(default_string)
        w = StringIO.StringIO()
        xml_solve(f, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_solve_default2(self):
        f = StringIO.StringIO(default_string2)
        w = StringIO.StringIO()
        xml_solve(f, w)
        self.assert_(w.getvalue() == "1\n5\n")

    def test_solve_nothing(self):
        f = StringIO.StringIO(pretty_print_string)
        w = StringIO.StringIO()
        xml_solve(f, w)
        self.assert_(w.getvalue() == "0\n")

print "TestXML.py"
unittest.main()
print "Done."
