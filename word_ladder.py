#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny',
    'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey'
    'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file) as f:
        words = set(line.strip() for line in f)
    if start_word not in words or end_word not in words:
        return None
    queue = [(start_word, [start_word])]
    while queue:
        word, path = queue.pop(0)
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + j + word[i+1:]
                if next_word == end_word:
                    return path + [next_word]
                if next_word in words and next_word not in path:
                    queue.append((next_word, path + [next_word]))
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    list = []
    if ladder:
        for i in range(len(ladder) - 1):
            list.append(_adjacent(ladder[i], ladder[i+1]))
        return all(list)
    return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    for c in range(len(word1)):
        if word1[c] != word2[c]:
            count += 1
    if count > 1:
        return False
    else:
        return True
