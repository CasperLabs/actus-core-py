import enum


class Unit(enum.Enum):
    """UT :: Unit.

    The physical unit of the contract. Example: Barrels for an Oil COM CT.

    """
    # Barrel :: Physical unit of the contract is Barrels.
    BRL = 0

    # Bushel :: Physical unit of the contract is Bushel.
    BSH = 1

    # Gallon :: Physical unit of the contract is Gallons.
    GLN = 2

    # Currency Unit :: Physical unit of the contract is Currency Units.
    CUU = 3

    # Mega Watt Hours :: Physical unit of the contract is Mega Watt Hours.
    MWH = 4

    # Pounds :: Physical unit of the contract is Pounds.
    PND = 5

    # Short Tons :: Physical unit of the contract is Short Tons.
    STN = 6

    # Tons :: Physical unit of the contract is Tons.
    TON = 7

    # Troy Ounce :: Physical unit of the contract is Troy Ounces.
    TRO = 8

