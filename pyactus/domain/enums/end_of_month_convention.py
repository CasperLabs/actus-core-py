import enum


class EndOfMonthConvention(enum.Enum):
    """EOMC :: End Of Month Convention.

    When computing schedules a special problem arises if an anchor date is at the end of a month and a cycle of monthly or quarterly is applied (yearly in the case of leap years only). How do we have to interpret an anchor date April 30 plus 1M cycles? In case where EOM is selected, it will jump to the 31st of May, then June 30, July 31 and so on. If SM is selected, it will jump to the 30st always with of course an exception in February. 
This logic applies for all months having 30 or less days and an anchor date at the last day. Month with 31 days will at any rate jump to the last of the month if anchor date is on the last day.

    """
    # Same Day :: Schedule times always fall on the schedule anchor date day of the month.
    SD = 0

    # End of Month :: Schedule times fall on the end of every month if the anchor date represents the last day of the respective month.
    EOM = 1

