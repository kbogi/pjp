"""
@author: Krystof Bogar

test dveri

"""
import doors
def test_condition():
    """
    test podminky
    """
    assert doors.condition("ahoj", "jaho") == True
def test_condition2():
    """
    test podminky
    """
    assert doors.condition("ahoj", "ahoj") == False

def test_solver():
    """
    test resice
    """
    arg = ["acm", "motyka", "apac"]
    result = True
    assert doors.solve_key(arg) ==  result

def test_solver2():
    """
    test resice
    """
    arg = ["acm", "lapac"]
    result = False
    assert doors.solve_key(arg) == result
    
def test_key():
    """
    test celeho algoritmu
    """
    arg = ["kolo", "karma"]
    result = False
    assert doors.is_key(arg) == result
    
def test_key2():
    """
    test celeho algoritmu
    """
    arg = ["motyka", "apac", "acm"]
    result = True
    assert doors.is_key(arg) == result
    
def test_key3():
    """
    test celeho algoritmu
    """
    arg = ["roura", "kobyla", "andulu", "tram", "syr", "ananas", "ulovit"]
    result = True
    assert doors.is_key(arg) == result
    
def test_key4():
    """
    test celeho algoritmu
    """
    arg = ["ok", "ko"]
    result = True
    assert doors.is_key(arg) == result


    
