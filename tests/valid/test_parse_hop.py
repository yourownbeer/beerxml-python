import os

from beerxml import BeerxmlParser


def test_parse_one_hop() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/hop/hop_single.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_hop_use_dry_hop() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/hop/valid_hop_use_dry_hop.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_hop_use_first_wort() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/hop/valid_hop_use_first_wort.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_hop_use_mash() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/hop/valid_hop_use_mash.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_hop_use_aroma() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/hop/valid_hop_use_aroma.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)
