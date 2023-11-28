def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # instead of reassigning phrase could be better with a new variable name
    # lower and replace return copies, str are immutable

    normalized_phrase = phrase.lower().replace(' ', '')

    i = 0
    j = len(normalized_phrase) - 1

    while i < j:

        if normalized_phrase[i] != normalized_phrase[j]:
            return False

        i += 1
        j -= 1

    return True

# TODO: another way to implement this is to check if the reverse and non-reverse are equal
