import enum


class ContractType(enum.Enum):
    """CT :: Contract Type.

    The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.

    """
    # Principal at Maturity :: Lending agreements with full amortization at maturity.
    PAM = 0

    # Annuity :: Lending agreements with fixed periodic payments consisting of an interest and principal portion. The periodic payments are adjusted for variable rate instruments such that maturity remains fixed.
    ANN = 1

    # Negative Amortizer :: Lending agreements with fixed periodic payments consisting of an interest and principal portion. Maturity changes for variable rate instruments. 
    NAM = 2

    # Linear Amortizer :: Lending agreements with fixed principal repayment amounts and variable interest payments.
    LAM = 3

    # Exotic Linear Amortizer :: Lending agreements with exotic repayment schedules.
    LAX = 4

    # Call Money :: Lonas that are rolled over as long as they are not called. Once called it has to be paid back after the stipulated notice period.
    CLM = 5

    # Undefined Maturity Profile :: Interest paying cash accounts (current / savings / etc.). 
    UMP = 6

    # Cash :: Represents cash holdings. 
    CSH = 7

    # Stock :: Represents stocks/shares/equity. 
    STK = 8

    # Commodity :: Represents commodities. 
    COM = 9

    # Swap :: An agreement of swapping two legs such as fixed against variable or currency 1 against currency 2 etc. 
    SWAPS = 10

    # Plain Vanilla Swap :: Plain vanilla interest rate swaps. 
    SWPPV = 11

    # Foreign Exchange Outright :: An agreement of swapping two cash flows in different currencies at a future point in time. 
    FXOUT = 12

    # Cap and Floor :: An agreement of paying the differential (cap or floor) of a reference rate versus a fixed rate. 
    CAPFL = 13

    # Future :: An agreement of exchanging an underlying instrument against a fixed price in the future. 
    FUTUR = 14

    # Option :: Different types of options on buying an underlying instrument at a fixed price in the future. 
    OPTNS = 15

    # Credit Enhancement Guarantee :: A guarantee / letter of credit by a third party on the scheduled payment obligations of an underlying instrument 
    CEG = 16

    # Credit Enhancement Collateral :: A collateral securing the scheduled payment obligations of an underlying instrument
    CEC = 17

