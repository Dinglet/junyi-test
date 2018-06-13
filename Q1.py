import re


def reverse_str(s: str):
    """(A.) """
    return s[::-1]


def reverse_sentence(s: str):
    """(B.) """
    return re.sub(r'\w+', lambda word: reverse_str(word.group()), s)


if __name__ == '__main__':
    print(reverse_str("junyiacademy"))
    assert ('ymedacaiynuj' == reverse_str('junyiacademy')), 'function junyiacademy(s) is not correct.'
    print(reverse_sentence("flipped class room is important"))
    assert ('flipped class room is important' == reverse_sentence("deppilf ssalc moor si tnatropmi")),\
        'function reverse_sentence(s) is not correct.'
