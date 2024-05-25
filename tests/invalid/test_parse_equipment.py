import os

import pytest
from pydantic import ValidationError

from beerxml import BeerxmlParser


def test_parse_invalid_calc_boil_volume():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_calc_boil_volume.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "CALC_BOIL_VOLUME") == err.value.errors()[0]["loc"]


def test_parse_invalid_batch_size():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_batch_size.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "BATCH_SIZE") == err.value.errors()[0]["loc"]


def test_parse_invalid_boil_size():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_boil_size.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "BOIL_SIZE") == err.value.errors()[0]["loc"]


def test_parse_invalid_boil_time():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_boil_time.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "BOIL_TIME") == err.value.errors()[0]["loc"]


def test_parse_invalid_evap_rate():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_boil_time.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "BOIL_TIME") == err.value.errors()[0]["loc"]


def test_parse_invalid_hop_utilization():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_hop_utilization.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "HOP_UTILIZATION") == err.value.errors()[0]["loc"]


def test_parse_invalid_lauter_deadspace():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_lauter_deadspace.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "LAUTER_DEADSPACE") == err.value.errors()[0]["loc"]


def test_parse_invalid_top_up_kettle():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_top_up_kettle.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TOP_UP_KETTLE") == err.value.errors()[0]["loc"]


def test_parse_invalid_top_up_water():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_top_up_water.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TOP_UP_WATER") == err.value.errors()[0]["loc"]


def test_parse_invalid_trub_chiller_loss():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_trub_chiller_loss.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TRUB_CHILLER_LOSS") == err.value.errors()[0]["loc"]


def test_parse_invalid_tun_specific_heat():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_tun_specific_heat.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TUN_SPECIFIC_HEAT") == err.value.errors()[0]["loc"]


def test_parse_invalid_tun_volume():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_tun_volume.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TUN_VOLUME") == err.value.errors()[0]["loc"]


def test_parse_invalid_tun_weight():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/equipment/invalid_tun_weight.xml")) as file_content:
        xml_content = file_content.read()
    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EQUIPMENT", "TUN_WEIGHT") == err.value.errors()[0]["loc"]
