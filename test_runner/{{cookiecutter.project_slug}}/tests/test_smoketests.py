import pytest

@pytest.fixture
def equipment():
    # Open DUT connection
    return True

def test_equipment_init(equipment):
    assert equipment