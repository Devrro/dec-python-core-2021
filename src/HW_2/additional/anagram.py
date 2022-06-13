# //////////////////////////////////////////////////////////////////////////////////////////////
# // Знайти анаграму.
# //     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
# //
# //     ANAGRAM | MGANRAA -> true
# // EXIT | AXET -> false
# // GOOD | DOGO -> true
# //////////////////////////////////////////////////////////////////////////////////////////////

def count_elements(lst: list) -> dict:
    elem_count = {}
    for i in lst:
        elem_count[i] = elem_count.get(i, 0) + 1

    return elem_count


def check_for_anagram(sentence: str, sentence2: str) -> bool:

    return count_elements(list(sentence.lower())) == count_elements(list(sentence2.lower()))


print(check_for_anagram('ANAGRAM', 'MGANRAA'))
print(check_for_anagram('EXIT', 'AXET'))
print(check_for_anagram('GOOD', 'DOGO'))
