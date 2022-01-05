import enum


class ContractRole(enum.Enum):
    """CNTRL :: Contract Role.

    CNTRL defines which position the CRID ( the creator of the contract record ) takes in a contract. For example, whether the contract is an asset or liability, a long or short position for the CRID. 
Most contracts are simple on or off balance sheet positions which are assets, liabilities. Such contracts can also play a secondary role as a collateral. 
The attribute is highly significant since it determines the direction of all cash flows. The exact meaning is given with each CT in the ACTUS High Level Specification document.

    """
    # Real Position Asset :: Contract creator takes the asset or lender side.
    RPA = 0

    # Real Position Liability :: Contract creator takes the liability or borrower side. 
    RPL = 1

    # Receive First Leg :: Contract creator receives the first leg. 
    RFL = 2

    # Pay First Leg :: Contract creator pays the first leg.
    PFL = 3

    # Receive Fix :: Contract creator receives the fixed leg.
    RF = 4

    # Pay Fix :: Contract creator pays the fixed leg.
    PF = 5

    # Buyer :: Contract creator holds the right to buy the underlying / exercise the option. 
    BUY = 6

    # Seller :: Contract creator holds the obligation to sell the underlying / deliver the option. 
    SEL = 7

    # Collateral Position :: Contract represents a collateral to an underlying instrument
    COL = 8

    # Close out Netting :: Contract creator and counterparty agree on netting payment obligations of underlying instruments in case of default. 
    CNO = 9

    # Underlying :: Contract represents the underlying to a composed contract. Role of the underlying is derived from the parent. 
    UDL = 10

    # Underlying Plus :: Contract represents the underlying to a composed contract. Role of the underlying is derived from the parent. When considered a standalone contract the underlying’s creator takes the asset side. 
    UDLP = 11

    # Underlying Minus :: Contract represents the underlying to a composed contract. Role of the underlying is derived from the parent. When considered a standalone contract the underlying’s creator takes the liability side.
    UDLM = 12

