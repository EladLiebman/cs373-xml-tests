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

import xml.etree.ElementTree as ET
import StringIO
import unittest

# from XML import is_nested_it, xml_search_2
# from xml_static import is_nested, xml_search
from XML import XML

#
# TestXML
#

class TestXML(unittest.TestCase) :

  # global constant:
	xml = """
	<THU>
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
	"""
	
	# global query constant
	query = " <Team> <Cooly> </Cooly> </Team> "
	query1 = " <JiaJia> <Team> </Team> </JiaJia> "
	query2 = " <Team> </Team> "
	query3 = " <Team> <Cooly> <Amber> </Amber> </Cooly> </Team> "
	
	# global XML Object
	xml_obj = XML('RunXML.in')
	
	 
	#
	# test_is_nested
	#
	def test_is_nested(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query1)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.is_nested(etree, qtree)
		self.assert_(result == True)
		
	def test_is_nested_2(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query2)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.is_nested(etree, qtree)
		self.assert_(result == True)
		
	def test_is_nested_3(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query3)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.is_nested(etree, qtree)
		self.assert_(result == True)
		
	#
	# test_xml_search
	#
	def test_xml_search(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.xml_search(etree, qtree)
		self.assert_(result == [2,[2,7]])
		
	def test_xml_search_2(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.xml_search(etree, qtree)
		self.assert_(result == [2,[2, 7]])
		
	def test_xml_search_3(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query3)
		qtree = ET.parse(fquery)
		#
		result = self.xml_obj.xml_search(etree, qtree)
		self.assert_(result == [1,[7]])
		
	#
	# test_add_root()
	#

	def test_add_root(self) :
		self.xml_obj.add_root('RunXML.in', 'testRunXML.in')
		master_tree = ET.parse('testRunXML.in')
		mroot = master_tree.getroot()
		self.assert_(mroot.tag == "ROOT")
		
	def test_add_root_2(self) :
		self.xml_obj.add_root(self.xml, 'testRunXML.in')
		master_tree = ET.parse('testRunXML.in')
		mroot = master_tree.getroot()
		self.assert_(mroot.tag == "ROOT")
		
	def test_add_root_3(self) :
		self.xml_obj.add_root(self.query, 'testRunXML.in')
		master_tree = ET.parse('testRunXML.in')
		mroot = master_tree.getroot()
		self.assert_(mroot.tag == "ROOT")
		
		
	
	


#
# main
#
# print xml

print "TestXML.py"
unittest.main()
print "Done."
	
	
