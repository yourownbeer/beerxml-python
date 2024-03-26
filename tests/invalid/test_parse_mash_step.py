import os

from beerxml import BeerxmlParser


def test_parse_invalid_mash_step_end_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_end_temp.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "END_TEMP") == err.errors()[0]["loc"]


def test_parse_invalid_mash_step_infuse_amount():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_infuse_amount.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "INFUSE_AMOUNT") == err.errors()[0]["loc"]


def test_parse_invalid_mash_step_ramp_time():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_ramp_time.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "RAMP_TIME") == err.errors()[0]["loc"]


def test_parse_invalid_mash_step_step_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_step_temp.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "STEP_TEMP") == err.errors()[0]["loc"]


def test_parse_invalid_mash_step_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_type.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "TYPE") == err.errors()[0]["loc"]


def test_parse_invalid_mash_step_version():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/mash_step/invalid_version.xml")) as file_content:
        xml_content = file_content.read()
    try:
        BeerxmlParser().parse(xml_content)
    except Exception as err:
        assert 1 == err.error_count()
        assert ("MASH", "MASH_STEPS", 0, "VERSION") == err.errors()[0]["loc"]
