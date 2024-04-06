import pytest
from unittest.mock import patch
from io import StringIO
import wordgame  # import wordgame script
import pywebio

# Mocking user input for testing
def mock_input(mock_values):
    return lambda _: mock_values.pop(0)

def test_choose():
    word = wordgame.choose()
    assert isinstance(word, str)

def test_jumble():
    jumbled_word = wordgame.jumble("test")
    assert sorted(jumbled_word) == sorted("test")  # Check if characters are the same

