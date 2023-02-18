from enum import Enum


class NoteProperties(Enum):
    """
    Enumeration class that aims to help making notes and which gives preset parameters
    """

    # Notes type  --->  [Name] = [Duration]
    WHOLE = 4
    HALF = 2
    QUARTER = 1
    HEIGHTH = 1/2
    SIXTEENTH = 1/4
    THIRTY_SECOND = 1/8

    # Notes name
    DO = "Do"
    RE = "Re"
    MI = "Mi"
    FA = "Fa"
    SOL = "Sol"
    LA = "La"
    SI = "Si"

    # Note level
    BASS = -1
    MEDIUM = 0
    HIGHT = 1
