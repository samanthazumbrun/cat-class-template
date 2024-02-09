import cat

def test_cat():
    c1 = cat.garfield
    assert c1.name == "Garfield"

def test_cat2():
    c1 = cat.garfield
    assert c1.age == 50

def test_cat3():
    c1 = cat.garfield
    assert c1.speak() == "Meow"