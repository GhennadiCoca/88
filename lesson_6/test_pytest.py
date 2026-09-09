import pytest


def test_first():
    assert 2 + 2 == 4
    assert 10 -3 == 7
    assert 10 * 3 == 30

def test_string():
    name = "Sveta"
    assert name == "Sveta"
    assert len(name) == 5
    assert name.upper() == "SVETA"



def test_list():
    num = [1, 2, 3]
    assert 2 in num
    assert len(num) == 3
    assert num[0] == 1

def add(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0



def get_discount_price(price, discount_percent):
    return price - price * discount_percent / 100



def test_add():
    assert add(1, 2) == 3
    assert add(-1, 2) == 1
    assert add(0,0) == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_discount():
    assert get_discount_price(100, 20) == 80
    assert get_discount_price(100,0) == 100

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, -2, -3),
    (0, 0, 0)
    ])

def test_add_parentheses(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("num,expected", [
    (1, False),
    (2, True),
    (3, False),
    (4, True),
])
def test_is_parametrize(num, expected):
    assert is_even(num) == expected

@pytest.fixture
def my_user():
    return {"name": "Sveta", "age": 18, "email": "svena123@gmail.com"}

def test_user(my_user):
    assert my_user["name"] == "Sveta"

def test_user_age(my_user):
    assert my_user["age"] == 18
    assert my_user["age"] > 17

# create func revers string and test for it
# same test with parametrize

def reverse_word(word):
    return word[::-1]

def test_reverse_word():
    assert reverse_word("aisi") == "isia"
    assert reverse_word("dog") == "god"
    assert reverse_word("cat") == "tac"
# same test with parametrize

@pytest.mark.parametrize("word,expected", [
    ("sveta", "atevs"),
    ("12345", "54321"),
    ("marker", "rekram"),
])
def test_reverse_word_parametrize(word, expected):
    assert reverse_word(word) == expected


@pytest.fixture
def schopping_list():
    return ["milk", "breat", "coffee"]

def test_shopping_list(shopping_list):
    assert len(shopping_list) == 3
    assert shopping_list[0] == "milk"
    assert "breat" in shopping_list
    assert "apple" not in shopping_list