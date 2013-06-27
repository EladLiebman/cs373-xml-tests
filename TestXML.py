#!/usr/bin/env python

# -------------------------------
# projects/XML/TestCollatz.py
# Copyright (C) 2013
# Andres Echeverria, Arturo Lemus
# -------------------------------

"""
To test the program:
% python TestXML.py >& TestXML.out
% chmod ugo+x TestCollatz.py
% TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import os
# These are the functions to be tested.

#from XML import xml_read, xml_eval, xml_print, xml_solve, cycle_length # ?? XML.py, xml_dowhatit'ssupposedtodo 
from XML import xml_eval, print_XML

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

#    def test_read (self) :
#        r = StringIO.StringIO("1 10\n")
#        a = [0, 0]
#        b = collatz_read(r, a)
#        self.assert_(b == True)
#        self.assert_(a[0] == 1)
#        self.assert_(a[1] == 10)

    # ----
    # eval
    # ----

 
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
   
   
    

    # -----
    # solve
    # -----

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

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
