"""
 Generate required number of XML files with random values
"""

from lxml import etree
from lxml.builder import E
from random import randint
import os.path


def r(mstr=''):
    # returns string with random number for xml generating

    return '{}{}'.format(mstr, randint(1,1000))


def make_xml_file(n):
    # Generate required number of XML files with random values

    for i in xrange(n):
        root = etree.Element('shiporder', {'orderid': r()})

        root.append((E.orderperson(r('orderperson'))))
        shipto = (E.shipto(
                          E.name(r('name')),
                          E.address(r('street')),
                          E.city(r('city')),
                          E.country(r('country'))
                          ))
        root.append(shipto)

        #<xs:element name="item" maxOccurs="unbounded">
        for j in xrange(1, randint(1, 10)):
            item = (E.item(
                E.title(r('title'))))

            #<xs:element name="note" type="xs:string" minOccurs="0"/>
            if randint(0,1) == 1:
                item.append((E.note(r('note'))))
            item.append((E.quantity(r(''))))
            item.append((E.price(r('')+'.00')))
            root.append(item)

        doc = etree.ElementTree(root)
        try:
            fname = os.path.join(os.path.dirname(__file__), 'xml_test_%s.xml' % i)
            doc.write((fname), xml_declaration=True, encoding='utf-8', pretty_print=True)
            print fname + '   saved.'
        except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)


make_xml_file(5)