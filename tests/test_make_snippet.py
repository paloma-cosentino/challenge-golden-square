from lib.make_snippet import *

def test_return_if_less_then_five_words():
    result = make_snippet("Hello world")
    assert result == "Hello world"


def test_return_if_more_then_five_words():
    result = make_snippet("Hello world! How are you today?")
    assert result == "Hello world! How are you ..."