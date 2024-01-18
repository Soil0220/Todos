"""

test_back

"""

from number_back import save,delete,find_all

#def test_number_back():
#    """
#    test save
#    """
#    assert save(10) is True
#    assert save("10") is False
#    assert save(3.14) is False

#def test_find_all():
#    assert len(find_all()) == 1
#    save(100)
#    assert len(find_all()) == 2


def test_delete():
    save(10)
    save(20)
    save(30)
    assert delete(20) == True
    assert len(find_all()) == 2
