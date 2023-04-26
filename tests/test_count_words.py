from lib.count_words import *

def test_count_words_four_words():
    result = count_words("Hello, cruel dark world!")
    assert result == 4