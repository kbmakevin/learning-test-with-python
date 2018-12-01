from app import *


def test_hello():
    assert hello_world() == 'hello world'


def test_custon_num_list():
    assert len(create_num_list(10)) == 0


def test_custom_func_x():
    assert custom_func_x(3, 3, 2) == 14


def test_custom_non_lin_num_list():
    assert custom_non_lin_num_list(5, 2, 3)[2] == 16
    assert custom_non_lin_num_list(5, 3, 2)[4] == 4
