import os

from beerxml import BeerxmlParser


def test_parse_invalid_yeast_amount():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_amount.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "AMOUNT") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_attenuation():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_attenuation.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "ATTENUATION") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_flocculation():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_flocculation.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "FLOCCULATION") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_max_reuse():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_max_reuse.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "MAX_REUSE") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_max_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_max_temp.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "MAX_TEMPERATURE") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_min_temperature():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_min_temp.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "MIN_TEMPERATURE") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_times_cultured():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_times_cultured.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "TIMES_CULTURED") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_form():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_form.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "FORM") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_version.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "VERSION") == err.errors()[0]["loc"]


def test_parse_invalid_yeast_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/yeast/invalid_yeast_type.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("YEASTS", 0, "TYPE") == err.errors()[0]["loc"]
