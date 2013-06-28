#!/usr/bin/env python

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
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		s = xml_read(r)
		self.assert_(s    == "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>")

	def test_read_blank (self) :
		r = StringIO.StringIO("")
		s = xml_read(r)
		self.assert_(s    == "<xml></xml>")

    # ----
    # eval
    # ----

	def test_eval_1 (self) :
		s = "<xml><HI></HI><HI></HI></xml>"
		l = xml_eval(s)
		self.assert_(l    == [1])

	def test_eval_2 (self) :
		s = "<xml><HI><Hello></Hello></HI><Hello></Hello></xml>"
		l = xml_eval(s)
		self.assert_(l    == [2])

	def test_eval_3 (self) :
		s = "<xml><HI><t1><a1></a1></t1><f1><HI></HI></f1><t2></t2></HI><HI><t1></t1><t2></t2></HI></xml>"
		l = xml_eval(s)
		self.assert_(l    == [1])

	def test_eval_4 (self) :
		s = "<xml><HI><a></a></HI><HI><a></a></HI></xml>"
		l = xml_eval(s)
		self.assert_(l    == [1])

	def test_eval_5 (self) :
		s = "<xml><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></xml>"
		l = xml_eval(s)
		self.assert_(l    == [2, 7])

	def test_eval_6 (self) :
		s = "<xml><HI><a></a><b></b></HI><HI><b></b><a></a></HI></xml>"
		l = xml_eval(s)
		self.assert_(l    == [1])

    # -----
    # print
    # -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		xml_print(w, 1, [4])
		self.assert_(w.getvalue() == "1\n4\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		xml_print(w, 2, [2, 7])
		self.assert_(w.getvalue() == "2\n2\n7\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		xml_print(w, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		self.assert_(w.getvalue() == "10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")

    # -----
    # solve
    # -----
	def test_solve_1 (self) :
		r = StringIO.StringIO("<HI></HI><HI></HI>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n1\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("<HI><Hello></Hello></HI><Hello></Hello>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n2\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("<HI><t1><a1></a1></t1><f1><HI></HI></f1><t2></t2></HI><HI><t1></t1><t2></t2></HI>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n1\n")

	def test_solve_4 (self) :
		r = StringIO.StringIO("<HI><a></a></HI><HI><a></a></HI>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n1\n")


	def test_solve_5 (self) :
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "2\n2\n7\n")

	def test_solve_6 (self) :
		r = StringIO.StringIO("<HI><a></a><b></b></HI><HI><b></b><a></a></HI>\n")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n1\n")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
