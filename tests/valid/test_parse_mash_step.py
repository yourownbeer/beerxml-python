import os

from beerxml import BeerxmlParser


def test_parse_end_temp() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_end_temp.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_ramp_temp() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_ramp_time.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_one_mash_step() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_single.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_temperature() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_temperature.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_type_decoction() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_type_decoction.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_type_infusion() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_type_infusion.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


def test_parse_version() -> None:
    with open(os.path.join(os.path.dirname(__file__), "../assets/valid/mash_step/valid_mash_step_version.xml")) as file_content:
        xml_content = file_content.read()
    BeerxmlParser().parse(xml_content)


