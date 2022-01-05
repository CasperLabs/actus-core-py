import enum


class DeliverySettlement(enum.Enum):
    """DS :: Delivery Settlement.

    Indicates whether the contract is settled in cash or physical delivery.
In case of physical delivery, the underlying contract and associated (future) cash flows are effectively exchanged. In case of cash settlement, the current market value of the underlying contract determines the cash flow exchanged.

    """
    # Cash Settlement :: The market value of the underlying is settled.
    S = 0

    # Physical Settlement :: The underlying is delivered physically.
    D = 1

