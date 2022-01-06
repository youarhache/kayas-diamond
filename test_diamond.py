from diamond import print_diamond

def test_print_diamond_when_A():
    result = print_diamond(letter="A")

    assert result == "A"


def test_print_diamond_when_B():
    result = print_diamond(letter="B")

    assert result == " A \n" +\
                     "B B\n" +\
                     " A "


def test_print_diamond_when_C():
    result = print_diamond(letter="C")

    assert result == "  A  \n" +\
                     " B B \n" +\
                     "C   C\n" +\
                     " B B \n" +\
                     "  A  "