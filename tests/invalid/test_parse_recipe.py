import os

import pytest
from pydantic import ValidationError

from beerxml import BeerxmlParser


def test_parse_invalid_age():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_age.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("AGE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_age_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_age_temp.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("AGE_TEMP",) == err.value.errors()[0]["loc"]


def test_parse_invalid_batch_size():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_batch_size.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("BATCH_SIZE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_boil_size():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_boil_size.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("BOIL_SIZE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_boil_time():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_boil_time.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("BOIL_TIME",) == err.value.errors()[0]["loc"]


def test_parse_invalid_carbonation():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_carbonation.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("CARBONATION",) == err.value.errors()[0]["loc"]


def test_parse_invalid_carbonation_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_carbonation_temp.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("CARBONATION_TEMP",) == err.value.errors()[0]["loc"]


def test_parse_invalid_efficiency():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_efficiency.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("EFFICIENCY",) == err.value.errors()[0]["loc"]


def test_parse_invalid_fermentation_stages():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_fermentation_stages.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("FERMENTATION_STAGES",) == err.value.errors()[0]["loc"]


def test_parse_invalid_fg():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_fg.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("FG",) == err.value.errors()[0]["loc"]


def test_parse_invalid_forced_carbonation():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_forced_carbonation.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("FORCED_CARBONATION",) == err.value.errors()[0]["loc"]


def test_parse_invalid_keg_priming_factor():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_keg_priming_factor.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("KEG_PRIMING_FACTOR",) == err.value.errors()[0]["loc"]


def test_parse_invalid_og():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_og.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("OG",) == err.value.errors()[0]["loc"]


def test_parse_invalid_primary_age():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_primary_age.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("PRIMARY_AGE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_primary_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_primary_temp.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("PRIMARY_TEMP",) == err.value.errors()[0]["loc"]



def test_parse_invalid_priming_sugar_equiv():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_priming_sugar_equiv.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("PRIMING_SUGAR_EQUIV",) == err.value.errors()[0]["loc"]


def test_parse_invalid_secondary_age():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_secondary_age.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("SECONDARY_AGE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_secondary_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_secondary_temp.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("SECONDARY_TEMP",) == err.value.errors()[0]["loc"]



def test_parse_invalid_taste_rating():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_taste_rating.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("TASTE_RATING",) == err.value.errors()[0]["loc"]


def test_parse_invalid_tertiary_age():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_tertiary_age.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("TERTIARY_AGE",) == err.value.errors()[0]["loc"]


def test_parse_invalid_tertiary_temp():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_tertiary_temp.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("TERTIARY_TEMP",) == err.value.errors()[0]["loc"]


def test_parse_invalid_type():
    with open(os.path.join(os.path.dirname(__file__), "../assets/invalid/recipe/invalid_type.xml")) as file_content:
        xml_content = file_content.read()

    with pytest.raises(ValidationError) as err:
        BeerxmlParser().parse(xml_content)
    assert 1 == err.value.error_count()
    assert ("TYPE",) == err.value.errors()[0]["loc"]