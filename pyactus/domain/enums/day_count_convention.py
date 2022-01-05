import enum


class DayCountConvention(enum.Enum):
    """IPDC :: Day Count Convention.

    Method defining how days are counted between two dates. This finally defines the year fraction in accrual calculations.

    """
    # Actual/Actual :: Year fractions accrue on the basis of the actual number of days per month and per year in the respective period.
    AA = 0

    # Actual Three Sixty :: Year fractions accrue on the basis of the actual number of days per month and 360 days per year in the respective period.
    A360 = 1

    # Actual Three Sixty Five :: Year fractions accrue on the basis of the actual number of days per month and 365 days per year in the respective period.
    A365 = 2

    # Thirty E Three Sixty ISDA :: Year fractions accrue on the basis of 30 days per month and 360 days per year in the respective period (ISDA method).
    _30E360ISDA = 3

    # Thirty E Three Sixty :: Year fractions accrue on the basis of 30 days per month and 360 days per year in the respective period.
    _30E360 = 4

    # Twenty Eight E Three Thirty Six :: Year fractions accrue on the basis of 28 days per month and 336 days per year in the respective period.
    _28E336 = 5

