import StringIO, unittest
import xml.etree.ElementTree as ET

from XML import xml_read, xml_eval, xml_print, xml_solve,\
                build_pattern_list, xml_search, check_match, index_check, index


#------------
#Test strings
#------------

xml_1 = "<THU>\n"\
    + "\t<Team>\n"\
    + "\t\t<ACRush></ACRush>\n"\
    + "\t\t<Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team>\n"\
    + "\t\t\t<Ahyangyi></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU>\n"\
    + "<Team><Cooly></Cooly></Team>"
    
xml_2 =  "<THU>\n"\
    + "\t<Team>\n"\
    + "\t\t<ACRush></ACRush>\n"\
    + "\t\t<Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team>\n"\
    + "\t\t\t<Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU>\n"\
    + "<Team><Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi></Team>"
    
xml_3 = "<THU><Team>"\
    + "    <ACRush></ACRush> <Jelly></Jelly>"\
    + "        <Cooly></Cooly>"\
    + "    </Team>"\
    + "    <JiaJia>"\
    + "        <Team>"\
    + "   <Ahyangyi></Ahyangyi>"\
    + "            <Dragon></Dragon>"\
    + "            <Cooly><Amber></Amber></Cooly>    "\
    + "        </Team>"\
    + "    </JiaJia>"\
    + "</THU><Team><Cooly></Cooly></Team>"
    
xml_4 = "<one><elem></elem></one><two><elem></elem></two><three>"\
    + "<elem></elem></three><four><elem></elem></four>"
    
xml_5 =  "<THU><Team>\n"\
    + "<ACRush></ACRush><Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team><Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU><Team><Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi></Team>"
    
xml_6 = "<THU>\n"\
    + "\t<Team>\n"\
    + "\t\t<ACRush></ACRush>\n"\
    + "\t\t<Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team>\n"\
    + "\t\t\t<Ahyangyi></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU>\n"\
    + "<Jelly></Jelly>"
    
xml_7 =  "<THU><Team>\n"\
    + "<ACRush></ACRush><Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team><Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU><Jelly></Jelly>"
    
et_1_xml = "<THU>\n"\
    + "\t<Team>\n"\
    + "\t\t<ACRush></ACRush>\n"\
    + "\t\t<Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team>\n"\
    + "\t\t\t<Ahyangyi></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU>\n"\
    
et_1_pattern = "<Team><Cooly></Cooly></Team>"

et_2_xml =  "<THU>\n"\
    + "\t<Team>\n"\
    + "\t\t<ACRush></ACRush>\n"\
    + "\t\t<Jelly></Jelly>\n"\
    + "\t\t<Cooly></Cooly>\n"\
    + "\t</Team>\n"\
    + "\t<JiaJia>\n"\
    + "\t\t<Team>\n"\
    + "\t\t\t<Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi>\n"\
    + "\t\t\t<Dragon></Dragon>\n"\
    + "\t\t\t<Cooly><Amber></Amber></Cooly>\n"\
    + "\t\t</Team>\n"\
    + "\t</JiaJia>\n"\
    + "</THU>\n"
    
et_2_pattern = "<Team><Ahyangyi><Gha><Jhi></Jhi></Gha></Ahyangyi></Team>"

et_3_pattern = "<Team><none></none></Team>"

et_4_pattern = "<Jelly></Jelly>"

