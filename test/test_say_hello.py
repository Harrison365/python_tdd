from src.say_hello import say_hello
import pytest


def test_say_hello_says_hello():
    excepted = "Hello World!"
    actual = say_hello("World")
    assert excepted == actual

def test_say_hello_raises_type_error():
    with pytest.raises(TypeError):
        say_hello(1)
        