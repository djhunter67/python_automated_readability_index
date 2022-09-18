
from fractions import Fraction

def count_words(text: str) -> int:
    """Return the number of words in a text."""

    return len(text.split())

def count_characters(text: str) -> int:
    """Return the number of characters in a text."""

    return len(text)

def count_sentences(text: str) -> int:
    """Return the number of sentences in a text."""

    return len(text.split("."))


def ari_function(words: int, characters: int, sentences: int) -> int:
    """Return the ari score of a text."""

    constant_1 = 4.71
    constant_2 = Fraction(1, 2)
    constant_3 = 21.43

    return int(constant_1 * (characters / words) + constant_2 * (words / sentences) - constant_3)

def quantify_ari(ari_score: float) -> str:
    """Return the ARI score of a text."""

    ari_scale = {
        1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
        3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
        4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
        5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
        6: {'ages': '10-11', 'grade_level':    '5th Grade'},
        7: {'ages': '11-12', 'grade_level':    '6th Grade'},
        8: {'ages': '12-13', 'grade_level':    '7th Grade'},
        9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

    return ari_scale[ari_score]



    

