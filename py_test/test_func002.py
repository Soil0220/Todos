"""
test
"""

import func002

def test_func002():
    """
    pytest test_func002.py
    """
    assert func002.ex(3) == 9
    assert func002.ex("10") == 0
