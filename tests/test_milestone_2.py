from milestone_2 import __version__, love


def test_version():
    assert __version__ == '0.1.0'

def test_love():
    assert love(2) == 4
    assert love(4) == 8
    assert love(float('inf')) == float('inf')