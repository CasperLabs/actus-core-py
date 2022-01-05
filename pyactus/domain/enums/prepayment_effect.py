import enum


class PrepaymentEffect(enum.Enum):
    """PPEF :: Prepayment Effect.

    This attribute defines whether or not the right of prepayment exists and if yes, how prepayment affects the remaining principal redemption schedule of the contract

    """
    # No Prepayment :: Prepayment is not allowed under the agreement.
    N = 0

    # Prepayment Reduces Redemption Amount :: Prepayment is allowed and reduces the redemption amount for the remaining period up to maturity.
    A = 1

    # Prepayment Reduces Maturity :: Prepayment is allowed and reduces the maturity.
    M = 2

