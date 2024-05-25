import os.path

from beerxml.beerxml_parser import BeerxmlParser


def test_parse_recipe_all_attributes() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/recipe/recipe_all_attributes.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_recipe_only_mandatory_attributes() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/recipe/recipe_only_mandatory.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_type_all_grain() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/recipe/recipe_type_all_grain.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_type_extract() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/recipe/recipe_type_extract.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_recipe_type_partial_mash() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/recipe/recipe_type_partial_mash.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
