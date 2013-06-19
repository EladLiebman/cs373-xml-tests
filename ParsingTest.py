import xml.etree.ElementTree as ET

# making a string from the input
x = '''<THU>
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
<Team><Cooly></Cooly></Team>'''

# appending and prepending valid XML tags
x = '<XML>' + x + '</XML>'
root = ET.fromstring(x)

for child in root.iter() :
	print child
