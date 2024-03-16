import os

from beerxml import BeerxmlParser


def test_parse_invalid_fermentable_amount():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/fermentable/invalid_amount.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("FERMENTABLES", 0, "AMOUNT") == err.errors()[0]["loc"]


def test_parse_invalid_fermentable_color():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/fermentable/invalid_color.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("FERMENTABLES", 0, "COLOR") == err.errors()[0]["loc"]


def test_parse_invalid_fermentable_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/fermentable/invalid_type.xml")) as file_content:
        xml_content = file_content.read()

    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("FERMENTABLES", 0, "TYPE") == err.errors()[0]["loc"]


def test_parse_invalid_fermentable_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/fermentable/invalid_version.xml")) as file_content:
        xml_content = file_content.read()

    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("FERMENTABLES", 0, "VERSION") == err.errors()[0]["loc"]


def test_parse_invalid_fermentable_yield():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/fermentable/invalid_yield.xml")) as file_content:
        xml_content = file_content.read()

    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("FERMENTABLES", 0, "YIELD") == err.errors()[0]["loc"]