"""
test relay
"""
import relay
def test_parse():
    """
    test parseru
    """
    arg = ('1) Austria 2:25:18 (Elisabeth Hohen' 
          'warter, Sonja Zinkl, Michaela Gigon)')
    result = [('1', '2:25:18',  'Elisabeth', 'Hohenwarter',
               'Sonja', 'Zinkl', 'Michaela', 'Gigon')]
    assert result == relay.parse_results(arg)
def test_db():
    """ 
    test prirazovace
    """
    arg = ('1) Austria 2:25:18 (Elisabeth Hohenwarter,'
           ' Sonja Zinkl, Michaela Gigon)')
    result = [{'id': 6634, 'time': '2:25:18', 'result': 1},
              {'id': 1742, 'time': '2:25:18', 'result': 1}]
    assert result == relay.loadDB(arg)


