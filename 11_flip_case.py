def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    modded_phrase = ""

    for letter in phrase:
        # make it lowercase outside of the loop
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()

        modded_phrase += letter

    return modded_phrase
