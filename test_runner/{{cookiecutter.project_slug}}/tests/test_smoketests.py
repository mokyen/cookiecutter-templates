import pytest

@pytest.fixture
def equipment():
    # Open DUT connection
    return True

@pytest.mark.smoketest
def test_equipment_init(equipment):
    assert equipment

@pytest.mark.regression
def test_more_complicated_thing(equipment):
    assert equipment