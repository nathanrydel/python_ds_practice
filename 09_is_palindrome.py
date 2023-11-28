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

    phrase = phrase.lower().replace(' ', '')

    i = 0
    j = len(phrase) - 1

    while i < j:

        if phrase[i] != phrase[j]:
            return False

        i += 1
        j -= 1

    return True

