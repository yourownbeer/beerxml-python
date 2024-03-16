import os

from beerxml import BeerxmlParser


def test_parse_one_yeast() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_single.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_form_culture() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_form_culture.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_form_dry() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_form_dry.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_form_slant() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_form_slant.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_type_champagne() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_type_champagne.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_type_lager() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_type_lager.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_type_wheat() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_type_wheat.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_type_wine() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_type_wine.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_flocculation_high() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_flocculation_high.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_flocculation_very_high() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_flocculation_very_high.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_yeast_flocculation_medium() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/yeast/valid_yeast_flocculation_medium.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)



