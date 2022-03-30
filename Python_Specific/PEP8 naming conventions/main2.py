# FactoryFunctionNames()

# Factory functions return objects
# Therefore to users of your code , factory functions act like class definations
# To reflect this,factory functions names should also capatalize the first letter of each word
class TangoArtist:
    def __init__(self, name) -> None:

        self.name = name

    def __str__(self) -> str:

        return self.name


def AstorPiazolla():
    return TangoArtist(name='Astor Piozolla')


a = AstorPiazolla()
print(a)

"""
_non_public_properties
In Python properties can be accesed from anywhere
Therefore , Private class properties don't exist
But to indicate that a property should be treated as if it were privte,names should be prefixed with the underscore

"""


class HugoDiaz(TangoArtist):
    def __init__(self) -> None:

        TangoArtist.__init__(self, name='Hugo Diaz')
        self._instrument = 'Hormonica'

    @property
    def instrument(self):

        return self._instrument


hugo_diaz = HugoDiaz()
print(hugo_diaz.instrument)


"""

conflicting_names_
If a name is already taken, suffix an underscore

"""

in_ = 'Tango'
