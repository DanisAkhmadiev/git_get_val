from utils import dicts

def test_get_val():
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, 0 ) == 'Python'
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, 8) == 'git'
    assert dicts.get_val({0: 'Python', 1: 'Java', 2: 'R'}, -7, 'NO') == 'NO'
