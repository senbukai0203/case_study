import pytest
class NotInRange(Exception) :
    def __init__(self, message="value not in given range - by Oracle") :
        self.message = message
        super().__init__(self.message)

def test_generic() :
    a = 30
    b = 40

    assert a == 30

def test_generic_1() :
    a=500;
    with pytest.raises(NotInRange):
        if a not in range(0,200):
            raise NotInRange
