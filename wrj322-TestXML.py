#!/usr/bin/env python

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""


import StringIO
import unittest

from XML import extractNextBodyAndQueryXML, search, writeXML, getNextQueryResult

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase):
    



    def testExtractNextBodyAndQueryXML_01(self):

        xml = "<THU><Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU> <Team><Cooly></Cooly></Team> <THU> <Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU> <Team><Cooly></Cooly></Team>"
        gen = extractNextBodyAndQueryXML(xml)

        body, query = gen.next()

        self.assert_(body == "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        self.assert_(query == "<Team><Cooly></Cooly></Team>")

        body, query = gen.next()

        self.assert_(body == "<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>")
        self.assert_(query == "<Team><Cooly></Cooly></Team>")

        with self.assertRaises(StopIteration):
            body, query = gen.next()
  

    def testExtractNextBodyAndQueryXML_02(self):

        xml = "<xml>   467  cookie monster         674   </xml>        <query> 1`234657</query>"
        gen = extractNextBodyAndQueryXML(xml)

        body, query = gen.next()
        self.assert_(body == "<xml>467cookiemonster674</xml>")
        self.assert_(query == "<query>1`234657</query>")

        with self.assertRaises(StopIteration):
            body, query = gen.next()
  

    def testExtractNextBodyAndQueryXML_03(self):

        xml = "<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data> <blank></blank>"
        gen = extractNextBodyAndQueryXML(xml)

        body, query = gen.next()
        self.assert_(body == "<animation_data><spritesheet_folder><location>Spritesheets/Samus</location></spritesheet_folder><animation><name>facingLeft</name><filename>spritesheet_samus_standing_left</filename><first_frame>0</first_frame><last_frame>2</last_frame><fps>4</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>facingRight</name><filename>spritesheet_samus_standing_right</filename><first_frame>0</first_frame><last_frame>2</last_frame><fps>4</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>turningLeftToRight</name><filename>spritesheet_samus_turning_left_to_right</filename><first_frame>0</first_frame><last_frame>0</last_frame><fps>4</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>turningRightToLeft</name><filename>spritesheet_samus_turning_right_to_left</filename><first_frame>0</first_frame><last_frame>0</last_frame><fps>4</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>walkingLeft</name><filename>spritesheet_samus_running_left</filename><first_frame>0</first_frame><last_frame>9</last_frame><fps>22</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>walkingRight</name><filename>spritesheet_samus_running_right</filename><first_frame>0</first_frame><last_frame>9</last_frame><fps>22</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingLeftPreparing</name><filename>samus_jumping_up_facing_left</filename><first_frame>0</first_frame><last_frame>1</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingRightPreparing</name><filename>samus_jumping_up_facing_right</filename><first_frame>0</first_frame><last_frame>1</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingLeftRising</name><filename>samus_jumping_up_facing_left</filename><first_frame>2</first_frame><last_frame>2</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingRightRising</name><filename>samus_jumping_up_facing_right</filename><first_frame>2</first_frame><last_frame>2</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingLeftApex</name><filename>samus_jumping_up_facing_left</filename><first_frame>3</first_frame><last_frame>6</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingRightApex</name><filename>samus_jumping_up_facing_right</filename><first_frame>3</first_frame><last_frame>6</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingLeftFalling</name><filename>samus_jumping_up_facing_left</filename><first_frame>7</first_frame><last_frame>7</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingRightFalling</name><filename>samus_jumping_up_facing_right</filename><first_frame>7</first_frame><last_frame>7</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingLeftLanding</name><filename>samus_jumping_up_facing_left</filename><first_frame>8</first_frame><last_frame>9</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation><animation><name>jumpingUpFacingRightLanding</name><filename>samus_jumping_up_facing_right</filename><first_frame>8</first_frame><last_frame>9</last_frame><fps>15</fps><shader_name>Unlit/Transparent</shader_name></animation></animation_data>")
        self.assert_(query == "<blank></blank>")

        with self.assertRaises(StopIteration):
            body, query = gen.next()


    def testExtractNextBodyAndQueryXML_04(self):

        xml = ""
        gen = extractNextBodyAndQueryXML(xml)

        with self.assertRaises(StopIteration):
            body, query = gen.next()
 
            




    def testSearch_01(self):

        tree = ET.fromstring("<THU> <Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU>")
        
        sequence1 = ET.fromstring("<THU><Team></Team></THU>")
        sequence2 = ET.fromstring("<THU>  <Team><Cooly> hello  </Cooly></Team></THU>")
        sequence3 = ET.fromstring("<JiaJia><Cooly></Cooly></JiaJia>")
        sequence4 = ET.fromstring("<THU><Mama></Mama></THU>")
        sequence5 = ET.fromstring("<THU><Dragon></Dragon></THU>")
        sequence6 = ET.fromstring("<THU><JiaJia><Team><Ahyangyi></Ahyangyi></Team></JiaJia></THU>")

        self.assert_( search(sequence1, tree) == True  )
        self.assert_( search(sequence2, tree) == True  )
        self.assert_( search(sequence3, tree) == False )
        self.assert_( search(sequence4, tree) == False )
        self.assert_( search(sequence5, tree) == False )
        self.assert_( search(sequence6, tree) == True  )


    def testSearch_02(self):

        tree = ET.fromstring("<THU> <Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU>")
        
        sequence1 = ET.fromstring("<THU> <Team> </Team> </THU>")
        sequence2 = ET.fromstring("<Team> <Cooly> </Cooly> </Team>")
        sequence3 = ET.fromstring("<JiaJia> <Cooly> </Cooly> </JiaJia>")
        sequence4 = ET.fromstring("<THU> <Mama> </Mama> </THU>")
        sequence5 = ET.fromstring("<THU> <Dragon> </Dragon> </THU>")
        sequence6 = ET.fromstring("<THU> <JiaJia> <Team> <Ahyangyi> </Ahyangyi> </Team> </JiaJia> </THU>")

        self.assert_( search(sequence1, tree,) == True  )
        self.assert_( search(sequence2, tree,) == False )
        self.assert_( search(sequence3, tree,) == False )
        self.assert_( search(sequence4, tree,) == False )
        self.assert_( search(sequence5, tree,) == False )
        self.assert_( search(sequence6, tree,) == True  )


    def testSearch_03(self):

        tree = ET.fromstring("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data>")
        sequence1 = ET.fromstring("<animation_data> <spritesheet_folder> <location> </location> </spritesheet_folder> </animation_data>")
        sequence2 = ET.fromstring("<animation_data> <animation> <fps> </fps> </animation> </animation_data>")
        sequence3 = ET.fromstring("<animation_data> <animation> <animation> </animation> </animation> </animation_data>")
        sequence4 = ET.fromstring("<THU> <Mama> </Mama> </THU>")
        sequence5 = ET.fromstring("<THU> <Dragon> </Dragon> </THU>")
        sequence6 = ET.fromstring("<THU> <JiaJia> <Team> <Ahyangyi> </Ahyangyi> </Team> </JiaJia> </THU>")
        sequence7 = ET.fromstring("<animation_data> <animation_data> <animation> </animation> </animation_data> </animation_data>")
        sequence8 = ET.fromstring("<one> <two> <three> <animation_data> <animation> </animation> </animation_data> </three> </two> </one>")

        self.assert_( search(sequence1, tree,) == True  )
        self.assert_( search(sequence2, tree,) == True  )
        self.assert_( search(sequence3, tree,) == False )
        self.assert_( search(sequence4, tree,) == False )
        self.assert_( search(sequence5, tree,) == False )
        self.assert_( search(sequence6, tree,) == False )
        self.assert_( search(sequence7, tree,) == False  )
        self.assert_( search(sequence8, tree,) == False  )


    def testSearch_04(self):

        tree = ET.fromstring("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data>")
        sequence1 = ET.fromstring("<location> </location>")
        sequence2 = ET.fromstring("<animation> <fps> </fps> </animation>")
        sequence3 = ET.fromstring("<animation> </animation>")
        sequence4 = ET.fromstring("<spritesheet_folder> <location> </location> </spritesheet_folder>")
        sequence5 = ET.fromstring("<cookie_monster> </cookie_monster>")
        sequence6 = ET.fromstring("<animation_data> <fps> </fps> </animation_data>")

        self.assert_( True in [search(sequence1, e) for e in tree.iter()] )
        self.assert_( True in [search(sequence1, e) for e in tree.iter()] )

        self.assert_( True in [search(sequence2, e) for e in tree.iter()] )
        self.assert_( True in [search(sequence2, e) for e in tree.iter()] )

        self.assert_( True in [search(sequence3, e) for e in tree.iter()] )
        self.assert_( True in [search(sequence3, e) for e in tree.iter()] )

        self.assert_( True in [search(sequence4, e) for e in tree.iter()] )
        self.assert_( True in [search(sequence4, e) for e in tree.iter()] )

        self.assert_( not True in [search(sequence5, e) for e in tree.iter()] )
        self.assert_( not True in [search(sequence5, e) for e in tree.iter()] )

        self.assert_( not True in [search(sequence6, e) for e in tree.iter()] )
        self.assert_( not True in [search(sequence6, e) for e in tree.iter()] )


    def testSearch_05(self):

        tree = ET.fromstring("<xylem> <wetlands> <roof-garden> <dynamic> <captain> <minuscule> <safe> <protactinium> <undeveloped/> <tragedy> <beneficiary/> </tragedy> </protactinium> <nine-one-one> <confident/> </nine-one-one> </safe> </minuscule> <encounter> <disorientation> <boron> <abundance/> <oxygen> <bees/> </oxygen> </boron> <eisenhower> <ventilation> <reasonable> <seedlings/> <flexible> <warmth> <perlite> <sunshine> <palladium> <gracious> <apprehension> <air> <calcium> <personable/> </calcium> </air> </apprehension> </gracious> </palladium> </sunshine> </perlite> </warmth> </flexible> </reasonable> </ventilation> </eisenhower> </disorientation> </encounter> <protection> <active> <fallow> <aid> <balance/> </aid> </fallow> </active> <aroma> <waxed-paper> <beetles> <ununoctium/> </beetles> </waxed-paper> <stink/> </aroma> </protection> <circumstances/> <valor> <astatine> <principled/> <lithium> <perimeter/> </lithium> </astatine> <wound> <evolve/> </wound> </valor> <trust> <rain> <kit/> </rain> </trust> </captain> <courageous> <truman> <fuse/> </truman> </courageous> <kindred/> <arsenic/> </dynamic> <mother-nature> <feeding> <verdant> <risk> <deplorable/> <substance> <uplifting> <humble> <taint> <materials/> </taint> </humble> </uplifting> <iridium> <seasonal/> </iridium> <crucial> <sand> <green-thumb> <perception/> </green-thumb> </sand> <rancorous/> </crucial> <opportunity/> </substance> <niobium> <barrier> <fervid/> </barrier> </niobium> </risk> <gasoline> <struggle> <chlorine> <jubilant> <unfair> <wasps/> </unfair> </jubilant> </chlorine> <just/> </struggle> </gasoline> <extrovert> <tolerant> <silicon> <sprig/> </silicon> </tolerant> </extrovert> </verdant> <humidity> <ornamental> <smoke> <suitable> <punishment> <blooming/> <mercury> <hydrant> <euphoric> <ease/> </euphoric> </hydrant> </mercury> </punishment> <foliage> <plentiful> <inferno> <farming> <insightful> <collapse> <ruthenium> <fibrous/> </ruthenium> </collapse> <innocent/> </insightful> <kelp/> </farming> </inferno> </plentiful> <squad> <save> <trimming/> </save> </squad> </foliage> <sober/> <equipment> <opt/> </equipment> </suitable> <temperatures> <addictive> <decorative> <mercy> <trek> <anxiety> <discreet/> </anxiety> <survival> <background> <judge> <unique/> <matches> <rake> <heat-reflective-suit> <legume> <revere> <domain> <wild-fire/> </domain> </revere> </legume> </heat-reflective-suit> </rake> <indigenous/> <adrenaline> <provision/> </adrenaline> <contemptible/> </matches> </judge> </background> </survival> </trek> <noticeable/> </mercy> </decorative> <clean-up> <exultation> <preparation> <iron> <devious> <pollination> <plantings> <quench/> <zeal> <gifted> <informative/> <matches> <rake> <heat-reflective-suit> <legume> <revere> <domain> <wild-fire/> </domain> </revere> </legume> </heat-reflective-suit> </rake> <indigenous/> <adrenaline> <provision/> </adrenaline> <contemptible/> </matches> </gifted> </zeal> </plantings> <visible/> </pollination> </devious> <specie> <notorious> <indium> <beneficial> <rubidium> <pain/> </rubidium> </beneficial> </indium> </notorious> </specie> </iron> </preparation> </exultation> <retreat> <rapidity> <dense> <outspoken> <creative/> </outspoken> </dense> </rapidity> </retreat> </clean-up> </addictive> <crawl> <witty/> </crawl> </temperatures> <praseodymium> <pessimism> <prejudicial> <unit/> </prejudicial> </pessimism> </praseodymium> <facts/> </smoke> <restrict> <antagonistic> <intolerant/> </antagonistic> </restrict> <victim/> </ornamental> <daunting/> </humidity> <work> <quiver> <seed/> <participation> <bold> <burn/> </bold> </participation> </quiver> </work> <jealous/> </feeding> <investigator> <zinc> <consistent> <bone-meal/> <classification> <reagan> <charred> <uncivil> <moral> <stern> <landscape> <negative> <convenient/> <gallium/> </negative> <caution> <unforgettable> <recovery> <vengeance> <repellent> <bumper-crop/> </repellent> </vengeance> </recovery> </unforgettable> <trustworthy> <propagate> <efforts> <nixon> <nerve/> </nixon> </efforts> </propagate> </trustworthy> </caution> <yelling> <sod/> </yelling> </landscape> <alibi> <responsible> <communicative> <oriented> <amusing> <transmit> <coastal/> </transmit> </amusing> <uncontrolled> <refined> <altitude/> </refined> </uncontrolled> </oriented> </communicative> </responsible> <civil/> </alibi> </stern> <titanium> <imprudent> <entry/> </imprudent> </titanium> <limitation> <approximate> <sunlight> <conservation/> </sunlight> </approximate> </limitation> </moral> <genuine/> <defensive> <quirky> <war/> </quirky> </defensive> </uncivil> </charred> <involve> <damage> <pyrostat> <grove> <alarm/> <ford> <heat> <needles> <catalyst> <solar/> </catalyst> </needles> </heat> </ford> </grove> <fireworks/> </pyrostat> <happy> <reproductive> <phosphate/> </reproductive> </happy> </damage> <glow> <solemn> <wellies/> </solemn> </glow> </involve> <strength/> <popular/> </reagan> <nozzle> <horrifying> <juvenile> <liberal> <fury/> </liberal> </juvenile> </horrifying> </nozzle> </classification> <constructive/> </consistent> <prints> <seaborgium> <expertise> <graft> <faithful> <authoritative> <stake/> </authoritative> </faithful> </graft> </expertise> </seaborgium> <restorative/> </prints> <spade/> <deferential> <ruck-gardening> <tin> <role/> </tin> </ruck-gardening> </deferential> </zinc> </investigator> <enclosure> <orderly> <tellurium> <urgency> <erosion> <evergreen/> </erosion> </urgency> </tellurium> <holding> <polite> <authorities> <magnificence> <hygienic/> </magnificence> </authorities> </polite> </holding> </orderly> </enclosure> </mother-nature> <hero> <amazing> <open-minded> <loyal> <irrigation/> </loyal> </open-minded> </amazing> <aquatic> <lutetium> <remarkable> <focus> <snip> <grateful> <battle/> </grateful> </snip> </focus> </remarkable> </lutetium> </aquatic> </hero> <crew> <abundant/> </crew> <lawrencium> <rot> <resourceful> <devoted/> </resourceful> </rot> </lawrencium> </roof-garden> <screaming> <valiant> <toxic> <zone/> </toxic> <jurisdiction/> </valiant> <rookie> <widespread> <gauge> <busy> <implementation> <tenacious> <division> <blase> <unfamiliar> <nitrate/> </unfamiliar> </blase> </division> </tenacious> </implementation> <terror> <gloomy/> </terror> </busy> <rhythm/> </gauge> <environment/> </widespread> <soluble> <cook/> </soluble> <flash/> </rookie> <insects> <pyromania> <maturation> <forgiving/> </maturation> </pyromania> </insects> </screaming> <niche> <well-trained> <faulty> <truthful> <horror/> <impressive> <fragile> <magnet> <encroach> <quick/> <matches> <rake> <heat-reflective-suit> <legume> <revere> <domain> <wild-fire/> </domain> </revere> </legume> </heat-reflective-suit> </rake> <indigenous/> <adrenaline> <provision/> </adrenaline> <contemptible/> </matches> </encroach> </magnet> </fragile> </impressive> </truthful> <bush> <adequate> <mixture> <colorful> <watch> <speculation/> </watch> </colorful> </mixture> </adequate> </bush> <flammable> <seaweed> <brave> <meadow/> </brave> </seaweed> </flammable> </faulty> <fire-resistant> <findings> <somber/> </findings> </fire-resistant> </well-trained> <blast/> </niche> </wetlands> <nursery> <barium> <inhalation> <frailty> <ruthless> <zygophyte> <vicious> <patch> <current/> </patch> </vicious> <considerate> <erupt/> <boost/> </considerate> <uniform> <explosion/> </uniform> </zygophyte> <melt> <understanding/> </melt> </ruthless> <ladder> <fragrant> <unworthy> <fair> <heirloom/> <strontium> <xyst/> </strontium> </fair> </unworthy> </fragrant> </ladder> </frailty> <ignoble/> <assistance> <ingenuous> <change> <planter> <unidentified> <flames/> </unidentified> </planter> </change> </ingenuous> </assistance> </inhalation> <deliberate> <jocular> <haze> <diminutive/> <shift/> </haze> <assessment> <wary> <successful> <radium> <testing/> </radium> <insolent/> </successful> <bog> <fire-truck> <transplant> <sympathetic/> </transplant> </fire-truck> </bog> </wary> <guilty/> </assessment> <willingness> <detection/> <bulbs> <vineyard/> </bulbs> </willingness> </jocular> <modest> <scandium> <over-harvest> <splendid> <roto-tiller> <commissioner> <sharing/> </commissioner> </roto-tiller> <rainfall/> </splendid> <antimony/> <loving> <riot/> </loving> </over-harvest> <miserable> <muffle> <ignorant/> </muffle> </miserable> <scope/> </scandium> </modest> <brilliant/> </deliberate> <reconstruct> <edible/> </reconstruct> </barium> <dormancy> <resilient> <supplies> <grief> <hassium/> </grief> <engine-company> <nascent> <green> <ultimate/> <radon> <sour> <unruly> <claim> <iodine> <grassy> <awesome/> </grassy> </iodine> </claim> </unruly> </sour> </radon> </green> </nascent> <discovery> <expectant/> </discovery> <zirconium> <sample/> </zirconium> </engine-company> </supplies> <naive> <deciduous> <warm> <samarium> <oxidation/> </samarium> <arbor> <chemical> <till/> </chemical> </arbor> </warm> <juxtapose/> <hydrogen/> </deciduous> <preserve> <disposable/> <vital> <ensure> <irascible/> </ensure> </vital> </preserve> </naive> <headquarters> <ambulance> <inhabitant/> <weary> <conflagration/> </weary> </ambulance> <unbelievable/> </headquarters> <overgrown/> </resilient> <effective> <wind> <carbon> <flowering> <produce> <wistful/> </produce> </flowering> <impartial> <floral> <destructive/> </floral> </impartial> </carbon> <keepsake/> </wind> <dedication> <flourish/> </dedication> </effective> </dormancy> <strike> <frenzy> <yard> <innovative/> <stress> <heliotrope> <natural> <johnson> <vanadium/> </johnson> </natural> </heliotrope> </stress> </yard> <sprout> <responsive> <personal/> <flash-point/> <yielding> <quadrant/> </yielding> </responsive> <extinguish> <climate/> </extinguish> </sprout> <temperate> <needy> <exclusive> <nefarious/> </exclusive> </needy> </temperate> </frenzy> <exotic> <accident> <photosynthesis> <estimable> <genus> <eradicate/> <birds/> </genus> <cold/> </estimable> <matches> <rake> <heat-reflective-suit> <legume> <revere> <domain> <wild-fire/> </domain> </revere> </legume> </heat-reflective-suit> </rake> <indigenous/> <adrenaline> <provision/> </adrenaline> <contemptible/> </matches> </photosynthesis> <nitrogen/> </accident> </exotic> <egotistical/> </strike> <beauty> <blackened/> <solitary/> </beauty> <fermium> <fillmore> <irresponsible> <gopher/> <suffocate> <mckinley/> </suffocate> </irresponsible> </fillmore> <police/> </fermium> <prairie/> </nursery> </xylem>")
        
        sequence1 = ET.fromstring("<matches><rake><heat-reflective-suit><legume><revere><domain><wild-fire /></domain></revere></legume></heat-reflective-suit></rake><indigenous /><adrenaline><provision /></adrenaline><contemptible /></matches>")
        sequence2 = ET.fromstring("<matches><rake><heat-reflective-suit><legume><revere><domain><wild-fire /></domain>    <hellfire /></revere></legume></heat-reflective-suit></rake><indigenous /><adrenaline><provision /></adrenaline><contemptible /></matches>")
        sequence3 = ET.fromstring("<a></a>")

        self.assert_( [search(sequence1, e) for e in tree.iter()].count(True) == 4 )
        self.assert_( [search(sequence2, e) for e in tree.iter()].count(True) == 0 )
        self.assert_( [search(sequence3, e) for e in tree.iter()].count(True) == 0 )






    def testWriteXML_01(self):
        ids = [10]
        writer = StringIO.StringIO("")
        writeXML(ids, writer)

        self.assert_(writer.getvalue() == "1\n10\n")


    def testWriteXML_02(self):
        ids = [2, 7]
        writer = StringIO.StringIO("")
        writeXML(ids, writer)

        self.assert_(writer.getvalue() == "2\n2\n7\n")


    def testWriteXML_03(self):
        ids = [0, 1, 2, 18, 99, 56543, 234, 21, "a", True]
        writer = StringIO.StringIO("")
        writeXML(ids, writer)

        self.assert_(writer.getvalue() == "10\n0\n1\n2\n18\n99\n56543\n234\n21\na\nTrue\n")


    def testWriteXML_04(self):
        ids = []
        writer = StringIO.StringIO()
        writeXML(ids, writer)

        self.assert_(writer.getvalue() == "0\n")


    def testWriteXML_05(self):
        ids = "1m2m3m4m5m"
        writer = StringIO.StringIO()
        writeXML(ids, writer)

        self.assert_(writer.getvalue() == "10\n1\nm\n2\nm\n3\nm\n4\nm\n5\nm\n")
   



    def testGetNextQueryResult_01(self):
        reader = StringIO.StringIO("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data> <empty_query></empty_query>")
        q = getNextQueryResult(reader)

        ids = q.next()
        self.assert_(ids == [])

        with self.assertRaises(StopIteration):
            q.next()


    def testGetNextQueryResult_02(self):
        reader = StringIO.StringIO("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data> <animation_data> <spritesheet_folder> <location></location>   </spritesheet_folder> </animation_data>")
        q = getNextQueryResult(reader)

        ids = q.next()
        self.assert_(ids == [1])

        with self.assertRaises(StopIteration):
            q.next()


    def testGetNextQueryResult_03(self):
        reader = StringIO.StringIO("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data> <animation> <name></name> </animation>")
        q = getNextQueryResult(reader)

        ids = q.next()
        self.assert_(ids == [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95, 102, 109])

        with self.assertRaises(StopIteration):
            q.next()


    def testGetNextQueryResult_04(self):
        reader = StringIO.StringIO("<animation_data> <spritesheet_folder> <location>Spritesheets/Samus</location> </spritesheet_folder> <animation> <name>facingLeft</name> <filename>spritesheet_samus_standing_left</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>facingRight</name> <filename>spritesheet_samus_standing_right</filename> <first_frame>0</first_frame> <last_frame>2</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningLeftToRight</name> <filename>spritesheet_samus_turning_left_to_right</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>turningRightToLeft</name> <filename>spritesheet_samus_turning_right_to_left</filename> <first_frame>0</first_frame> <last_frame>0</last_frame> <fps>4</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingLeft</name> <filename>spritesheet_samus_running_left</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>walkingRight</name> <filename>spritesheet_samus_running_right</filename> <first_frame>0</first_frame> <last_frame>9</last_frame> <fps>22</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftPreparing</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightPreparing</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>0</first_frame> <last_frame>1</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftRising</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightRising</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>2</first_frame> <last_frame>2</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftApex</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightApex</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>3</first_frame> <last_frame>6</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftFalling</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightFalling</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>7</first_frame> <last_frame>7</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingLeftLanding</name> <filename>samus_jumping_up_facing_left</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> <animation> <name>jumpingUpFacingRightLanding</name> <filename>samus_jumping_up_facing_right</filename> <first_frame>8</first_frame> <last_frame>9</last_frame> <fps>15</fps> <shader_name>Unlit/Transparent</shader_name> </animation> </animation_data>                                 <last_frame>information!</last_frame> ")
        q = getNextQueryResult(reader)

        ids = q.next()
        self.assert_(ids == [8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113])

        with self.assertRaises(StopIteration):
            q.next()


    def testGetNextQueryResult_05(self):
        reader = StringIO.StringIO("<THU> <Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU> <Team><Cooly></Cooly></Team> <THU> <Team> <ACRush></ACRush> <Jelly></Jelly> <Cooly></Cooly> </Team> <JiaJia> <Team> <Ahyangyi></Ahyangyi> <Dragon></Dragon> <Cooly><Amber></Amber></Cooly> </Team> </JiaJia> </THU> <Team><Cooly></Cooly></Team> <xml></xml> <query></query> ")
        q = getNextQueryResult(reader)

        ids = q.next()
        self.assert_(ids == [2, 7])

        ids = q.next()
        self.assert_(ids == [2, 7])

        ids = q.next()
        self.assert_(ids == [])

        with self.assertRaises(StopIteration):
            q.next()


    def testGetNextQueryResult_06(self):
        reader = StringIO.StringIO()
        q = getNextQueryResult(reader)

        with self.assertRaises(StopIteration):
            q.next()


print "TestXML.py"
unittest.main()
print "Done."
