# -------
# imports
# -------

import StringIO
import unittest


from XML import xml_handler, xml_solver, xml_reader, xml_printer

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # xml_reader
    # ----
	def test_xml_reader_1query(self):
		r = StringIO.StringIO("<THU> </THU> <THU> </THU>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "1\n1\n\n")

	def test_xml_reader_givenExample(self):
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n")

	def test_xml_reader_givenExample_2inputs(self):
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>\n\n<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n2\n2\n7\n\n")

	# -------------
	# xml_printer
	# -------------
	def test_xml_printer_4elements(self):
		answer = {0:0, 1:1, 2:2, 3:3}
		self.assertEqual(answer[0],0)
		self.assertEqual(answer[1],1)
		self.assertEqual(answer[2],2)
		self.assertEqual(answer[3],3)

	def test_xml_printer_is0(self):
		answer = {0:0}
		self.assertEqual(answer[0],0)

	def test_xml_printer_all5(self):
		answer = {0:5, 1:5, 2:5, 3:5, 4:5, 5:5}
		self.assertEqual(answer[0],5)
		self.assertEqual(answer[1],5)
		self.assertEqual(answer[2],5)
		self.assertEqual(answer[3],5)
		self.assertEqual(answer[4],5)
		self.assertEqual(answer[5],5)

	# -------------
	# xml_handler
	# -------------	
	def test_xml_handler_is0(self):
		inputString = "<hphamnk> <THU> </THU> <B> </B> </hphamnk>"
		#r = StringIO.StringIO(inputString)
		w = StringIO.StringIO()
		answer = xml_handler(inputString)
		self.assert_(answer == {0: 0})

	def test_xml_handler_givenExample(self):
		inputString = "<hphamnk> <THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team> </hphamnk>"
		#r = StringIO.StringIO(inputString)
		w = StringIO.StringIO()
		answer = xml_handler(inputString)
		self.assert_(answer == {0: 2, 1: 2, 2: 7})

	def test_xml_handler_1occur_line1(self):
		inputString = "<hphamnk><THU></THU><THU></THU></hphamnk>"
		#r = StringIO.StringIO(inputString)
		w = StringIO.StringIO()
		answer = xml_handler(inputString)
		self.assert_(answer == {0: 1, 1: 1})

	# -----------
	# xml_solver
	# -----------
	def test_xml_solver_is0(self):
		xml = "<a> <THU> </THU> </a>"
		xml_tree = ET.ElementTree(ET.fromstring(xml))
		xml_root = xml_tree.getroot()
		query = "<a> <Fri> </Fri> </a>"
		query_tree = ET.ElementTree(ET.fromstring(query))
		query_root = query_tree.getroot()
		answer = xml_solver(xml_root,query_root)
		self.assert_(answer == 0)

	def test_xml_solver_is1(self):
		xml = "<a> <THU> </THU> </a>"
		xml_tree = ET.ElementTree(ET.fromstring(xml))
		xml_root = xml_tree.getroot()
		query = "<a> <THU> </THU> </a>"
		query_tree = ET.ElementTree(ET.fromstring(query))
		query_root = query_tree.getroot()
		answer = xml_solver(xml_root,query_root)
		self.assert_(answer == 1)

	def test_xml_solver_is1_v2(self):
		xml = "<a> <THU> </THU> <MON> </MON> </a>"
		xml_tree = ET.ElementTree(ET.fromstring(xml))
		xml_root = xml_tree.getroot()
		query = "<a> <THU> </THU> </a>"
		query_tree = ET.ElementTree(ET.fromstring(query))
		query_root = query_tree.getroot()
		answer = xml_solver(xml_root,query_root)
		self.assert_(answer == 1)

# ----
# main
# ----

import xml.etree.ElementTree as ET

print ("TestXML.py")
unittest.main()
print ("Done.")