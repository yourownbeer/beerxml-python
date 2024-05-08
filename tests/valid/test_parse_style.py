import os

from beerxml import BeerxmlParser


def test_parse_style_all() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_all_fields.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_ale() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_ale.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_cider() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_cider.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_lager() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_lager.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_mead() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_mead.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_mixed() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_mixed.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_style_type_wheat() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/style/valid_type_wheat.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
