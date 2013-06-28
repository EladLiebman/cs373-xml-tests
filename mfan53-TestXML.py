#!/usr/bin/env python

import StringIO
import unittest
import xml.etree.ElementTree as ET

from XML import xml_read, xml_solve, xml_print, xml_eval

class TestXML (unittest.TestCase):

	def test_print (self):
		w = StringIO.StringIO()
		list = [2,4,7,8]
		i = 4
		xml_print(w,i,list)
		self.assert_(w.getvalue() == "4\n2\n4\n7\n8\n\n")

	def test_print2 (self):
		w = StringIO.StringIO()
		list = [2,7]
		i = 2
		xml_print(w,i,list)
		self.assert_(w.getvalue() == "2\n2\n7\n\n")

	def test_print3 (self):
		w = StringIO.StringIO()
		list = [6,12,13,19,47,50,55]
		i = 7
		xml_print(w,i,list)
		self.assert_(w.getvalue() == "7\n6\n12\n13\n19\n47\n50\n55\n\n")

	def test_read (self):
		r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
		tree = xml_read(r)
		self.assert_(tree[0].tag == "THU")
		self.assert_(tree[1].tag == "Team")

	def test_read2 (self):
		r = StringIO.StringIO("<Swag>\n\t<Pays>\n\t\t<All></All>\n\t\t<The></The>\n\t\t<Bills></Bills>\n\t</Pays>\n\t<Hashtag>\n\t\t<Pays>\n\t\t\t<Bills></Bills>\n\t\t</Pays>\n\t</Hashtag>\n</Swag>\n<Pays><Bills></Bills></Pays>")
		tree = xml_read(r)
		self.assert_(tree[0].tag == "Swag")
		self.assert_(tree[1].tag == "Pays")

	def test_read3 (self):
		r = StringIO.StringIO("<Fluffy>\n\t<Purple>\n\t\t<Dragon></Dragon>\n\t</Purple>\n</Fluffy>\n<Fluffy><Dragon></Dragon></Fluffy>")
		tree = xml_read(r)
		self.assert_(tree[0].tag == "Fluffy")
		self.assert_(tree[1].tag == "Fluffy")

	def test_eval (self):
		line = 0
		index = 0
		pattern = ["Team","Cooly"]
		lst = []
		s = "<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>"
		tree = ET.fromstring(s)
		node = [tree]
		count = xml_eval(node,line,pattern,index,lst)
		self.assert_(count == 2)
		self.assert_(lst[0] == 2)
		self.assert_(lst[1] == 7)

	def test_eval2 (self):
		line = 0
		index = 0
		pattern = ["Purple","Dragon"]
		lst = []
		s = "<Fluffy>\n\t<Purple>\n\t\t<Dragon></Dragon>\n\t</Purple>\n</Fluffy>"
		tree = ET.fromstring(s)
		node = [tree]
		count = xml_eval(node,line,pattern,index,lst)
		self.assert_(count == 1)
		self.assert_(lst[0] == 2)

	def test_eval3 (self):
		line = 0
		index = 0
		pattern = ["Pays","Bills"]
		lst = []
		s = "<Swag>\n\t<Pays>\n\t\t<All></All>\n\t\t<The></The>\n\t\t<Bills></Bills>\n\t</Pays>\n\t<Hashtag>\n\t\t<Pays>\n\t\t\t<Bills></Bills>\n\t\t</Pays>\n\t</Hashtag>\n</Swag>"
		tree = ET.fromstring(s)
		node = [tree]
		count = xml_eval(node,line,pattern,index,lst)
		self.assert_(count == 2)
		self.assert_(lst[0] == 2)
		self.assert_(lst[1] == 7)


	def test_solve (self):
		w = StringIO.StringIO()
		r = StringIO.StringIO("<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
		xml_solve(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n")

	def test_solve2 (self):
		w = StringIO.StringIO()
		r = StringIO.StringIO("<Swag>\n\t<Pays>\n\t\t<All></All>\n\t\t<The></The>\n\t\t<Bills></Bills>\n\t</Pays>\n\t<Hashtag>\n\t\t<Pays>\n\t\t\t<Bills></Bills>\n\t\t</Pays>\n\t</Hashtag>\n</Swag>\n<Pays><Bills></Bills></Pays>")
		xml_solve(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n")

	def test_solve3 (self):
		w = StringIO.StringIO()
		r = StringIO.StringIO("<Fluffy>\n\t<Purple>\n\t\t<Dragon></Dragon>\n\t</Purple>\n</Fluffy>\n<Purple><Dragon></Dragon></Purple>")
		xml_solve(r,w)
		self.assert_(w.getvalue() == "1\n2\n\n")

print "TestXML.py"
unittest.main()
print "Done."
