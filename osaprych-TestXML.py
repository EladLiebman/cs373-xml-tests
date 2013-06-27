#!/usr/bin/env python

# -------------------------------
# Unit tests for XML program
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

from XML import xml_read_file, xml_split_roots, xml_data_query, xml_get_subelements, xml_depth_search, xml_det_kickoff, xml_query_check, xml_output

str0 = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>"
str1 = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly><Amber></Amber></Cooly></Team>"
str2 = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly><Hello></Hello></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia><JaJa><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JaJa></THU><Team><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly><Hello></Hello></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia><JaJa><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JaJa></THU><Team><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>"


# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # xml_read_file
    # ----
	# We wrote first three unit tests using three smaller file that are not included in turnin
	# the fourth test_read_file output too much for our TestXML.out, but they all work
	"""
	def test_read_file0(self):
		r = open('RunXML_init.in')
		a = 0
		b = xml_read_file(r, a)
		#Found length by printing from XML.py
		self.assert_(len(b) == 246)        
   
	def test_read_file1(self):
                r = open('RunXML_altered.in')
                a = 0
                b = xml_read_file(r, a)
                #Found length by printing from XML.py
                self.assert_(len(b) == 269)

	def test_read_file2(self):
		r = open('RunXML_altered2.in')
		a = 0
		b = xml_read_file(r, a)
		#Found length by printing from XML.py
		self.assert_(len(b) == 836)   

	def test_read_file0(self):
		r = open('RunXML.in')
		a = 0
		b = xml_read_file(r, a)
		#Found length by printing from XML.py
		self.assert_(len(b) == 2375950)
	"""      
	#----
	# xml_split_roots
	#----
	
	def test_split_roots0(self):
		x = "<xml>" + str0 + "</xml>"
		v = xml_split_roots(x)
		self.assert_(v[0].tag == "THU")
		self.assert_(v[1].tag == "Team")
	
	def test_split_roots1(self):
		x = "<xml>" + str1 + "</xml>"
		v = xml_split_roots(x)
                self.assert_(v[0].tag == "THU")
                self.assert_(v[1].tag == "Team")

	def test_split_roots2(self):
		x = "<xml>" + str2 + "</xml>"
		v = xml_split_roots(x)
		self.assert_(v[0].tag == "THU")
		self.assert_(v[1].tag == "Team")

	#-----
	# xml_data_query
	#-----

	def test_data_query0 (self):
		r = "<xml>" + str0 + "</xml>"
		vv = xml_split_roots(r)
               	v = xml_data_query(vv)
		#Returns query root element
		self.assert_(v.tag == "Team")

	def test_data_query1 (self):
		r = "<xml>" + str1 + "</xml>"
		vv = xml_split_roots(r)
               	v = xml_data_query(vv)
                #Returns query root element
                self.assert_(v.tag == "Team")

	def test_data_query2 (self):
		r = "<xml>" + str2 + "</xml>"
		vv = xml_split_roots(r)
               	v = xml_data_query(vv)
		#Returns query root element
		self.assert_(v.tag == "Team")


	#----
	# xml_get_subelements
	#----

	def test_get_subelements0(self):
		r = "<xml>" + str0 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
		q = vv[1]
		p = xml_get_subelements(d, q)
                #Returns true after the program has searched the tree
                self.assert_(p == True)

	def test_get_subelements1(self):
		r = "<xml>" + str1 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
		q = vv[1]
		p = xml_get_subelements(d, q)
                #Returns true after the program has searched the tree
                self.assert_(p == True)

	def test_get_subelements2(self):
		r = "<xml>" + str2 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
		q = vv[1]
		p = xml_get_subelements(d, q)
                #Returns true after the program has searched the tree
                self.assert_(p == True)

	#----
	# depth_search (recursive function)
	#----
	
	def test_depth_search0 (self) :
		r = "<xml>" + str0 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
		p = xml_depth_search(d, q)
		#Returns true if parses through children and grandchildren of parent
		self.assert_(p == True)

	def test_depth_search1 (self) :
		r = "<xml>" + str1 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_depth_search(d, q)
                #Returns true if parses through children and grandchildren of parent
                self.assert_(p == True)

	def test_depth_search2 (self) :
		r = "<xml>" + str2 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_depth_search(d, q)
                #Returns true if parses through children and grandchildren of parent
                self.assert_(p == True)
	
	#----
	# test_det_kickoff(self) :
	#----

	def test_det_kickoff1 (self) :
                r = "<xml>" + str0 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_det_kickoff(d, q)
                #Returns data element of successful kickoff function
                self.assert_(p == d)

	def test_det_kickoff0 (self) :
                r = "<xml>" + str1 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_det_kickoff(d, q)
                #Returns data element of successful kickoff function
                self.assert_(p == d)

	def test_det_kickoff2 (self) :
                r = "<xml>" + str2 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_det_kickoff(d, q)
                #Returns data element of successful kickoff function
                self.assert_(p == d)

	#----
	# test_query_check
	#----

	def test_query_check0 (self) :
                r = "<xml>" + str0 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_query_check(d, q)
                #Returns true if d == q
                self.assert_(p == "checked_query")

	def test_query_check1 (self) :
                r = "<xml>" + str1 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_query_check(d, q)
                #Returns true if d == q
                self.assert_(p == "checked_query")

	def test_query_check2 (self) :
                r = "<xml>" + str2 + "</xml>"
                vv = xml_split_roots(r)
                d = vv[0]
                q = vv[1]
                p = xml_query_check(d, q)
                #Returns true if d == q
                self.assert_(p == "checked_query")

	#---
	# test_output
	#---


	def test_output (self) :
                r = "<xml>" + str0 + "</xml>"
		s = xml_output()
                #Check num pattern occurances supposed to happen per file
                #reset_globals() was added right before this return
		self.assert_(s == 0)

	def test_output1 (self) :
                r = "<xml>" + str1 + "</xml>"
                s = xml_output()
                #Check num pattern occurances supposed to happen per file               
                self.assert_(s == 0)

	def test_output2 (self) :
                r = "<xml>" + str2 + "</xml>"
                s = xml_output()
                #Check num pattern occurances supposed to happen per file               
                self.assert_(s == 0)


	

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."


  


