import os

from beerxml import BeerxmlParser


def test_parse_fermentable_type_adjunct() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/fermentable/valid_fermentable_type_adjunct.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_fermentable_type_dry_extract() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/fermentable/valid_fermentable_type_dry_extract.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_fermentable_type_extract() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/fermentable/valid_fermentable_type_extract.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)