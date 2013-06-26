#!/usr/bin/env python

# -------
# Imports
# -------
import StringIO
import unittest

from XML import xml_read, xml_search, xml_print, xml_solve

# -------
# TestXML
# -------
class TestXML (unittest.TestCase) :
	# ----	
	# read
	# ----	
	def test_read (self) :
		r = StringIO.StringIO("<Tester><inner></inner></Tester>\n")
		a = xml_read(r)
		assert len(list(a)) == 1

	def test_read_2 (self) :
		try :
			r = StringIO.StringIO("<Test><inner></Test></inner>")
			a = xml_read(r)
			assert False		
		except Exception, e :
			pass			

	def test_read_3 (self) :
		r = StringIO.StringIO("<Test>\n\t<inner></inner>\n\t<inner2></inner2>\n</Test>\n")
		a = xml_read(r)
		assert len(list(a)) == 1

	def test_read_4 (self) :
		r = StringIO.StringIO("<Test><inner></inner></Test><Test2><inner></inner></Test2>\n")
		a = xml_read(r)
		assert len(list(a)) == 2
		
	# ----------
	# xml_search
	# ----------
	def test_search (self) :
		r = StringIO.StringIO("<Tag1><Tag2><Tag3></Tag3><Tag4></Tag4></Tag2><Tag5></Tag5></Tag1>\n<Tag2><Tag3></Tag3></Tag2>")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2]

	def test_search_2 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3></Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5></Tag5>
					</Tag1>
					<Tag2>
						<Tag4></Tag4>
					</Tag2>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2]

	def test_search_3 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3></Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5>
							<Tag2>
								<Tag4></Tag4>
							</Tag2>
						</Tag5>
					</Tag1>
					<Tag2>
						<Tag4></Tag4>
					</Tag2>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2, 6]

	def test_search_4 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3></Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5></Tag5>
					</Tag1>
					<Tag2>
						<Tag3></Tag3>
						<Tag4></Tag4>
					</Tag2>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2]

	def test_search_5 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3></Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5></Tag5>
					</Tag1>
					<Tag2>
						<Tag4></Tag4>
						<Tag3></Tag3>
					</Tag2>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2]

	def test_search_6 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3>
								<Tag8></Tag8>
							</Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5></Tag5>
					</Tag1>
					<Tag2>
						<Tag4>
							<Tag8></Tag8>
						</Tag4>
					</Tag2>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == []

	def test_search_7 (self) :
		r = StringIO.StringIO("""<Tag1>
					 	<Tag2>
							<Tag3>
								<Tag8></Tag8>
							</Tag3>
							<Tag4></Tag4>
						</Tag2>
						<Tag5></Tag5>
					</Tag1>
					<Tag1>
						<Tag2>
						</Tag2>
					</Tag1>""")
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [1]

	def test_search_8 (self) :
		r = StringIO.StringIO("""
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
			<Team><Cooly></Cooly></Team> """)
		tmp = xml_read(r)
		matches = xml_search(list(tmp)[0], list(tmp)[1])
		assert matches == [2, 7]

	# -----	
	# print
	# -----
	def test_print (self) :
		w = StringIO.StringIO()
		matches = [2, 7]
		xml_print(matches, w)
		assert(w.getvalue() == "2\n2\n7\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		matches = []
		xml_print(matches, w)
		assert(w.getvalue() == "0\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		matches = ["abc", "def"]
		xml_print(matches, w)
		assert(w.getvalue() == "2\nabc\ndef\n")

	
	# -----
	# solve
	# -----
	def test_solve (self) :
		r = StringIO.StringIO("""
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
             <Team><Cooly></Cooly></Team> """)
		w = StringIO.StringIO()
		xml_solve(r, w)
		assert(w.getvalue() == "2\n2\n7\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("<T1></T1><T1></T1>")
		w = StringIO.StringIO()
		xml_solve(r, w)
		assert(w.getvalue() == "1\n1\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("""
			<T1>
				<T2>
					<T3>
						<T4></T4>
					</T3>
				</T2>
			</T1>
			<T2><T3><T4></T4></T3></T2>
			 """)
		w = StringIO.StringIO()
		xml_solve(r, w)
		assert(w.getvalue() == "1\n2\n")

	def test_solve_4 (self) :
		r = StringIO.StringIO("<T1></T1><T2></T2>")
		w = StringIO.StringIO()
		xml_solve(r, w)
		assert(w.getvalue() == "0\n")

	def test_solve_5 (self) :
		r = StringIO.StringIO("""
			<T1>
				<T2>
					<T3>
						<T4></T4>
					</T3>
				</T2>
			</T1>
			<T2><T3><T5></T5></T3></T2>
			 """)
		w = StringIO.StringIO()
		xml_solve(r, w)
		assert(w.getvalue() == "0\n")


# ----
# Main
# ----
print "TestXML.py"
unittest.main()
print "Done."
