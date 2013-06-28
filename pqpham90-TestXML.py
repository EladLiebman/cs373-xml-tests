#!/usr/bin/env python

# -------------------
# TestXML.py
# PhillipQuang N Pham
# pqpham90
# -------------------

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

from XML import xml_read, xml_solve, xml_print

# -----------
# TestXML
# -----------

class TestCollatz (unittest.TestCase) :
	# ----
	# read
	# ----

	def test_read_1 (self) :
		r = StringIO.StringIO("<Thu>\n<Win>\n</Win>\n</Thu>\n<Win></Win>\n")
		a = xml_read(r)
		self.assert_(a[0] == "<Thu><Win></Win></Thu>")
		self.assert_(a[1].tag ==  "Win")

	def test_read_2 (self) :
		r = StringIO.StringIO("<Thu>\n<Win>\n<Nokia>\n</Nokia>\n</Win>\n" +
			"</Thu>\n<Win><Nokia></Nokia></Win>\n")
		a = xml_read(r)
		self.assert_(a[0] == "<Thu><Win><Nokia></Nokia></Win></Thu>")
		self.assert_(a[1].tag ==  "Win")

	def test_read_3 (self) :
		r = StringIO.StringIO("<Cards>\n<Yu>\n<Gi>\n<Oh>\n</Oh>\n</Gi>\n</Yu>" +
			"\n</Cards>\n<Yu><Gi><Oh></Oh></Gi></Yu>\n")
		a = xml_read(r)
		self.assert_(a[0] == "<Cards><Yu><Gi><Oh></Oh></Gi></Yu></Cards>")
		self.assert_(a[1].tag ==  "Yu")

	def test_read_4 (self) :
		r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly>" +
			"</Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi>" +
			"</Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n" +
			"</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
		a = xml_read(r)
		self.assert_(a[0] == "<THU><Team><ACRush></ACRush><Jelly></Jelly>" +
			"<Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi>" +
			"<Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia>" +
			"</THU>")
		self.assert_(a[1].tag ==  "Team")

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("<Thu>\n<Win>\n</Win>\n</Thu>\n<Win></Win>\n")
		a = xml_read(r)
		l = xml_solve(a)
		self.assert_(len(l) == 1)
		self.assert_(l[0] == 2)

	def test_solve_2 (self) :
		r = StringIO.StringIO("<Thu>\n<Win>\n<Nokia>\n</Nokia>\n</Win>\n" +
			"</Thu>\n<Win><Nokia></Nokia></Win>\n")
		a = xml_read(r)
		l = xml_solve(a)
		self.assert_(len(l) == 1)
		self.assert_(l[0] == 2)

	def test_solve_3 (self) :
		r = StringIO.StringIO("<Cards>\n<Yu>\n<Gi>\n<Oh>\n</Oh>\n</Gi>\n</Yu>" +
			"\n</Cards>\n<Yu><Gi><Oh></Oh></Gi></Yu>\n")
		a = xml_read(r)
		l = xml_solve(a)
		self.assert_(len(l) == 1)
		self.assert_(l[0] == 2)

	def test_solve_4 (self) :
		r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly>" +
			"</Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi>" +
			"</Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n" +
			"</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
		a = xml_read(r)
		l = xml_solve(a)
		self.assert_(len(l) == 2)
		self.assert_(l[1] == 7)

	# -----
	# print
	# -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		r = StringIO.StringIO("<Thu>\n<Win>\n</Win>\n</Thu>\n<Win></Win>\n")
		a = xml_read(r)
		l = xml_solve(a)
		xml_print(w, l)
		self.assert_(w.getvalue() == "1\n2\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		r = StringIO.StringIO("<Thu>\n<Win>\n<Nokia>\n</Nokia>\n</Win>\n" +
			"</Thu>\n<Win><Nokia></Nokia></Win>\n")
		a = xml_read(r)
		l = xml_solve(a)
		xml_print(w, l)
		self.assert_(w.getvalue() == "1\n2\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		r = StringIO.StringIO("<Cards>\n<Yu>\n<Gi>\n<Oh>\n</Oh>\n</Gi>\n</Yu>" +
			"\n</Cards>\n<Yu><Gi><Oh></Oh></Gi></Yu>\n")
		a = xml_read(r)
		l = xml_solve(a)
		xml_print(w, l)
		self.assert_(w.getvalue() == "1\n2\n")

	def test_print_4 (self) :
		w = StringIO.StringIO()
		r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly>" +
			"</Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi>" +
			"</Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n" +
			"</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
		a = xml_read(r)
		l = xml_solve(a)
		xml_print(w, l)
		self.assert_(w.getvalue() == "2\n2\n7\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."