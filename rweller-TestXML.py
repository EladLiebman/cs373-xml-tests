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

from XML import xml_read, xml_eval, xml_print, xml_solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = ['<a><b></b></a>', '<a></a>']
        c = []
        b = xml_read(r, c)
        self.assert_(b    == True)
        self.assert_(r ==  [])
        self.assert_(c == ['<a><b></b></a>', '<a></a>'])

    def test_read_2 (self) :
        r = ['<a><b></b></a>', '\n','<a></a>']
        c = []
        b = xml_read(r, c)
        self.assert_(b    == True)
        self.assert_(r ==  ['<a></a>'])
        self.assert_(c == ['<a><b></b></a>'])

    def test_read_3 (self) :
        r = ['<a><b></b></a>', '<c></c>','\n','<a></a>']
        c = []
        b = xml_read(r, c)
        self.assert_(b    == True)
        self.assert_(r ==  ['<a></a>'])
        self.assert_(c == ['<a><b></b></a>', '<c></c>'])

    def test_read_4 (self) :
        r = ['<a><b></b></a>', '<c></c>','\n','<a></a>', '<c></c>']
        c = []
        b = xml_read(r, c)
        self.assert_(b    == True)
        self.assert_(r ==  ['<a></a>', '<c></c>'])
        self.assert_(c == ['<a><b></b></a>', '<c></c>'])

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = xml_eval('<THU> <Team> <ACRush></ACRush><Jelly></Jelly><Cooly></Cooly> </Team> </THU>', '<Team><ACRush></ACRush></Team>')
        self.assert_(v == [1, 2])

    def test_eval_2 (self) :
        v = xml_eval('''<THU>
                            <Team>
                                <ACRush></ACRush>
                                <Jelly></Jelly>
                                <Cooly></Cooly>
                            </Team>
                            <JiaJia>
                                <Team>
                                    <Ahyangyi></Ahyangyi>
                                    <Dragon></Dragon>
                                    <Cooly><Amber></Amber></Cooly>
                                </Team>
                            </JiaJia>
                        </THU>''', '<Team><Cooly></Cooly></Team>')
        self.assert_(v == [2, 2, 7])

    def test_eval_3 (self) :
        v = xml_eval('''<THU>
                            <Team>
                                <ACRush></ACRush>
                                <Jelly></Jelly>
                                <Cooly></Cooly>
                            </Team>
                            <JiaJia>
                                <Team>
                                    <Ahyangyi></Ahyangyi>
                                    <Dragon></Dragon>
                                    <Cooly><Amber></Amber></Cooly>
                                </Team>
                            </JiaJia>
                        </THU>''', '<Team><Ahyangyi></Ahyangyi><Cooly><Amber></Amber></Cooly><Dragon></Dragon></Team>')
        self.assert_(v == [1,7])
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        xml_print(w, [1, 2, 3])
        self.assert_(w.getvalue() == "1\n2\n3\n\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w, [100, 200, 125])
        self.assert_(w.getvalue() == "100\n200\n125\n\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w, [201, 210, 89])
        self.assert_(w.getvalue() == "201\n210\n89\n\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        xml_print(w, [900, 1000, 174])
        self.assert_(w.getvalue() == "900\n1000\n174\n\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("""<THU>
                                    <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                    </Team>
                                    <JiaJia>
                                        <Team>
                                            <Ahyangyi></Ahyangyi>
                                            <Dragon></Dragon>
                                            <Cooly><Amber></Amber></Cooly>
                                        </Team>
                                    </JiaJia>
                                </THU>
                                <Team><Cooly></Cooly></Team>""")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("""<THU>
                                    <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                    </Team>
                                    <JiaJia>
                                        <Team>
                                            <Ahyangyi></Ahyangyi>
                                            <Dragon></Dragon>
                                            <Cooly><Amber></Amber></Cooly>
                                        </Team>
                                    </JiaJia>
                                </THU>
                                <JiaJia><Team><Cooly><Amber></Amber></Cooly><Dragon></Dragon></Team></JiaJia>""")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n6\n\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("""<THU>
                                    <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                    </Team>
                                </THU>
                                <Team><ACRush></ACRush><Jelly></Jelly></Team>""")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n2\n\n")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
