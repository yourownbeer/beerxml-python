import os

from beerxml import BeerxmlParser


def test_parse_invalid_hop_alpha():
    with open(os.path.join(os.path.dirname(__file__), "assets/invalid/hop/invalid_alpha.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("HOPS", 0, "ALPHA") == err.errors()[0]["loc"]


def test_parse_invalid_hop_amount():
    with open(os.path.join(os.path.dirname(__file__), "assets/invalid/hop/invalid_amount.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("HOPS", 0, "AMOUNT") == err.errors()[0]["loc"]


def test_parse_invalid_hop_use():
    with open(os.path.join(os.path.dirname(__file__), "assets/invalid/hop/invalid_use.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("HOPS", 0, "USE") == err.errors()[0]["loc"]


def test_parse_invalid_hop_time():
    with open(os.path.join(os.path.dirname(__file__), "assets/invalid/hop/invalid_time.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("HOPS", 0, "TIME") == err.errors()[0]["loc"]