"""testy"""
import main
def test_word():
    result = 49714
    assert main.Word('COLIN', 938).get_rank() == result

def test_page():
    arg = '<HTML>janca TONIK pepca LOJZA </html>'
    assert main.Page(arg).get_rank() == 202
