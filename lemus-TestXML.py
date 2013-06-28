#!/usr/bin/env python

# -------------------------------
<<<<<<< HEAD
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

# Global node_height
node_height = 0

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
=======
# projects/XML/TestCollatz.py
# Copyright (C) 2013
# Andres Echeverria, Arturo Lemus
# -------------------------------

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestCollatz.py
% TestXML.py >& TestXML.out
>>>>>>> 261211e518c9b70200fa90d92a7b4375e55ff518
"""

# -------
# imports
# -------

import StringIO
import unittest
<<<<<<< HEAD

import xml.etree.ElementTree as ET

from XML import xml_read, xml_eval, xml_print, xml_solve, depth_search, findpath, inner_search

#Tests from https://piazza.com/class#summer2013/csw373/106.

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :

=======
import os
# These are the functions to be tested.

#from XML import xml_read, xml_eval, xml_print, xml_solve, cycle_length # ?? XML.py, xml_dowhatit'ssupposedtodo 
from XML import xml_eval, print_XML

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
>>>>>>> 261211e518c9b70200fa90d92a7b4375e55ff518
    # ----
    # read
    # ----

<<<<<<< HEAD
    #Single-line input is allowed, as-per Piazza. Input and pattern are both at root-level.
    def test_xml_read_1 (self) :
        r = StringIO.StringIO("<THU><Team></Team></THU><Team><Cooly></Cooly></Team>");
        root = xml_read(r)
        self.assert_(root.tag == "xml")

    
    #Ordered Children Occurences allowed, as-per Piazza.
    def test_xml_read_2 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<Cooly></Cooly>\n<JiaJia></JiaJia>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n");
        root = xml_read(r)
        self.assert_(root.tag == "xml")

    #Unordered Children Occurences allowed, as-per Piazza.
    def test_xml_read_3 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n");
        root = xml_read(r)
        self.assert_(root.tag == "xml")
    
=======
#    def test_read (self) :
#        r = StringIO.StringIO("1 10\n")
#        a = [0, 0]
#        b = collatz_read(r, a)
#        self.assert_(b == True)
#        self.assert_(a[0] == 1)
#        self.assert_(a[1] == 10)
>>>>>>> 261211e518c9b70200fa90d92a7b4375e55ff518

    # ----
    # eval
    # ----

<<<<<<< HEAD
    #Unordered Children Occurences. Valid input.
    def test_xml_eval_1 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)
        o = xml_eval(root);
        #print "test_xml_eval_1 -> o: ",o
        self.assert_(o    == [2])


    #Ordered Children Occurences. Valid input.
    def test_xml_eval_2 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)
        o = xml_eval(root);
        #print "test_xml_eval_2 -> o: ",o
        self.assert_(o    == [2])


    def test_xml_eval_3 (self) :
        s = "<xml>\n<THU>\n<Team></Team>\n<Cooly></Cooly>\n</THU>\n<Team><Cooly></Cooly></Team>\n</xml>"
        root = ET.fromstring(s)
        o = xml_eval(root);
        #print "test_xml_eval_3 -> o: ",o
        self.assert_(o == [0]) # Wrong output, NEEDLE is the HAYSTACK. 7th block
                               # Should return: [1]



    #-------------
    # inner_search
    #-------------
    def test_inner_search_1 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        id = 0
        for el in haystack.getiterator() :
            id += 1
            if(el.tag == needle.tag) :
                o = inner_search(el, needle) 

        self.assert_(o == True)  


    def test_inner_search_2 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        id = 0
        for el in haystack.getiterator() :
            id += 1
            if(el.tag == needle.tag) :
                o = inner_search(el, needle) 

        self.assert_(o == True) 


    def test_inner_search_3 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Cooly><Blah></Blah></Cooly>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        id = 0
        for el in haystack.getiterator() :
            id += 1
            if(el.tag == needle.tag) :
                o = inner_search(el, needle) 
        self.assert_(o == False)                       



    #-------------
    # findpath
    #-------------  
    def test_findpath_1 (self) :
        s = "<xml>\n<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        o = findpath(haystack, ".") 
        self.assert_(o == "./Team/JiaJia/../Cooly/../ACRush")


    def test_findpath_2 (self) :
        s = "<xml>\n<THU>\n<Team>\n<Cooly></Cooly>\n<JiaJia></JiaJia>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        o = findpath(needle, ".")
        self.assert_(o == "./Cooly/../JiaJia")


    def test_findpath_3 (self) :
        s = "<xml>\n<THU>\n<Team></Team>\n<Cooly></Cooly>\n</THU>\n<Team><Cooly><Blah></Blah></Cooly></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        o = findpath(haystack, ".")
        self.assert_(o == "./Team/../Cooly")   
    #-------------
    # depth_search
    #-------------
    def test_depth_search_1 (self) :
        s = "<xml>\n<THU>\n<Team>\n<Cooly></Cooly>\n<JiaJia></JiaJia>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]


        global node_height
        for el in needle.getiterator() :
            node_height = depth_search(needle, el)

        self.assert_(node_height == 1)

        
    def test_depth_search_2 (self) :
        s = "<xml>\n<THU>\n<Team>\n<Cooly></Cooly>\n<JiaJia></JiaJia>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]

        global node_height
        for el in haystack.getiterator() :
            if(el.tag == "JiaJia") :
                node_height = depth_search(haystack, el)           

        self.assert_(node_height == 2)


    def test_depth_search_3 (self) :
        s = "<xml>\n<THU>\n<Team>\n<Cooly></Cooly>\n<JiaJia></JiaJia>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>\n</xml>"
        root = ET.fromstring(s)

        # Haystack is first child of <xml> root
        haystack = list(root)[0]

        # Needle is seconde child of <xml> root
        needle = list(root)[1]
               
        global node_height
        for el in haystack.getiterator() :
            if(el.tag == "ACRush") :
                node_height = depth_search(haystack, el)           

        self.assert_(node_height == 1)       



    # -----
    # print
    # -----

    def test_xml_print (self) :
        w = StringIO.StringIO()
        xml_print(w, [2,7])
        self.assert_(w.getvalue() == "2\n2\n7\n\n")
    
    def test_xml_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w, [])
        self.assert_(w.getvalue() == "0\n\n")

    def test_xml_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w, [1])
        self.assert_(w.getvalue() == "1\n1\n\n")        


=======
 
    def test_eval_1 (self) :
        filename = "Test.in"
        f = open(filename, 'wb')
        f.write('''<THU>
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
<Team><Cooly></Cooly></Team>''')
        f.close()        
        #f.write(xml_eval())
        results = xml_eval(filename)
        os.remove("Test.in")
        self.assert_(results == [2, 2, 7])

    def test_eval_2 (self) :
        filename = "Test.in"
        f = open(filename, 'wb')
        f.write('''<X>
        <B>
            <A>
                <B>
                </B>
                <C>
                </C>
                <D>
                </D>
            </A>
        </B>
</X>
<A><B></B><C></C><D></D></A>''')
        f.close()      
        #f.write(xml_eval())
        results = xml_eval(filename)
        os.remove("Test.in")
        self.assert_(results == [1,3])

    def test_eval_3 (self) :
        filename = "Test.in"
        f = open(filename, 'wb')
        f.write('''<THU>
    <Team>
        <ACRush></ACRush>
        <Jelly></Jelly>
        <Cooly></Cooly>
        <Dragon></Dragon>
    </Team>
    <JiaJia>
        <Team>
            <Ahyangyi></Ahyangyi>
            <Dragon></Dragon>
            <Cooly><Amber></Amber></Cooly>
        </Team>
    <Team>
        <Cooly>
        </Cooly>
        <Dragon>
        </Dragon>
    </Team>
    </JiaJia>
</THU>
<Team><Cooly></Cooly><Dragon></Dragon></Team>''')
        f.close()        
        #f.write(xml_eval())
        results = xml_eval(filename)
        os.remove("Test.in")
        self.assert_(results == [3,2,8,13])
   
   
    
>>>>>>> 261211e518c9b70200fa90d92a7b4375e55ff518

    # -----
    # solve
    # -----

<<<<<<< HEAD
    def test_xml_solve_1 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<JiaJia></JiaJia>\n<Cooly></Cooly>\n</Team>\n<ACRush></ACRush>\n</THU>\n<Team><Cooly></Cooly><JiaJia></JiaJia></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n2\n\n")
    
    def test_xml_solve_2 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")
    
    def test_xml_solve_3 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_xml_solve_4 (self) :
        r = StringIO.StringIO("<ExS>\n<GiGjGVWP>\n<yiyDYZqc>\n<iKCRc>\n</iKCRc>\n</yiyDYZqc>\n</GiGjGVWP>\n</ExS>\n<ExS>\n<GiGjGVWP>\n<yiyDYZqc>\n<iKCRc>\n</iKCRc>\n</yiyDYZqc>\n</GiGjGVWP>\n</ExS>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n\n")
    
    def test_xml_solve_5 (self) :
        r = StringIO.StringIO("<yvOthoUY>\n<ozkDstpr>\n<wpEVxQQ>\n</wpEVxQQ>\n</ozkDstpr>\n<EwuuLQ>\n</EwuuLQ>\n</yvOthoUY>\n<yvOthoUY>\n<ozkDstpr>\n<wpEVxQQ>\n</wpEVxQQ>\n</ozkDstpr>\n<EwuuLQ>\n</EwuuLQ>\n</yvOthoUY>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "0\n\n")        
    
=======
#    def test_solve (self) :
#        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    # ----
    # new unit tests for my own cycle_length function
    # ----

#    def test_cycle_length (self) :
#        c = 5
#        self.assert_(cycle_length(c) == 6)
>>>>>>> 261211e518c9b70200fa90d92a7b4375e55ff518

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
