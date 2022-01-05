import enum


class ScalingEffect(enum.Enum):
    """SCEF :: Scaling Effect.

    Indicates which payments are scaled. I = Interest payments, N = Nominal payments and M = Maximum deferred interest amount. They can be scaled in any combination.

    """
    # No Scaling :: No scaling applies.
    _000 = 0

    # Interest is Scaled :: Scaling applies only to interest.
    I00 = 1

    # Principal is Scaled :: Scaling applies only to principal.
    _0N0 = 2

    # Interest and Principal is Scaled :: Scaling applies to interest and principal.
    IN0 = 3

