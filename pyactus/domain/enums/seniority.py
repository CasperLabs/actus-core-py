import enum


class Seniority(enum.Enum):
    """SEN :: Seniority.

    Refers to the order of repayment in the event of a sale or default of the issuer. 

    """
    # Senior :: Contract represents senior debt.
    S = 0

    # Junior :: Contract represents junior debt.
    J = 1

