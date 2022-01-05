import enum


class PenaltyType(enum.Enum):
    """PYTP :: Penalty Type.

    Defines whether prepayment is linked to a penalty and of which kind.

    """
    # No Penalty :: No penalty applies.
    N = 0

    # Fixed Penalty :: A fixed amount applies as penalty.
    A = 1

    # Relative Penalty :: A penalty relative to the notional outstanding applies.
    R = 2

    # Interest Rate Differential :: A penalty based on the current interest rate differential relative to the notional outstanding applies.
    I = 3

