#!/usr/bin/env python

# -------
# imports
# -------
import xml.etree.ElementTree as ET
import StringIO
import unittest

from XML import XML_read, XML_eval, helper, XML_write, XML_solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----
     
     def test_read_1 (self) :
          dummy = StringIO.StringIO()
          r = StringIO.StringIO("<TEMP>\n</TEMP>\n<TEMP></TEMP>")
          input = StringIO.StringIO()
          pattern = StringIO.StringIO()
          XML_read(r, dummy, input, pattern)
          self.assert_(input.getvalue() == "<TEMP></TEMP>\n")
          self.assert_(pattern.getvalue() == "<TEMP></TEMP>")
          
     def test_read_2 (self) :
          dummy = StringIO.StringIO()
          r = StringIO.StringIO("<TEMP>\n<Team>\n<Cooly>\n<Derp></Derp>\n</Cooly>\n</Team>\n</TEMP>\n<TEMP><Team></Team></TEMP>")
          input = StringIO.StringIO()
          pattern = StringIO.StringIO()
          XML_read(r, dummy, input, pattern)
          self.assert_(input.getvalue() == "<TEMP><Team>\n<Cooly>\n<Derp></Derp></Cooly>\n</Team>\n</TEMP>\n")
          self.assert_(pattern.getvalue() == "<TEMP><Team></Team></TEMP>")
          
     def test_read_3 (self) :
          dummy = StringIO.StringIO()
          r = StringIO.StringIO("<A>\n<B>\n<C>\n<D></D>\n</C>\n<E>\n<F></F>\n</E>\n</B>\n<Z></Z>\n</A>\n<B><C><D></D></C><E><F></F></E></B>")
          input = StringIO.StringIO()
          pattern = StringIO.StringIO()
          XML_read(r, dummy, input, pattern)
          self.assert_(input.getvalue() == "<A><B>\n<C>\n<D></D></C>\n<E>\n<F></F></E>\n</B>\n<Z></Z></A>\n")
          self.assert_(pattern.getvalue() == "<B><C><D></D></C><E><F></F></E></B>")
          
     def test_read_4 (self) :
          dummy = StringIO.StringIO()
          r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
          input = StringIO.StringIO()
          pattern = StringIO.StringIO()
          XML_read(r, dummy, input, pattern)
          self.assert_(input.getvalue() == "<THU><Team>\n<ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>\n</JiaJia>\n</THU>\n")
          self.assert_(pattern.getvalue() == "<Team><Cooly></Cooly></Team>")
          
    # ------
    # helper
    # ------
          
     def test_helper_1 (self) :
          XMLroot = ET.fromstring("<TEMP>\n</TEMP>\n")
          proot = ET.fromstring("<TEMP></TEMP>")
          tmp = helper(XMLroot, proot)
          self.assert_(tmp)
     
     def test_helper_2 (self) :
          XMLroot = ET.fromstring("<TEMP>\n<Team>\n<Cooly>\n<Derp></Derp>\n</Cooly>\n</Team>\n</TEMP>\n")
          proot = ET.fromstring("<TEMP><Team></Team></TEMP>")
          tmp = helper(XMLroot, proot)
          self.assert_(tmp)
     
     def test_helper_3 (self) :
          XMLroot = ET.fromstring("<B>\n<C>\n<D></D>\n</C>\n<E>\n<F></F>\n</E>\n</B>\n")
          proot = ET.fromstring("<B><C><D></D></C><E><F></F></E></B>")
          tmp = helper(XMLroot, proot)
          self.assert_(tmp)
     
     def test_helper_4 (self) :
          XMLroot = ET.fromstring("<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n")
          proot = ET.fromstring("<Team><Cooly></Cooly></Team>")
          tmp = helper(XMLroot, proot)
          self.assert_(tmp)
     
    # ----
    # eval
    # ----
          
     def test_eval_1 (self) :
          XMLroot = ET.fromstring("<TEMP>\n</TEMP>\n")
          proot = ET.fromstring("<TEMP></TEMP>")
          result = [0]
          XML_eval(XMLroot, proot, result)
          self.assert_(result == [1, 1])
          
     def test_eval_2 (self) :
          XMLroot = ET.fromstring("<TEMP>\n<Team>\n<Cooly>\n<Derp></Derp>\n</Cooly>\n</Team>\n</TEMP>\n")
          proot = ET.fromstring("<TEMP><Team></Team></TEMP>")
          result = [0]
          XML_eval(XMLroot, proot, result)
          self.assert_(result == [1, 1])
     
     def test_eval_3 (self) :
          XMLroot = ET.fromstring("<A>\n<B>\n<C>\n<D></D>\n</C>\n<E>\n<F></F>\n</E>\n</B>\n<Z></Z>\n</A>\n")
          proot = ET.fromstring("<B><C><D></D></C><E><F></F></E></B>")
          result = [0]
          XML_eval(XMLroot, proot, result)
          self.assert_(result == [1, 2])
     
     def test_eval_4 (self) :
          XMLroot = ET.fromstring("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n")
          proot = ET.fromstring("<Team><Cooly></Cooly></Team>")
          result = [0]
          XML_eval(XMLroot, proot, result)
          self.assert_(result == [2, 2, 7])

    # -----
    # write
    # -----
     
     def test_write_1 (self) :
          w = StringIO.StringIO()
          result = [1, 1]
          XML_write(w, result)
          self.assert_(w.getvalue() == "1\n1\n")
     
     def test_write_2 (self) :
          w = StringIO.StringIO()
          result = [1, 1]
          XML_write(w, result)
          self.assert_(w.getvalue() == "1\n1\n")
     
     def test_write_3 (self) :
          w = StringIO.StringIO()
          result = [1, 2]
          XML_write(w, result)
          self.assert_(w.getvalue() == "1\n2\n")
     
     def test_write_4 (self) :
          w = StringIO.StringIO()
          result = [2, 2, 7]
          XML_write(w, result)
          self.assert_(w.getvalue() == "2\n2\n7\n")
          
    # -----
    # solve
    # -----
     
     def test_solve_1 (self) :
          r = StringIO.StringIO("<TEMP>\n</TEMP>\n<TEMP></TEMP>")
          w = StringIO.StringIO()
          XML_solve(r, w)
          self.assert_(w.getvalue() == "1\n1\n")
     
     def test_solve_2 (self) :
          r = StringIO.StringIO("<TEMP>\n<Team>\n<Cooly>\n<Derp></Derp>\n</Cooly>\n</Team>\n</TEMP>\n<TEMP><Team></Team></TEMP>")
          w = StringIO.StringIO()
          XML_solve(r, w)
          self.assert_(w.getvalue() == "1\n1\n")
     
     def test_solve_3 (self) :
          r = StringIO.StringIO("<A>\n<B>\n<C>\n<D></D>\n</C>\n<E>\n<F></F>\n</E>\n</B>\n<Z></Z>\n</A>\n<B><C><D></D></C><E><F></F></E></B>")
          w = StringIO.StringIO()
          XML_solve(r, w)
          self.assert_(w.getvalue() == "1\n2\n")
     
     def test_solve_4 (self) :
          r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
          w = StringIO.StringIO()
          XML_solve(r, w)
          self.assert_(w.getvalue() == "2\n2\n7\n")
          
# ----
# main
# ----    
    
print "TestXML.py"
unittest.main()
print "Done."
