import os

from beerxml import BeerxmlParser


def test_parse_invalid_misc_amount():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/misc/invalid_amount_is_weight.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MISCS", 0, "AMOUNT_IS_WEIGHT") == err.errors()[0]["loc"]


def test_parse_invalid_misc_time():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/misc/invalid_time.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MISCS", 0, "TIME") == err.errors()[0]["loc"]


def test_parse_invalid_misc_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/misc/invalid_type.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MISCS", 0, "TYPE") == err.errors()[0]["loc"]


def test_parse_invalid_misc_use():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/misc/invalid_use.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MISCS", 0, "USE") == err.errors()[0]["loc"]


def test_parse_invalid_misc_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/misc/invalid_version.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MISCS", 0, "VERSION") == err.errors()[0]["loc"]

