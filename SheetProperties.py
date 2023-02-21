from enum import Enum


class SheetProperties(Enum):
    """
    Enumeration class that aims to help making the music sheet which gives preset parameters
    """

    # Privates variables
    __sharp = ["Fa", "Do", "Sol", "Re", "La", "Mi", "Si"]
    __flat = ["Si", "Mi", "La", "Re", "Sol", "Do", "Fa"]
    # __natural = []

    # The keys
    TREBLE_CLEF = 0
    BASS_CLEF = 1

    # The accidentals
    SHARP = "#"
    FLAT = "♭"
    NATURAL = "♮"
