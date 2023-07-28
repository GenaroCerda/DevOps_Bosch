import pytest
import Hello_World

@pytest.mark.parametrize(
    "lenguage",
    [
        ("English")
    ],
)
def test_greeting_eng(lenguage):
    assert Hello_World.greeting(lenguage) == "Hello World!"
    
@pytest.mark.parametrize(
    "lenguage",
    [
        ("German")
    ],
)
def test_greeting_ger(lenguage):
    assert Hello_World.greeting(lenguage) == "Hallo Welt!"

@pytest.mark.parametrize(
    "lenguage",
    [
        ("Spanish")
    ],
)
def test_greeting_spa(lenguage):
    assert Hello_World.greeting(lenguage) == "Hola Mundo!"
    

@pytest.mark.parametrize(
    "lenguage",
    [
        ("French")
    ],
)
def test_greeting_fre(lenguage):
    assert Hello_World.greeting(lenguage) == "Salut monde!"

@pytest.mark.parametrize(
    "lenguage",
    [
        ("Italian")
    ],
)
def test_greeting_ita(lenguage):
    assert Hello_World.greeting(lenguage) == "Ciao mondo!"
    
    
@pytest.mark.parametrize(
    "lenguage",
    [
        ("Arabic"),
        ("Navajo"),
        ("High-Valyrian"),
        ("Arameo"),
        ("Latin")
    ],
)
def test_greeting_unavailable(lenguage):
    assert Hello_World.greeting(lenguage) == "Sorry that lenguage has not beed added yet"