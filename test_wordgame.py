import pytest
from unittest.mock import patch
from io import StringIO
import wordgame  # import wordgame script

# Mocking user input for testing
def mock_input(mock_values):
    return lambda _: mock_values.pop(0)

def test_choose():
    word = wordgame.choose()
    assert isinstance(word, str)

def test_jumble():
    jumbled_word = wordgame.jumble("test")
    assert sorted(jumbled_word) == sorted("test")  # Check if characters are the same

@patch("wordgame.input", side_effect=mock_input(["Test"]))
def test_play(mock_input):
    # Redirect stdout to capture output for testing
    with patch('sys.stdout', new=StringIO()) as fake_out:
        wordgame.play()
        output = fake_out.getvalue().strip()
    assert "challenge is :" in output.lower()
    assert "great!" in output.lower() or "uh oh!" in output.lower()  # Checks for feedback

@patch("wordgame.input", side_effect=mock_input(["Test"]))
def test_thank(mock_input):
    # Redirect stdout to capture output for testing
    with patch('sys.stdout', new=StringIO()) as fake_out:
        main_script.thank("Test Player", 1, 3)
        output = fake_out.getvalue().strip()
    assert "test player, your score is :" in output.lower()
    assert "thanks for playing!" in output.lower()

