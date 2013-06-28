#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET

from XML import xml_read, xml_eval, xml_print, xml_solve, read_xml_tree, id_helper, xml_traverse

# -----------
# TestXML
# -----------


class TestXML(unittest.TestCase):
    def test_read_1(self):
        r = StringIO.StringIO("<THU>\n<Cooley>\n<Hi>\n</Hi>\n</Cooley>\n</THU>\n<Cooley><Hi></Hi></Cooley>\n")
        a = xml_read(r)
        assert type(a[0]) is ET.Element
        assert type(a[1]) is ET.Element
        assert a[0].tag == "THU"
        assert a[1].tag == "Cooley"

    def test_read_2(self):
        r = StringIO.StringIO("<THU>\n<Cooley>\n<THU>\n</THU>\n</Cooley>\n</THU><THU><Cooley><THU></THU></Cooley></THU>")
        a = xml_read(r)
        assert type(a[0]) is ET.Element
        assert type(a[1]) is ET.Element
        assert a[0].tag == "THU"
        assert a[1].tag == "THU"


    def test_read_3(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        a = xml_read(r)
        assert type(a[0]) is ET.Element
        assert type(a[1]) is ET.Element
        assert a[0].tag == "THU"
        assert a[1].tag == "Team"

    def test_eval_1(self):
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        a = xml_read(r)
        assert type(a[0]) is ET.Element
        assert type(a[1]) is ET.Element
        result = xml_eval(a)
        assert(result[0][0] == 1)

    def test_eval_2(self) :
        r = StringIO.StringIO("<THU>\n<Cooley>\n<Hi>\n</Hi>\n<Bye>\n</Bye>\n</Cooley>\n</THU>\n<Cooley><Hi></Hi><Bye></Bye></Cooley>\n")
        a = xml_read(r)
        result = xml_eval(a)
        assert(result[0][0] == 1)

    def test_eval_3(self) :
        r = StringIO.StringIO("<THU>\n<Cooley>\n<Hi>\n</Hi>\n</Cooley>\n</THU>\n<Cooley><Hi></Hi><Bye></Bye></Cooley>\n")
        a = xml_read(r)
        result = xml_eval(a)
        assert(result[0][0] == 0)

    def test_eval_4(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        a = xml_read(r)
        result = xml_eval(a)
        self.assert_(result[0][0] == 2)

    def test_eval_5(self) :
        r = StringIO.StringIO("<THU>\n<Cooley>\n<Hi>\n<WHAT></WHAT>\n</Hi>\n<Bye>\n</Bye>\n</Cooley>\n</THU>\n<Cooley><Hi><NOWAY></NOWAY></Hi><Bye></Bye></Cooley>\n")
        a = xml_read(r)
        result = xml_eval(a)
        assert(result[0][0] == 0)

    def test_print_1(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        w = StringIO.StringIO()
        a = xml_read(r)
        data = xml_eval(a)
        xml_print(w, data)
        self.assert_(w.getvalue() == "1\n1\n\n")

    def test_print_2(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        a = xml_read(r)
        data = xml_eval(a)
        xml_print(w, data)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_print_3(self) :
        r = StringIO.StringIO("<THU>\n<MONKEY>\n<RED>\n</RED>\n</MONKEY>\n</THU>\n<THU><MONKEY></MONKEY></THU>\n")
        w = StringIO.StringIO()
        a = xml_read(r)
        data = xml_eval(a)
        xml_print(w, data)
        self.assert_(w.getvalue() == "1\n1\n\n")

    def test_solve_1(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n\n")

    def test_solve_2(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n\n")

    def test_solve_3(self) :
        r = StringIO.StringIO("<THU>\n<MONKEY>\n<RED>\n</RED>\n</MONKEY>\n</THU>\n<THU><MONKEY></MONKEY></THU>\n")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n\n")

    def test_solve_4(self) :
        r = StringIO.StringIO("""<and>
	<back>
		<and>
			<forth>
				<and>
					<back>
					</back>
					<forth>
					</forth>
				</and>
			</forth>
			<back>
				<and>
					<forth>
					</forth>
					<back>
					</back>
				</and>
			</back>
		</and>
	</back>
	<forth>
		<and>
			<back>
				<and>
					<back>
					</back>
					<forth>
					</forth>
				</and>
			</back>
			<forth>
				<and>
					<back>
					</back>
					<forth>
					</forth>
				</and>
			</forth>
		</and>
	</forth>
</and>
<back><and></and></back>""""")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == """3
2
8
14

""")

    def test_read_xml_tree_1(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        check = read_xml_tree(r)
        self.assert_(r.pos == 12)
        self.assert_(check == "<THU>\n</THU>")

    def test_read_xml_tree_2(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        check = read_xml_tree(r)
        check = read_xml_tree(r)
        self.assert_(r.pos == 24)
        self.assert_(check == "\n<THU></THU>")

    def test_read_xml_tree_3(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        check = read_xml_tree(r)
        self.assert_(r.pos == 182)
        self.assert_("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>")
        check = read_xml_tree(r)
        self.assert_(r.pos == 211)
        self.assert_(check == "\n<Team><Cooly></Cooly></Team>")

    def test_id_helper_1(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        a = xml_read(r)
        root = a[0]
        id_map = {root: 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        self.assert_(len(id_map.items()) == 1)

    def test_id_helper_2(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        a = xml_read(r)
        root = a[0]
        id_map = {root: 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        self.assert_(len(id_map.items()) == 11)

    def test_id_helper_3(self) :
        r = StringIO.StringIO("<THU>\n<MONKEY>\n<RED>\n</RED>\n</MONKEY>\n</THU>\n<THU><MONKEY></MONKEY></THU>\n")
        a = xml_read(r)
        root = a[0]
        id_map = {root: 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        self.assert_(len(id_map.items()) == 3)

    def test_xml_traverse_1(self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        a = xml_read(r)
        root = a[0]
        root_query = a[1]
        occurrences = [0]
        id_list = []
        query_list = [root_query]
        element_list = [root]
        first_match = [None]
        id_map = {root : 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        xml_traverse (element_list, query_list, root_query, occurrences, id_list, first_match, id_map)
        self.assert_(occurrences[0] == 2)
        self.assert_(id_list == [2, 7])

    def test_xml_traverse_2(self) :
        r = StringIO.StringIO("<THU>\n<Cooley>\n<Hi>\n</Hi>\n</Cooley>\n</THU>\n<Cooley><Hi></Hi><Bye></Bye></Cooley>\n")
        a = xml_read(r)
        root = a[0]
        root_query = a[1]
        occurrences = [0]
        id_list = []
        query_list = [root_query]
        element_list = [root]
        first_match = [None]
        id_map = {root : 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        xml_traverse (element_list, query_list, root_query, occurrences, id_list, first_match, id_map)
        self.assert_(occurrences[0] == 0)
        self.assert_(id_list == [])

    def test_xml_traverse_3(self) :
        r = StringIO.StringIO("<THU>\n</THU>\n<THU></THU>\n")
        a = xml_read(r)
        root = a[0]
        root_query = a[1]
        occurrences = [0]
        id_list = []
        query_list = [root_query]
        element_list = [root]
        first_match = [None]
        id_map = {root : 1}
        id_tracker = [2]
        id_helper(root, id_tracker, id_map)
        xml_traverse (element_list, query_list, root_query, occurrences, id_list, first_match, id_map)
        self.assert_(occurrences[0] == 1)
        self.assert_(id_list == [1])

# ----
# main
# ----

print "TestXML.py"
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    unittest.main()
print "Done."