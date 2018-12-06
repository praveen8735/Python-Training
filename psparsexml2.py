import xml.etree.ElementTree as et

etree = et.parse('hosts.xml')
print(etree)
print()
print(etree.getroot())
print(etree.getroot().tag)
print()
print(etree.getroot().attrib)