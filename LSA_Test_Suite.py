import LSA as lsa
from LSA import LSA
import textmining


def test_parse():
    mylsa = LSA("","")
    test_string = "Try to parse this correctly?"
    expected_dict = ['try', 'to','parse', 'this','correctly?']
    mylsa.parse(test_string)
    print mylsa.word_dict.keys()
    if cmp(expected_dict , mylsa.word_dict.keys()) == 0:
        print "Parsing of a simple string successful"
    else:
        print "Parsing Failed!"

def test_parse_with_restrictions():
    stop_words = ["to", "this"]
    ignorechar = '?'
    mylsa = LSA(stop_words, ignorechar)
    test_string = "Try to parse this correctly?"
    expected_dict = ['try','parse', 'correctly']
    mylsa.parse(test_string)
    print mylsa.word_dict.keys(), len(test_string)
    if cmp(expected_dict , mylsa.word_dict.keys()) == 0:
        print "Parsing of a simple string with restrictions successful"
    else:
        print "Parsing Failed!"

test_parse()
test_parse_with_restrictions()