import enum


class ContractPerformance(enum.Enum):
    """PRF :: Contract Performance.

    Indicates the current contract performance status. Different states of the contract range from performing to default.

    """
    # Performant :: Contract is performing according to terms and conditions.
    PF = 0

    # Delayed :: Contractual payment obligations are delayed according to the Grace Period.
    DL = 1

    # Delinquent :: Contractual payment obligations are delinquent according to the Delinquency Period.
    DQ = 2

    # Default :: Contract defaulted on payment obligations according to Delinquency Period.
    DF = 3

    # Matured :: Contract matured.
    MA = 4

    # Terminated :: Contract has been terminated.
    TE = 5

