# Based heavily on the example given on markovify's github page.

import markovify


def message():
    # Get raw text as string.
    with open("big.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print three randomly-generated sentences of no more than 140 characters
    return text_model.make_short_sentence(135) + " Arr!"
