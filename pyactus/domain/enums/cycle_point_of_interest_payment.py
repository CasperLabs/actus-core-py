import enum


class CyclePointOfInterestPayment(enum.Enum):
    """IPPNT :: Cycle Point Of Interest Payment.

    Usually, interest is paid at the end of each IPCL which corresponds to a IPPNT value of E which is also the default. If interest payment occurs at the beginning of the cycle, the value is B.

    """
    # Beginning :: Interest is paid upfront of the interest period.
    B = 0

    # End :: Interest is paid at the end of the interest period.
    E = 1

