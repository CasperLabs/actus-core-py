import enum


class Calendar(enum.Enum):
    """CLDR :: Calendar.

    Calendar defines the non-working days which affect the dates of contract events (CDE's) in combination with EOMC and BDC. Custom calendars can be added as additional enum options.

    """
    # No Calendar :: No holidays defined
    NC = 0

    # MondayToFriday :: Saturdays and Sundays are holidays
    MF = 1

