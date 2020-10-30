import pytest
from programs import route_planner

def test_route():
    assert route_planner.route_planner("0 2 6 3 5 9 8 4 9 5") == ['0', '2', '6', '9']