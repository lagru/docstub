"""Basic docstring examples.

Docstrings, including module-level ones, are stripped.
"""

# Existing imports are preserved
import logging

# Assign-statements are preserved
logger = logging.getLogger(__name__)  # Inline comments are stripped


__all__ = [
    "func_empty",
    "ExampleClass",
]


def func_empty(a1, a2, a3):
    """Empty type descriptions will be replaced with "Any".

    Parameters
    ----------
    a1 :
    a2
    """


def func_contains(self, a1, a2, a3, a4):
    """Dummy.

    Parameters
    ----------
    a1 : list[float]
    a2 : dict[str, Union[int, str]]
    a3 : Sequence[int | float]
    a4 : frozenset[bytes]

    Returns
    -------
    r1 : tuple of int
    r2 : list of int
    """


def func_literals(a1, a2="uno"):
    """Dummy

    Parameters
    ----------
    a1 : {1, 3, "foo"}
    a2 : {"uno", 2, "drei", "four"}, default: "uno"
    """


def func_use_from_elsewhere(a1, a2):
    """Check if types with full import names are matched.

    Parameters
    ----------
    a1 : example_pkg.CustomException
    a2 : ExampleClass

    Returns
    -------
    r1 : ~.CustomException
    """


class ExampleClass:
    """Dummy.

    Parameters
    ----------
    a1 : str
    a2 : float, optional
    """

    def __init__(self, a1, a2=None):
        pass

    def method(self, a1, a2):
        """Dummy.

        Parameters
        ----------
        a1 : float
        a2 : float, optional

        Returns
        -------
        r1 : list of float
        """

    @staticmethod
    def some_staticmethod(a1, a2="uno"):
        """Dummy

        Parameters
        ----------
        a1 : float
        a2 : float, optional

        Returns
        -------
        r1 : dict[str, Any]
        """

    @property
    def some_property(self):
        """Dummy

        Returns
        -------
        name : str
        """
        return str(self)

    @some_property.setter
    def some_property(self, value):
        """Dummy

        Parameters
        ----------
        value : str
        """

    @classmethod
    def method_returning_cls(cls, config):
        """Using `Self` in context of classmethods is supported.

        Parameters
        ----------
        config : configparser.ConfigParser
            Configuation.

        Returns
        -------
        out : Self
            New class.
        """

    @classmethod()
    def method_returning_cls2(cls, config):
        """Using `Self` in context of classmethods is supported.

        Parameters
        ----------
        config : configparser.ConfigParser
            Configuation.

        Returns
        -------
        out : Self
            New class.
        """
