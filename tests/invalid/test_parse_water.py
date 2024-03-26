import os

from beerxml import BeerxmlParser


def test_parse_invalid_water_amount():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_amount.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "AMOUNT") == err.errors()[0]["loc"]


def test_parse_invalid_water_bicarbonate():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_bicarbonate.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "BICARBONATE") == err.errors()[0]["loc"]


def test_parse_invalid_water_calcium():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_calcium.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "CALCIUM") == err.errors()[0]["loc"]


def test_parse_invalid_water_chloride():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_chloride.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "CHLORIDE") == err.errors()[0]["loc"]


def test_parse_invalid_water_magnesium():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_magnesium.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "MAGNESIUM") == err.errors()[0]["loc"]


def test_parse_invalid_water_ph():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_ph.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "PH") == err.errors()[0]["loc"]


def test_parse_invalid_water_sodium():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_sodium.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "SODIUM") == err.errors()[0]["loc"]


def test_parse_invalid_water_sulfate():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_sulfate.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "SULFATE") == err.errors()[0]["loc"]


def test_parse_invalid_water_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/water/invalid_version.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("WATERS", 0, "VERSION") == err.errors()[0]["loc"]



