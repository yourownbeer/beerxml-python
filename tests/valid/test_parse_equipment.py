import os

from beerxml import BeerxmlParser


def test_parse_equipment_all_values() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/equipment/valid_equipment_all_values.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_equipment_mandatory_values() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/equipment/valid_equipment_mandatory_values.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
