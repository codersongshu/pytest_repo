from fixture_func import studentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup------------')
    db = studentDB()
    db.connect('data.json')
    # return db
    yield db
    print('----------teardown------------')
    db.close()

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'