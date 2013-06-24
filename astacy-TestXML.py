#!/usr/bin/env python

import os
import StringIO
import unittest
import xml.etree.ElementTree as ET
from XML import parse_input, return_list_of_indices

# this makes a dict of all of the xml fixtures in the fixtures/unit directory
# since it's easier to look at xml files than long xml strings in python source
# code
fixtures = dict((f.split('.')[0], open('fixtures/unit/' + f).read())
    for f in os.listdir('fixtures/unit'))

def build_index_list(root):
    """
    utility function that just returns the list of all tag names in an
    ElementTree or Element instance
    precondition    given an ElementTree or Element instance
    postcondition   return list of tags (strings) of all sub elements
    """
    a = []
    for child in root.iter():
        a.append(child.tag)
    return a

class TestXML(unittest.TestCase) :

    def test_return_list_of_indices_for_default_input(self):
        """
        this tests the default input from sphere
        """
        doc, query = parse_input(fixtures['default'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [2, 7])

    def test_return_list_of_indices_for_default_input_with_extra_whitespace(self):
        """
        this tests the default input where extra whitespace is added (tabs, spaces, newlines)
        """
        doc, query = parse_input(fixtures['default'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [2, 7])

    def test_return_list_of_indices_for_query_with_multiple_children(self):
        """
        this is the corner case discussed here:

            https://piazza.com/class#summer2013/csw373/99

        """
        doc, query = parse_input(fixtures['query_with_multiple_children'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [7])

    def test_return_list_of_indices_when_childrens_order_is_reversed(self):
        """
        this is the corner case discussed here:

            https://piazza.com/class#summer2013/csw373/104

        """
        doc, query = parse_input(fixtures['reversed_order'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [2])

    def test_return_list_of_indices_deeply_nested_query(self):
        """
        this checks our algorithm when we're searching for something w/ 4
        levels of nesting
        """
        doc, query = parse_input(fixtures['nested_4_levels'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [9])

    def test_return_list_of_indices_deeply_nested_with_many_children(self):
        """
        this checks our algorithm when we're searching for something w/ deep
        nesting and a lot of children. it's kind of a catch-all
        """
        doc, query = parse_input(fixtures['deep_nest_many_children'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [10, 34])

    def test_return_list_of_indices_no_matches(self):
        """
        we should get an empty list if there are no matches
        """
        doc, query = parse_input(fixtures['no_matches'])
        self.assertEqual(list(return_list_of_indices(doc, query)), [])

    def test_parse_pretty_input(self):
        pretty_input = """
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
            <Team><Cooly></Cooly></Team>
            """
        doc, query = parse_input(pretty_input)
        assert type (doc) == ET.Element
        assert type (query) == ET.Element

    def test_build_index_list(self):
        s = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>\n")
        tree = ET.parse(s)
        assert type(tree) == ET.ElementTree
        root = tree.getroot()
        assert type(root) == ET.Element
        a = build_index_list(root)
        assert a == ['THU', 'Team', 'ACRush', 'Jelly', 'Cooly', 'JiaJia', 'Team', 'Ahyangyi', 'Dragon', 'Cooly', 'Amber']


if __name__ == '__main__':
    print "TestXML.py"
    unittest.main()
    print "Done."

