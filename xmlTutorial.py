import lxml.etree
import lxml.objectify
import re


def main():
    sample_tutorial()


def sample_tutorial():
    file_name = 'ready.xml'
    xml_parse = lxml.etree.parse(file_name)
    # print(f"type: {type(xml_parse)},Parse: {xml_parse}")

    xml_string = lxml.etree.tostring(xml_parse, encoding='utf-8')
    root = lxml.etree.XML(xml_string)

    pattern = re.compile("\{[^\}]+\}")
    xmlns_value = pattern.search(root.tag).group()

    # print(f"xmlns value: {xmlns_value}")
    # breakpoint()

    # printing the whole xml document
    # print(lxml.etree.tostring(root, pretty_print=True).decode("utf-8"))

    # for e in root:
    #     print(e.tag)

    # root.set('newAttribute', 'newAttributeValue')
    # print(lxml.etree.tostring(root, pretty_print=True).decode("utf-8"))

    # print(root.get('newAttribute'))
    # print(root[1].get('alpha'))

    # root[0].text = "sample1"
    # root[1].text = "sample2"
    # root[1][0].text = root[1][0].text + " sample2"
    # print(lxml.etree.tostring(root, pretty_print=True).decode("utf-8"))

    # checking if there are childrens
    # if len(root) > 0:
    #     print("with children!")
    # else:
    #     print("without children!")

    # checking for childnodes for children
    # for i in range(len(root)):
    #     if len(root[i]) > 0:
    #         print(f"children {root[i].tag} has child nodes")
    #     else:
    #         print(f"children {root[i].tag} has no child nodes")

    # checking if it is a valid element
    # for i in range(len(root)):
    #     print(lxml.etree.iselement(root[i]))

    # get parent elements
    # print(f"get parent: {root.getparent()}")
    # print(f"get parent: {root[0].getparent()}")
    # print(f"get parent: {root[1].getparent()}")

    # getting next and previous elements/tags
    # print(root[0].getnext())
    # print(root[1].getprevious())

    # root.text = "NEW ROOT FOR TESTING PURPOSES!"
    # print(lxml.etree.tostring(root, xml_declaration=True).decode('utf-8'))

    # finding elements!
    # print(root[0].tag)
    # print(root[1].tag)

    print(root[0][1].tag)
    print(root[0].find(xmlns_value + 'supplier-dataset-id'))
    print(root.find(xmlns_value + 'dataset-unique-ids'))


def edx_tutorial():
    xml_parse = lxml.etree.parse('sample.xml')
    # print(type(xml_parse))

    xml_string = lxml.etree.tostring(xml_parse, encoding='utf-8')
    root = lxml.etree.XML(xml_string)

    # print(lxml.etree.tostring(root, pretty_print=True).decode('utf-8'))
    # print(lxml.etree.tostring(root, pretty_print=True).decode('utf-8'))
    # print(f"Printing root!")
    # for element in root:
    #     print(element)
    #
    # for element in root.findall("emphasis"):
    #     print(element)

    # accessing tags within tags.
    # for item in root.iter('text'):
    #     if isinstance(item, lxml.etree._Element):
    #         print()

    # print(r)
    # print(f"{element.text}")
    # print(f"{element.text}")

    for r in root.findall('title'):
        print(r.text)


main()