class TestXML (unittest.TestCase):
    
    #----
    #Read
    #----
        
    def test_read_1 (self) :
        r = StringIO.StringIO(xml_1)
        tree = xml_read(r)
        self.assert_(type(tree) is list)
        self.assert_(tree[0].tag == "THU")
        self.assert_(tree[1].tag == "Team")
        
    def test_read_2 (self) :
        r = StringIO.StringIO(xml_2)
        tree = xml_read(r)
        self.assert_(type(tree) is list)
        self.assert_(tree[0].tag == "THU")
        self.assert_(tree[1].tag == "Team")
        
    def test_read_3 (self) :
        r = StringIO.StringIO(xml_3)
        tree = xml_read(r)
        self.assert_(type(tree) is list)
        self.assert_(tree[0].tag == "THU")
        self.assert_(tree[1].tag == "Team")
        
    def test_read_4 (self) :
        r = StringIO.StringIO(xml_4)
        tree = xml_read(r)
        self.assert_(type(tree) is list)
        self.assert_(tree[0].tag == "one")
        self.assert_(tree[1].tag == "two")
    #----
    #Eval
    #----
     
    #Pattern depth = 0
    def test_eval_1(self) :
        tree = ET.ElementTree(ET.fromstring(et_1_xml)).getroot()
        pattern_tree = ET.ElementTree(ET.fromstring(et_4_pattern))
        pattern_root = pattern_tree.getroot()
        pattern = [pattern_root.tag]
        build_pattern_list(pattern_root, pattern)
        result = xml_eval(tree, pattern)
        self.assert_(result == [1,[4]])
        
    #Pattern depth = 1
    def test_eval_2(self) :
        tree = ET.ElementTree(ET.fromstring(et_1_xml)).getroot()
        pattern_tree = ET.ElementTree(ET.fromstring(et_1_pattern))
        pattern_root = pattern_tree.getroot()
        pattern = [pattern_root.tag]
        build_pattern_list(pattern_root, pattern)
        result = xml_eval(tree, pattern)
        self.assert_(result == [2,[2,7]])
        
    #Pattern depth = 3
    def test_eval_3(self) :
        tree = ET.ElementTree(ET.fromstring(et_2_xml)).getroot()
        pattern_tree = ET.ElementTree(ET.fromstring(et_2_pattern))
        pattern_root = pattern_tree.getroot()
        pattern = [pattern_root.tag]
        build_pattern_list(pattern_root, pattern)
        result = xml_eval(tree, pattern)
        self.assert_(result == [1,[7]])
        
    #No match
    def test_eval_4(self) :
        tree = ET.ElementTree(ET.fromstring(et_2_xml)).getroot()
        pattern_tree = ET.ElementTree(ET.fromstring(et_3_pattern))
        pattern_root = pattern_tree.getroot()
        pattern = [pattern_root.tag]
        build_pattern_list(pattern_root, pattern)
        result = xml_eval(tree, pattern)
        self.assert_(result == [0,[]])
        
    #-----
    #Print
    #-----
    
    #No input
    def test_print_1(self):
        w = StringIO.StringIO()
        xml_print(w, [0, []])
        self.assert_(w.getvalue() == "0\n\n")
        
    #Single input
    def test_print_2(self):
        w = StringIO.StringIO()
        xml_print(w, [1, [4]])
        self.assert_(w.getvalue() == "1\n4\n\n")
        
    #Multiple inputs
    def test_print_3(self):
        w = StringIO.StringIO()
        xml_print(w, [2, [3, 7]])
        self.assert_(w.getvalue() == "2\n3\n7\n\n")
    
    #-----
    #Solve
    #-----
        
    #Correctly formatted, pattern depth = 0
    def test_solve_1(self):
        r = StringIO.StringIO(xml_6)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n4\n\n")
        
    #Correctly formatted, pattern depth = 1
    def test_solve_2(self):
        r = StringIO.StringIO(xml_1)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")
        
    #Correctly formatted, pattern depth = 3
    def test_solve_3(self):
        r = StringIO.StringIO(xml_2)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n7\n\n")  
            
    #Poorly formatted, pattern depth = 0
    def test_solve_4(self):
        r = StringIO.StringIO(xml_7)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n4\n\n")
          
    #Poorly formatted, pattern depth = 1
    def test_solve_5(self):
        r = StringIO.StringIO(xml_3)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")
              
    #Poorly formatted, pattern depth = 3
    def test_solve_6(self):
        r = StringIO.StringIO(xml_5)
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n7\n\n")
        

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."