import xml.etree.ElementTree as et

etree = et.parse('hosts.xml')

for host_tag in etree.getiterator('host'):
    print(host_tag.get('name'), host_tag.get('port'))

    for host_info in host_tag:
        print(host_info.text)
    print()
