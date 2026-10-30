
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_grade_page_loads():
    client = app.test_client()
    response = client.get('/')
    assert b'Grade' in response.data


def test_invalid_marks():
    client = app.test_client()
    response = client.post('/result', data={
        'maths': '150',
        'cs': '80',
        'physics': '75',
        'english': '85',
        'chemistry': '90'
    })
    assert response.status_code == 400
    assert b'Marks must be between 0 and 100' in response.data

