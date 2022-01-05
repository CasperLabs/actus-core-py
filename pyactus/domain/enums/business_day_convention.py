import enum


class BusinessDayConvention(enum.Enum):
    """BDC :: Business Day Convention.

    BDC's are linked to a calendar. Calendars have working and non-working days. A BDC value other than N means that cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding).
These two simple rules get refined twofold:
- Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month, then  it is shifted to preceding (following) business day.
- Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other way round.
Attention: Does not affect non-cyclical dates such as PRD, MD, TD, IPCED since they can be set to the correct date directly.

    """
    # No Shift :: No shift applied to non-business days.
    NOS = 0

    # Shift-Calculate Following :: Shift event dates first then calculate accruals etc. Strictly shift to the next following business day.
    SCF = 1

    # Shift-Calculate Modified-Following :: Shift event dates first then calculate accruals etc. Shift to the next following business day if this falls in the same month. Shift to the most recent preceding business day otherwise.
    SCMF = 2

    # Calculate-Shift Following :: Calculate accruals etc. first then shift event dates. Strictly shift to the next following business day.
    CSF = 3

    # Calculate-Shift Modified-Following :: Calculate accruals etc. first then shift event dates. Shift to the next following business day if this falls in the same month. Shift to the most recent preceding business day otherwise.
    CSMF = 4

    # Shift-Calculate Preceding :: Shift event dates first then calculate accruals etc. Strictly shift to the most recent preceding business day.
    SCP = 5

    # Shift-Calculate Modified-Preceding :: Shift event dates first then calculate accruals etc. Shift to the most recent preceding business day if this falls in the same month. Shift to the next following business day otherwise.
    SCMP = 6

    # Calculate-Shift Preceding :: Calculate accruals etc. first then shift event dates. Strictly shift to the most recent preceding business day.
    CSP = 7

    # Calculate-Shift Modified-Preceding :: Calculate accruals etc. first then shift event dates. Shift to the most recent preceding business day if this falls in the same month. Shift to the next following business day otherwise.
    CSMP = 8

