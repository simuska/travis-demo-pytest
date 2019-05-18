from fizzbuzz import fizzbuzz
import pytest

def test_fb_is_callable_with_1_argument(): # collection - kolekce - test skonci hned na zaciatku, nedojde do fcie
    fizzbuzz(1)

def test_fb_returns_str():
    assert isinstance(fizzbuzz(1), str)

@pytest.mark.parametrize('num', [1, 2, 4])
def test_fb_regular_is_self(num):
    assert fizzbuzz(num) == str(num)

@pytest.mark.parametrize('num', [3, 6, 9])
def test_fb_three_is_fizz(num):
    assert fizzbuzz(num) == 'fizz'  # fizz znamena delitelny troma

@pytest.mark.parametrize('num', [5, 20, 50])
def test_fb_five_is_buzz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15, 30, 3000])
def test_fb_threefive_is_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'

@pytest.mark.parametrize('num', ["", 1.5, 4j] )
def test_fb_raises_typerror_on_nonint(num):
    with pytest.raises(TypeError):
        fizzbuzz(num)

@pytest.mark.parametrize('num', [-1, -20, 0])
def test_fb_raises_typerror_on_nonpositive(num):
    with pytest.raises(ValueError):
        fizzbuzz(num)
