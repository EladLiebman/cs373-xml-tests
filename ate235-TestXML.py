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

from XML import xml_print, xml_eval, xml_solve

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = xml_eval("<xml>\n<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n</xml>")
        self.assert_(len(v) == 2 and v[0] == 2 and v[1] == 7)

    def test_eval_2 (self) :
        v = xml_eval("<xml>\n<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly><Dragon></Dragon></Team>\n</xml>")
        self.assert_(len(v) == 1 and v[0] == 7)

    def test_eval_3 (self) :
        v = xml_eval("<xml>\n<THU></THU>\n<OKAY></OKAY>\n</xml>")
        self.assert_(len(v) == 0)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        xml_print(w, [1,2])
        self.assert_(w.getvalue() == "2\n1\n2")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w, [200, 125])
        self.assert_(w.getvalue() == "2\n200\n125")


    def test_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w, [27, 125, 1, 2, 5])
        self.assert_(w.getvalue() == "5\n27\n125\n1\n2\n5")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly><Dragon></Dragon></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n7")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<THU></THU>\n<OKAY></OKAY>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "0")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
