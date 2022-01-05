import enum


class InterestCalculationBase(enum.Enum):
    """IPCB :: Interest Calculation Base.

    This is important for amortizing instruments. The basis of interest calculation is normally the notional outstanding amount as per SD. This is considered the fair basis and in many countries the only legal basis. If NULL or NTSD is selected, this is the case. 
Alternative bases (normally in order to favor the lending institution) are found. In the extreme case the original balance (PCDD=NT+PDCDD) never gets adjusted. In this case PCDD must be chosen. 
An intermediate case exist wherre balances do get adjusted, however with lags. In this case NTL mut be selected and anchor dates and cycles must be set.

    """
    # Notional Outstanding :: Interest accrues on the basis of the notional outstanding.
    NT = 0

    # Notional at Initial Exchange :: Interest accrues on the basis of the notional value at initial exchange.
    NTIED = 1

    # Notional Outstanding Lagged :: Interest accrues on the basis of the lagged notional outstanding.
    NTL = 2

