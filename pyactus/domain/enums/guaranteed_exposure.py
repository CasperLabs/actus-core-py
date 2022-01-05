import enum


class GuaranteedExposure(enum.Enum):
    """CEGE :: Guaranteed Exposure.

    Defines which value of the exposure is covered:
- NO: Nominal Value
- NI: Nominal plus Interest
- MV: Market Value

    """
    # Nominal Value :: Nominal value of the exposure is covered.
    NO = 0

    # Nominal Value plus Interest :: Nominal value of the exposure plus interest accrued is covered.
    NI = 1

    # Market Value :: Market value of the exposure is covered.
    MV = 2

