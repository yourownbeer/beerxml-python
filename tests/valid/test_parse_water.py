import os

from beerxml import BeerxmlParser


def test_parse_water_all() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/water/valid_all.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
