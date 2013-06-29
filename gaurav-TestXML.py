#!/usr/bin/env python

# -------
# imports
# -------
import unittest
from StringIO import StringIO
import xml.etree.ElementTree as et
from XML import xml_read, xml_eval, constructXPath, xml_solve, xml_print


# -------
# TestXML
# -------
class TestXML (unittest.TestCase):
    # ----
    # read
    # ----
    
    # Testing Sphere input
    def test_read_1(self):
        xml = [ 0, 0 ]
        valid = xml_read(StringIO('<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>'), xml)
        
        self.assert_(valid)
        self.assert_(xml[0].tag == "THU")
        self.assert_(xml[1].tag == "Team")

        # Testing multiple inputs
    def test_read_2(self):
        xml = [ 0, 0 ]
        r = StringIO('<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n\n<Hello><World><Bye></Bye></World><Never><Again></Again><Bye></Bye></Never></Hello>\n<World><Bye></Bye></World>')
        valid = xml_read(r, xml)
        
        self.assert_(valid)
        self.assert_(xml[0].tag == 'THU')
        self.assert_(xml[1].tag == 'Team')
        
        valid = xml_read(r, xml)
        self.assert_(valid)
        self.assert_(xml[0].tag == 'Hello')
        self.assert_(xml[1].tag == 'World')
    
    # Testing the empty string
    def test_read_3(self):
        xml = [ 0, 0 ]
        valid = xml_read(StringIO(''), xml)
        self.assert_(not valid)
        self.assert_(xml[0] == 0)
        self.assert_(xml[1] == 0)
    
    # Testing assertions
    def test_read_4(self):
        xml = [ 0, 0 ]
        
        try:
            valid = xml_read(StringIO('<hello><why><do><YOU><say></say><goodbye></goodbye></YOU></do></why></hello>'), xml)
        except AssertionError:
            self.assert_(xml[0] == 0)
            self.assert_(xml[1] == 0)

    # ---
    # eval
    # ---
    
    # sphere input
    def test_eval_1(self):
        document = et.fromstring("""<gaurav_root><THU>
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
<Team><Cooly></Cooly></Team></gaurav_root>""")
        ids = xml_eval(document[0], document[1])
        self.assert_(ids == [ 2, 7 ])

    # No matches
    def test_eval_2(self):
        document = et.fromstring('<gaurav_root><THU></THU><Team></Team></gaurav_root>')
        ids = xml_eval(document[0], document[1])
        self.assert_(ids == [ ])
        
    # Matching entire input
    def test_eval_3(self):
        document = et.fromstring('<gaurav_root><THU><Team><ACRush></ACRush></Team></THU><THU><Team><ACRush></ACRush></Team></THU></gaurav_root>')
        ids = xml_eval(document[0], document[1])
        self.assert_(ids == [ 1 ])
        
    # Matching across siblings
    def test_eval_4(self):
        document = et.fromstring('<gaurav_root><hi><hola></hola><bye><bienvenue><bonjour></bonjour></bienvenue><howdy></howdy><pardner></pardner></bye></hi><bye><bienvenue><bonjour></bonjour></bienvenue><pardner></pardner></bye></gaurav_root>')
        ids = xml_eval(document[0], document[1])
        self.assert_(ids == [ 3 ])
        
    def test_eval_5(self):
        document = et.fromstring('<gaurav_root><hi><how><hi><how></how></hi></how><howdy><hi><whats></whats><up></up><how><blah></blah></how></hi></howdy></hi>\n<hi><how></how></hi></gaurav_root>')
        ids = xml_eval(document[0], document[1])
        self.assert_(ids == [ 1, 3, 6 ])
    
    
    # ---
    # constructXPath
    # ---
    def test_constructXPath_1(self):
        document = et.fromstring('<gaurav_root><hi><how><hi><how></how></hi></how><howdy><hi><whats></whats><up></up><how><blah></blah></how></hi></howdy></hi>\n<hi><how></how></hi></gaurav_root>')
        query = document[1]
        paths = [ ]
        constructXPath(query, '', paths)
        
        self.assert_(paths == [ 'hi/how' ])
        
    def test_constructXPath_2(self):
        document = et.fromstring('<gaurav_root><hi><hola></hola><bye><bienvenue><bonjour></bonjour></bienvenue><howdy></howdy><pardner></pardner></bye></hi>\n<bye><bienvenue><bonjour></bonjour></bienvenue><pardner></pardner></bye></gaurav_root>')       
        query = document[1]
        paths = [ ]
        constructXPath(query, '', paths)
        self.assert_(paths == [ 'bye/bienvenue/bonjour', 'bye/pardner' ])
        
    def test_constructXPath_3(self):
        document = et.fromstring('<node></node>')
        paths = [ ]
        constructXPath(document, '', paths)
        self.assert_(paths == [ 'node' ])
        
    # --- 
    # xml_print
    # ---
    def test_xml_print_1(self):
        w = StringIO()
        xml_print(w, [ 2, 7 ])
        self.assert_(w.getvalue() == '2\n2\n7\n\n')
        
    def test_xml_print_2(self):
        w = StringIO()
        xml_print(w, [ 1, 3, 6 ])
        self.assert_(w.getvalue() == '3\n1\n3\n6\n\n')
        
    def test_xml_print_3(self):
        w = StringIO()
        xml_print(w, [ ])
        self.assert_(w.getvalue() == '0\n\n')

    # ---
    # xml_solve
    # ---
    def test_xml_solve_1(self):
        w = StringIO()
        r = StringIO('')
        xml_solve(r, w)
        
        self.assert_(w.getvalue() == '')
    
    def test_xml_solve_2(self):
        r = StringIO('<THU>\n\t<Team>\n\t\t<ACRush></ACRush>\n\t\t<Jelly></Jelly>\n\t\t<Cooly></Cooly>\n\t</Team>\n\t<JiaJia>\n\t\t<Team>\n\t\t\t<Ahyangyi></Ahyangyi>\n\t\t\t<Dragon></Dragon>\n\t\t\t<Cooly><Amber></Amber></Cooly>\n\t\t</Team>\n\t</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n\n<Hello><World><Bye></Bye></World><Never><Again></Again><Bye></Bye></Never></Hello>\n<World><Bye></Bye></World>')    
        w = StringIO()
        xml_solve(r, w)
        
        self.assert_(w.getvalue() == '2\n2\n7\n\n1\n2\n\n')
        
# ----
# main
# ----
print "TestXML.py"
unittest.main()
print "Done."
