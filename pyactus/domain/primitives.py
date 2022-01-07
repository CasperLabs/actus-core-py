import datetime
import typing


# Time period.
Period = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)

# Time period.
Cycle = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)

# XXXXXX.
ContractReference = typing.NewType("XXXXXXXX.", datetime.timedelta)
