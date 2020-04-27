from my_project import main


def test_main():
    msg_data = main()
    assert 'data' in msg_data
    assert msg_data['data'].startswith('hello world')

def test_fail_on_purpose():
    assert False