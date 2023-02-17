from enum import Enum


class SheetProperties(Enum):
    """
    Enumeration class that aims to help making the music sheet which gives preset parameters
    """

    # Privates variables
    __sharp = []
    __flat = []
    __natural = []

    # The keys
    TREBLE_KEY = 0
    BASS_KEY = 1

    # The accidentals
    SHARP = "#"
    FLAT = "♭"
    NATURAL = "♮"
