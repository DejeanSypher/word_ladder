#!/bin/python3


from collections import deque

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
        dictionary = set(word.strip().lower() for word in f)

    if start_word not in dictionary:
        return None

    stack = [start_word]
    queue = deque([stack])

    while queue:
        curr_ladder = queue.popleft()
        curr_word = curr_ladder[-1]

        if curr_word == end_word:
            return curr_ladder

        for next_word in dictionary:
            if is_adjacent(curr_word, next_word):
                if next_word == end_word:
                    return curr_ladder + [next_word]

                new_ladder = curr_ladder + [next_word]
                queue.append(new_ladder)
                dictionary.remove(next_word)

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
    if not ladder:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False

    count = 0
    for c in range(len(word1)):
        if word1[c] != word2[c]:
            count += 1
    if count > 1:
        return False
    else:
        return True
