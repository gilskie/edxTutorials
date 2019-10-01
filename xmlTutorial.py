import lxml.etree


def main():
    xml_parse = lxml.etree.parse('sample.xml')
    # print(type(xml_parse))

    xml_string = lxml.etree.tostring(xml_parse, encoding='unicode')
    root = lxml.etree.XML(xml_string)
    # print(lxml.etree.tostring(root, pretty_print=True).decode('utf-8'))
    # r = []
    for element in root.findall('letter/text'):
        print(element.text)

    # accessing tags within tags.
    for item in root.iter('text'):
        if isinstance(item, lxml.etree._Element):
            print()


    # print(r)
    # print(f"{element.text}")
    # print(f"{element.text}")


main()
