from utils import dicts
import pytest

def test_get_val():
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, 0 ) == 'Python'
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, 8) == 'git'
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, -7, 'NO') == 'NO'

@pytest.fixture
def fixt():
    return {0: 'Python', 1: 'Java', 2: 'R', 3: 'JS', 4: 'C#', 5: 'C++'}

def test_get_val_fixt1():
    assert dicts.get_val(fixt, 1) == 'Java'

def test_get_val_fixt2():
    assert dicts.get_val(fixt, 3) != 'git'

