import os.path

from beerxml.beerxml_parser import BeerxmlParser


def test_parse_valid_only_mandatory_attributes() -> None:
    with open(os.path.join(os.path.dirname(__file__), "assets/valid/only_mandatory.xml")) as file_content:
        xml_content = file_content.read()
    result = BeerxmlParser().parse(xml_content)


def test_parse_one_hop() -> None:
    with open(os.path.join(os.path.dirname(__file__), "assets/valid/hop_single.xml")) as file_content:
        xml_content = file_content.read()
    result = BeerxmlParser().parse(xml_content)
