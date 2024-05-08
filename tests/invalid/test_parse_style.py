import os

from beerxml import BeerxmlParser


def test_parse_invalid_abv_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_abv_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "ABV_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_abv_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_abv_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "ABV_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_carb_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_carb_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "CARB_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_carb_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_carb_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "CARB_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_color_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_color_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "COLOR_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_color_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_color_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "COLOR_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_fg_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_fg_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "FG_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_fg_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_fg_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "FG_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_ibu_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_ibu_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "IBU_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_ibu_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_ibu_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "IBU_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_og_max():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_og_max.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "OG_MAX") == err.errors()[0]["loc"]


def test_parse_invalid_og_min():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_og_min.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "OG_MIN") == err.errors()[0]["loc"]


def test_parse_invalid_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_type.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "TYPE") == err.errors()[0]["loc"]


def test_parse_invalid_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/style/invalid_version.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("STYLE", "VERSION") == err.errors()[0]["loc"]
