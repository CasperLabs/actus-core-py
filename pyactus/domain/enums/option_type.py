import enum


class OptionType(enum.Enum):
    """OPTP :: Option Type.

    Defines whether the option is a call or put or a combination of it. This field has to be seen in combination with CNTRL where it is defined whether CRID is the buyer or the seller.

    """
    # Call :: Call option.
    C = 0

    # Put :: Put option.
    P = 1

    # Call-Put :: Combination of call and put option.
    CP = 2

