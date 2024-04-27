from python_repos import status

def test_status():
    status_num = status()
    assert status_num == 200