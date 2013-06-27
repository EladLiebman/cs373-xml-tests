#!/usr/bin/env python

#
# Enam Ayivi
# aea787
# Paul Carroll
# pvc95
#


"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET

from XML import xml_read, indexTree, validatePattern, xml_solve

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
	# ----
	# read
	# ----

	def test_read_1 (self) :
		r = StringIO.StringIO("<a></a>\n<a></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0].tag ==  'a')
		self.assert_(b[1].tag == 'a')

	def test_read_2 (self) :
		r = StringIO.StringIO("<a><b></b></a>\n<a></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0][0].tag ==  'b')
		self.assert_(b[1].tag == 'a')

	def test_read_3 (self) :
		r = StringIO.StringIO("<a><b></b><c></c><d></d></a>\n<a><b><c></c></b></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0].tag ==  'a')
		self.assert_(b[0][0].tag ==  'b')
		self.assert_(b[0][1].tag ==  'c')
		self.assert_(b[0][2].tag ==  'd')
		self.assert_(b[1].tag ==  'a')
		self.assert_(b[1][0].tag ==  'b')
		self.assert_(b[1][0][0].tag ==  'c')


	# ---------
	# indexTree
	# ---------

	def test_indexTree_1 (self) :
		l = indexTree(ET.fromstring("<a></a>"))
		self.assert_(len(l) == 1)
		self.assert_(l == ['a'])

	def test_indexTree_2 (self) :
		l = indexTree(ET.fromstring("<a><b></b></a>"))
		self.assert_(len(l) == 2)
		self.assert_(l == ['a', 'b'])

	def test_indexTree_3 (self) :
		l = indexTree(ET.fromstring("<a><b><c><d></d><e></e></c></b></a>"))
		self.assert_(len(l) == 5)
		self.assert_(l == ['a', 'b', 'c', 'd', 'e'])


	# ---------------
	# validatePattern
	# ---------------

	def test_validatePattern_1 (self):
		tree1 = ET.fromstring("<a></a>")
		tree2 = ET.fromstring("<b><a></a></b>")
		b = validatePattern(tree1, tree2)
		self.assert_(b != False)

	def test_validatePattern_2 (self):
		tree1 = ET.fromstring("<a><b></b><c></c></a>")
		tree2 = ET.fromstring("<a><b><c></c></b></a>")
		b = validatePattern(tree1, tree2)
		self.assert_(b == False)

	def test_validatePattern_3 (self):
		tree1 = ET.fromstring("<d><a><b></b><c></c></a></d>")
		tree2 = ET.fromstring("<d><a><b></b><c></c></a></d>")
		b = validatePattern(tree1, tree2)
		self.assert_(b != False)

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("<d><a><b></b><c></c></a></d>\n<a><b></b><c></c></a>")
		w = StringIO.StringIO()
		xml_solve(r, w)
		print w.getvalue()
		self.assert_(w.getvalue() == "1\n2\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("<a></a>\n<a></a>")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "1\n1\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("<d><a><b></b><c></c></a></d>\n<e></e>")
		w = StringIO.StringIO()
		xml_solve(r, w)
		self.assert_(w.getvalue() == "0\n")



# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
