#!/usr/bin/env python

# -------
# imports
# -------

import StringIO
import xml.etree.ElementTree as ET
import unittest

from XML import *

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
	# ----
	# xml_id
	# ----

	def test_xml_id_1 (self) :
		s = "<a></a>"
		xml = ET.fromstring(s)
		r = xml_id(xml, 1)
		self.assert_(r == 1)
		self.assert_(xml.attrib.get("id") == 1)

	def test_xml_id_2 (self) :
		s = "<a><b><c><d></d></c></b></a>"
		xml = ET.fromstring(s)
		r = xml_id(xml, 1)
		self.assert_(r == 4)
		self.assert_(xml[0][0].attrib.get("id") == 3)

	def test_xml_id_3 (self) :
		s = "<a><b></b><c></c></a>"
		xml = ET.fromstring(s)
		r = xml_id(xml, 3)
		self.assert_(r == 5)
		self.assert_(xml[1].attrib.get("id") == 5)

	# ----
	# xml_read
	# ----

	def test_xml_read_1 (self) :
		r = StringIO.StringIO("<a></a><x></x>\n")
		t = xml_read(r)
		self.assert_(t[0].tag == "a")
		self.assert_(list(t[0]) == [])
		self.assert_(t[1].tag == "x")

	def test_xml_read_2 (self) :
		r = StringIO.StringIO("<a></a><x><y><z></z></y></x>\n")
		t = xml_read(r)
		self.assert_(t[0].tag == "a")
		self.assert_(len(list(t[1])) == 1)
		self.assert_(t[1][0].tag == "y")

	def test_xml_read_3 (self) :
		r = StringIO.StringIO("<a><b></b><c></c></a><x></x>\n")
		t = xml_read(r)
		self.assert_(t[0][1].tag == "c")
		self.assert_(len(list(t[0])) == 2)
		self.assert_(t[0][1].tag == "c")
	
	# -----
	# xml_search
	# -----
	
	def test_xml_search_1 (self) :
		s1 = "<a><b></b></a>"
		s2 = "<c></c>"
		main = ET.fromstring(s1)
		xml_id(main, 1)
		query = ET.fromstring(s2)
		id_list = []
		xml_search(main, query, False, id_list)
		id_list.sort()
		self.assert_(id_list == [])
	
	def test_xml_search_2 (self) :
		s1 = "<a><b><c></c></b></a>"
		s2 = "<b></b>"
		main = ET.fromstring(s1)
		xml_id(main, 1)
		query = ET.fromstring(s2)
		id_list = []
		xml_search(main, query, False, id_list)
		id_list.sort()
		self.assert_(id_list == [2])
	
	def test_xml_search_3 (self) :
		s1 = "<a><b></b><c></c></a>"
		s2 = "<a><c></c><b></b></a>"
		main = ET.fromstring(s1)
		xml_id(main, 1)
		query = ET.fromstring(s2)
		id_list = []
		xml_search(main, query, False, id_list)
		id_list.sort()
		self.assert_(id_list == [1])
		
	def test_xml_search_4 (self) :
		s1 = "<a><b><c><e></e></c></b><c><d><e></e></d></c></a>"
		s2 = "<c><e></e></c>"
		main = ET.fromstring(s1)
		xml_id(main, 1)
		query = ET.fromstring(s2)
		id_list = []
		xml_search(main, query, False, id_list)
		id_list.sort()
		self.assert_(id_list == [3])
		
	def test_xml_search_5 (self) :
		s1 = "<a><b><c></c><b></b></b></a>"
		s2 = "<b></b>"
		main = ET.fromstring(s1)
		xml_id(main, 1)
		query = ET.fromstring(s2)
		id_list = []
		xml_search(main, query, False, id_list)
		id_list.sort()
		self.assert_(id_list == [2, 4])
	
	# -----
	# xml_output
	# -----
	
	def test_xml_output_1 (self) :
		r = StringIO.StringIO("<a><b><c></c></b><c></c></a><c></c>")
		w = StringIO.StringIO()
		xml_output(r, w)
		self.assert_(w.getvalue() == "2\n3\n4\n")
	
	def test_xml_output_2 (self) :
		r = StringIO.StringIO("<a><b><c></c></b><c></c></a><e></e>")
		w = StringIO.StringIO()
		xml_output(r, w)
		self.assert_(w.getvalue() == "0\n")
 
	def test_xml_output_3 (self) :
		r = StringIO.StringIO("<c></c><c></c>")
		w = StringIO.StringIO()
		xml_output(r, w)
		self.assert_(w.getvalue() == "1\n1\n")
	
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
