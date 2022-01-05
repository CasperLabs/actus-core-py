import enum


class ClearingHouse(enum.Enum):
    """MRCLH :: Clearing House.

    Indicates wheter CRID takes a clearing house function or not. In other word, whether CRID receive margins (MRIM, MRVM).

    """
    # Is Clearing House :: Contract creator is the clearing house.
    Y = 0

    # Is Not Clearing House :: Contract creator is not the clearing house.
    N = 1

