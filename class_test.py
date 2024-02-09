import cat

def test_cat():
    c1 = cat.Cat()
    assert c1.name == "Unknown"

def test_cat2():
    c1 = cat.Cat()
    assert c1.age == 0

def test_cat3():
    c1 = cat.Cat()
    assert c1.speak() == "Meow"