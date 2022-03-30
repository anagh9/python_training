# A set of style guidelines for Python
# Readable code


# regular_variables

import random
a_tango_artist = 'Astor Piazzolla'

# constants
"""
In Python , all variables can be modified
Therefore real constraints don't exist
But to indicate that a variable should be treated as if it were a constant, names should be uppercase , where necessary separating words by undersores

"""
TANGO_ARTISTS = [
    'Artist Piozolla',
    'Abraham Vuhe'
]


# Function Name
# function_names()
# Names of functions and class methods should be lowercase , where necessary seperating by underscore


def random_tango_artist():
    return random.choice(TANGO_ARTISTS)


print(random_tango_artist())

# ClassNames
# Class names should capatalize the first letter of each word


class TangoArtist:
    def __init__(self, name) -> None:

        self.name = name

    def __str__(self) -> str:

        return self.name


ani = TangoArtist(name="Raone Trivia")
print(ani)  # Raone Trivia
