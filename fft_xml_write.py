# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

def indent(elem, level=0):
    i = "\n" + level * " "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def makeXML(userIndex, fft):
    node = ET.Element("data")
    str_id = str(userIndex)
    for i in range(0, len(fft)):
        node.attrib["Second"] = str_id
        ET.SubElement(node, "_" + str(i+1) + "Hz").text = str(fft[i])
    return node

    #node.attrib["Second"] = str_id
    #ET.SubElement(node, "Fp1").text = str_ch1
    #ET.SubElement(node, "")
    #return node

'''
user = ET.Element("leehong")
data = makeXML(1, "3.414", "4.3204")
user.append(data)
data = makeXML(2, "4.4324", "34.234")
user.append(data)
indent(user)
ET.ElementTree(user).write("887.xml")
'''
