import os.path

from beerxml.beerxml_parser import BeerxmlParser


def test_parse_only_mandatory_attributes() -> None:
    with open(os.path.join(os.path.dirname(__file__), "assets/only_mandatory.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
