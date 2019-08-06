import xml.etree.cElementTree as et
import pandas as pd


def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


def main():
    """ main """
    parsed_xml = et.parse("import.xml")
    dfcols = ['servedMSISDN', 'created_UTC']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsed_xml.getroot():
        servedMSISDN = node.attrib.get('servedMSISDN')
        created_UTC = node.find('created_UTC')

        df_xml = df_xml.append(
            pd.Series([servedMSISDN, getvalueofnode(created_UTC)], index=dfcols), ignore_index=True)

    print(df_xml)

main()