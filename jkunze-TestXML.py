
import xml.etree.ElementTree as ET
import StringIO
import unittest

from XML import SearchTreeForTree, MatchesPattern, ReadTrees, Solve_XML

class TextXML (unittest.TestCase) :
    def test_search_for_tree_simple (self) :
        tree = ET.fromstring("<a><b><c><d><e><f></f></e></d></c></b></a>");
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<b></b>"), arr, [0])
        self.assert_(arr == [2])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<c></c>"), arr, [0])
        self.assert_(arr == [3])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<d></d>"), arr, [0])
        self.assert_(arr == [4])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<e></e>"), arr, [0])
        self.assert_(arr == [5])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<f></f>"), arr, [0])
        self.assert_(arr == [6])

    def test_search_for_tree_many (self) :
        tree = ET.fromstring("<a><b><word></word></b><c><word></word></c><d></d><word></word></a>");
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<b></b>"), arr, [0])
        self.assert_(arr == [2])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<c></c>"), arr, [0])
        self.assert_(arr == [4])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<d></d>"), arr, [0])
        self.assert_(arr == [6])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<word></word>"), arr, [0])
        self.assert_(arr == [3,5,7])

    def test_search_for_tree_nested (self) :
        tree = ET.fromstring("<a><b><c><d><e><f></f></e></d></c></b></a>");
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><b></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><b><c></c></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<b><c><d></d></c></b>"), arr, [0])
        self.assert_(arr == [2])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<c><d><e></e></d></c>"), arr, [0])
        self.assert_(arr == [3])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<d><e><f></f></e></d>"), arr, [0])
        self.assert_(arr == [4])

    def test_search_for_tree_wrong_order (self) :
        tree = ET.fromstring("<a><b></b><c></c><d></d><e></e><f></f></a>");
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><c></c><b></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><d></d><b></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><e></e><b></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><e></e><b></b></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><d></d><c></c></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><e></e><c></c></a>"), arr, [0])
        self.assert_(arr == [1])
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<a><f></f><d></d></a>"), arr, [0])
        self.assert_(arr == [1])

    def test_search_for_tree_distanced (self) :
        tree = ET.fromstring("<a><x><y></y></x><b><x><y></y></x></b><c><x><q><y></y></q></x></c></a>");
        arr = []
        SearchTreeForTree(tree, ET.fromstring("<x><y></y></x>"), arr, [0])
        self.assert_(arr == [2,5])

    def test_matches_pattern_simple (self) :
        tree = ET.fromstring("<a><b><c><d><e><f></f></e></d></c></b></a>")
        self.assert_(MatchesPattern(tree, ET.fromstring("<a></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b><c></c></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b><c><d></d></c></b></a>")))
        self.assert_(~MatchesPattern(tree, ET.fromstring("<b></b>")))
        self.assert_(~MatchesPattern(tree, ET.fromstring("<a><c></c></a>")))

    def test_matches_pattern_siblings (self) :
        tree = ET.fromstring("<a><b></b><c></c><d></d><e></e></a>")
        self.assert_(MatchesPattern(tree, ET.fromstring("<a></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><c></c></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><d></d></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><e></e></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b></b><c></c></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b></b><d></d></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><b></b><e></e></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><c></c><b></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><c></c><d></d></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><c></c><e></e></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><d></d><b></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><d></d><c></c></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><d></d><e></e></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><e></e><b></b></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><e></e><c></c></a>")))
        self.assert_(MatchesPattern(tree, ET.fromstring("<a><e></e><d></d></a>")))

    def test_read_trees (self) :
        s = StringIO.StringIO("<a></a><b><x></x></b><c></c><d></d>");
        t = ReadTrees(s)
        self.assert_(t[0].tag == "a")
        self.assert_(t[1].tag == "b")
        self.assert_(t[1][0].tag == "x")
        self.assert_(t[2].tag == "c")
        self.assert_(t[3].tag == "d")
        self.assert_(len(t) == 4)

    def test_solve_xml (self) :
        i = StringIO.StringIO("<a><b><c></c><d></d></b><y><b><c></c></b><x></x></y></a><b><c></c></b>\n")
        o = StringIO.StringIO("")
        Solve_XML(i, o)
        self.assert_(o.getvalue() == "2\n2\n6")

    def test_solve_xml_find_nothing (self) :
        i = StringIO.StringIO("<a><b><c></c><d></d></b><y><b><c></c></b><x></x></y></a><joy></joy>\n")
        o = StringIO.StringIO("")
        Solve_XML(i, o)
        self.assert_(o.getvalue() == "0")

    def test_solve_xml_find_root (self) :
        i = StringIO.StringIO("<a><b><c></c><d></d></b><y><b><c></c></b><x></x></y></a><a></a>\n")
        o = StringIO.StringIO("")
        Solve_XML(i, o)
        self.assert_(o.getvalue() == "1\n1")

    def test_solve_xml_find_self (self) :
        n = 0
        a = "a"
        s = ""
        while n < 100 :
            s = "<" + a + ">" + s + "</" + a + ">"
            i = StringIO.StringIO(s + s)
            o = StringIO.StringIO("")
            Solve_XML(i, o)
            self.assert_(o.getvalue() == "1\n1")
            a += "a"
            n += 1


print "TestXML.py"
unittest.main()
print "Done."
