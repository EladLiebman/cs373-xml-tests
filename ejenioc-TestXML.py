#!/usr/bin/env python

"""
To test the program:
% python TestCollatz.py >& TestCollatz.py.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py >& TestCollatz.py.out
"""

# --------
# Imports
# --------

import StringIO
import unittest

from XML import xml_read, xml_eval, xml_print, xml_solve

# --------
# TestXML
# --------

class TestXML (unittest.TestCase):

    # ----
    # read
    # ----
    
    def test_read(self):
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n")
        key, block, path = xml_read(r)
        self.assert_(key == "./Team")
        self.assert_("".join(path) == "./Ahyangyi/../Dragon/../Cooly/Amber")

    def test_read1(self):
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        key, block, path = xml_read(r)
        self.assert_(key == "./Team")
        self.assert_("".join(path) == "./Cooly")

    def test_read2(self):
        r = StringIO.StringIO("<RADIOHEAD>\n\t<DOWN>\n\t\t<UP>\n\t\t\t<NO>\n\t\t\t\t<KARMA></KARMA>\n\t\t\t\t<LET></LET>\n\t\t\t</NO>\n\t\t</UP>\n\t</DOWN>\n\t<FITTER>\n\t\t<POLICE></POLICE>\n\t</FITTER>\n\t<UP>\n\t\t<AIRBAG>\n\t\t\t<HAPPIER></HAPPIER>\n\t\t</AIRBAG>\n\t</UP>\n</RADIOHEAD>\n<UP>\n\t<DOWN>\n\t</DOWN>\n</UP>\n")
        key, block, path = xml_read(r)
        self.assert_(key == "./UP")
        self.assert_("".join(path) == "./DOWN")

    def test_read3(self):
        r = StringIO.StringIO("<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n")
        key, block, path = xml_read(r)
        self.assert_(key == "./RADIOHEAD")
        self.assert_("".join(path) == "./THE/MUSIC/OK/../../../TOURIST/THE/../../FITTER/EXIT/WALLS/../TOURIST/../../HOMESICK/DOWN/MUSIC/../../../../UP/CLIMBING")


    # ----
    # eval
    # ----

    def test_eval(self):
        a = []
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n")
        key, block, path = xml_read(r)
        xml_eval(a, key, block, path)
        self.assert_(a == [1, 7])

    def test_eval1(self):
        a = []
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        key, block, path = xml_read(r)
        xml_eval(a, key, block, path)
        self.assert_(a == [2, 2, 7])

    def test_eval2(self):
        a = []
        r = StringIO.StringIO("<RADIOHEAD>\n\t<DOWN>\n\t\t<UP>\n\t\t\t<NO>\n\t\t\t\t<KARMA></KARMA>\n\t\t\t\t<LET></LET>\n\t\t\t</NO>\n\t\t</UP>\n\t</DOWN>\n\t<FITTER>\n\t\t<POLICE></POLICE>\n\t</FITTER>\n\t<UP>\n\t\t<AIRBAG>\n\t\t\t<HAPPIER></HAPPIER>\n\t\t</AIRBAG>\n\t</UP>\n</RADIOHEAD>\n<UP>\n\t<DOWN>\n\t</DOWN>\n</UP>\n")
        key, block, path = xml_read(r)
        xml_eval(a, key, block, path)
        self.assert_(a == [0])

    def test_eval3(self):
        a = []
        r = StringIO.StringIO("<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n")
        key, block, path = xml_read(r)
        xml_eval(a, key, block, path)
        self.assert_(a == [1,1])

    
    # -----
    # print
    # -----
  
    def test_print(self):
        w = StringIO.StringIO()
        a = [1,7]
        xml_print(w, a)
        self.assert_(w.getvalue() == "1\n7\n")

    def test_print1(self):
        w = StringIO.StringIO()
        a = [2,2,7]
        xml_print(w, a)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_print2(self):
        w = StringIO.StringIO()
        a = [0]
        xml_print(w, a)
        self.assert_(w.getvalue() == "0\n")

    def test_print3(self):
        w = StringIO.StringIO()
        a = [1,1]
        xml_print(w, a)
        self.assert_(w.getvalue() == "1\n1\n")


    # -----
    # solve
    # -----
  
    def test_solve(self):
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n7\n")

    def test_solve1(self):
        r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_solve2(self):
        r = StringIO.StringIO("<RADIOHEAD>\n\t<DOWN>\n\t\t<UP>\n\t\t\t<NO>\n\t\t\t\t<KARMA></KARMA>\n\t\t\t\t<LET></LET>\n\t\t\t</NO>\n\t\t</UP>\n\t</DOWN>\n\t<FITTER>\n\t\t<POLICE></POLICE>\n\t</FITTER>\n\t<UP>\n\t\t<AIRBAG>\n\t\t\t<HAPPIER></HAPPIER>\n\t\t</AIRBAG>\n\t</UP>\n</RADIOHEAD>\n<UP>\n\t<DOWN>\n\t</DOWN>\n</UP>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "0\n")

    def test_solve3(self):
        r = StringIO.StringIO("<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n<RADIOHEAD>\n\t<THE>\n\t\t<MUSIC>\n\t\t\t<OK></OK>\n\t\t</MUSIC>\n\t</THE>\n\t<TOURIST>\n\t\t<THE></THE>\n\t</TOURIST>\n\t<FITTER>\n\t\t<EXIT>\n\t\t\t<WALLS></WALLS>\n\t\t\t<TOURIST></TOURIST>\n\t\t</EXIT>\n\t\t<HOMESICK>\n\t\t\t<DOWN>\n\t\t\t\t<MUSIC></MUSIC>\n\t\t\t</DOWN>\n\t\t</HOMESICK>\n\t</FITTER>\n\t<UP>\n\t\t<CLIMBING></CLIMBING>\n\t</UP>\n</RADIOHEAD>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n1\n")


# --------
# Main
# --------

print "TestXML.py"
unittest.main()
print "Done."
