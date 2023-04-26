import pytest
from Pen import *


class TestColor:

    def test_color(self):
        assert Pen(color="yellow").get_color() == "yellow"
