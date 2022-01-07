import dataclasses
import datetime

from pyactus.domain import enums
from pyactus.domain import primitives


@dataclasses.dataclass
class Stock():
    """STK :: Stock.

    Any instrument which is bought at a certain amount (market price normally) and then follows an index.

    """
    
    # Calendar :: Calendar defines the non-working days which affect the dates of contract events (CDE's) in combination with EOMC and BDC. Custom calendars can be added as additional enum options.
    calendar : enums.Calendar
    
    # Business Day Convention :: BDC's are linked to a calendar. Calendars have working and non-working days. A BDC value other than N means that cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding).These two simple rules get refined twofold:- Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month, then  it is shifted to preceding (following) business day.- Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other way round.Attention: Does not affect non-cyclical dates such as PRD, MD, TD, IPCED since they can be set to the correct date directly.
    business_day_convention : enums.BusinessDayConvention
    
    # End Of Month Convention :: When computing schedules a special problem arises if an anchor date is at the end of a month and a cycle of monthly or quarterly is applied (yearly in the case of leap years only). How do we have to interpret an anchor date April 30 plus 1M cycles? In case where EOM is selected, it will jump to the 31st of May, then June 30, July 31 and so on. If SM is selected, it will jump to the 30st always with of course an exception in February. This logic applies for all months having 30 or less days and an anchor date at the last day. Month with 31 days will at any rate jump to the last of the month if anchor date is on the last day.
    end_of_month_convention : enums.EndOfMonthConvention
    
    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type : enums.ContractType
    
    # Status Date :: SD holds the date per which all attributes of the record were updated. This is especially important for the highly dynamic attributes like Accruals, Notional, interest rates in variable instruments etc.
    status_date : datetime.datetime
    
    # Contract Role :: CNTRL defines which position the CRID ( the creator of the contract record ) takes in a contract. For example, whether the contract is an asset or liability, a long or short position for the CRID. Most contracts are simple on or off balance sheet positions which are assets, liabilities. Such contracts can also play a secondary role as a collateral. The attribute is highly significant since it determines the direction of all cash flows. The exact meaning is given with each CT in the ACTUS High Level Specification document.
    contract_role : enums.ContractRole
    
    # Creator Identifier :: This identifies the legal entity creating the contract record. The counterparty of the contract is tracked in CPID.CRID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can also refer to a annonymous group in which case this information is not to be disclosed. CRID may also refer to a group taking a joint risk.
    creator_id : str
    
    # Contract Identifier :: Unique identifier of a contract.  If the system is used on a single firm level, an internal unique ID can be generated. If used on a national or globally level, a globally unique ID is required.
    contract_id : str
    
    # Market Object Code :: Is pointing to the market value at SD (MarketObject).Unique codes for market objects must be used.
    market_object_code : str
    
    # Counterparty Identifier :: CPID identifies the counterparty to the CRID in this contract.CPID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can also refer to a annonymous group in which case this information is not to be disclosed. CPID may also refer to a group taking a joint risk or more generally, CPID is the main counterparty, against which the contract has been settled.
    counterparty_id : str
    
    # Contract Performance :: Indicates the current contract performance status. Different states of the contract range from performing to default.
    contract_performance : enums.ContractPerformance
    
    # Seniority :: Refers to the order of repayment in the event of a sale or default of the issuer. 
    seniority : enums.Seniority
    
    # Non Performing Date :: The date of the (uncovered) payment event responsible for the current value of the Contract Performance attribute.
    non_performing_date : datetime.datetime
    
    # Cycle Anchor Date Of Dividend :: Date from which the dividend payment date schedule is calculated according to the cycle length. The first dividend payment event takes place on this anchor.
    cycle_anchor_date_of_dividend : datetime.datetime
    
    # Cycle Of Dividend :: Defines in combination with DVANX the payment points of dividends. The dividend payment schedule will start at DVANX and end at MaximumProjectionPeriod (cf. sheet Modeling Parameters).
    cycle_of_dividend : primitives.Cycle
    
    # Next Dividend Payment Amount :: Defines the next dividend payment (amount) whereas the date of dividend payment is defined through the DVANX/DVCL pair. If DVCL is defined, then this amount will be used as dividend payment for each future dividend payment date.
    next_dividend_payment_amount : float
    
    # Ex Dividend Date :: In case contract is traded between DVEX and next DV payment date (i.e. PRD>DVEX & PRD<next DV payment date), then the old holder of the contract (previous to the trade) receives the next DV payment. In other words, the next DV payment is cancelled for the new (after the trade) holder of the contract.
    ex_dividend_date : datetime.datetime
    
    # Currency :: The currency of the cash flows.
    currency : str
    
    # Contract Deal Date :: This date signifies the origination of the contract where an agreement between the customer and the bank has been settled. From this date on, the institution will have a (market) risk position for financial contracts. This is even the case when IED is in future.
    contract_deal_date : datetime.datetime
    
    # Notional Principal :: Current nominal value of the contract. For debt instrument this is the current remaining notional outstanding. NT is generally the basis on which interest payments are calculated. If IPCBS is set, IPCBS may introduce a different basis for interest payment calculation.
    notional_principal : float
    
    # Quantity :: This attribute relates either to physical contracts (COM) or underlyings of traded contracts. In case of physical contracts it holds the number of underlying units of the specific good (e.g. number of barrels of oil). In case of well defined traded contracts it holds the number of defined underlying instruments. Example: QT of STK CTs underlying a FUTUR indicates the number of those specific STK CTs which underlie the FUTUR.
    quantity : float
    
    # Purchase Date :: If a contract is bought after initiation (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PPRD) and transfer of the security happens. In other words, PRD - if set - takes the role otherwise IED has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    purchase_date : datetime.datetime
    
    # Price At Purchase Date :: Purchase price exchanged at PRD.  PPRD represents a clean price (includes premium/discount but not IPAC).
    price_at_purchase_date : float
    
    # Termination Date :: If a contract is sold before MD (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PTD) and transfer of the security happens. In other words, TD - if set - takes the role otherwise MD has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    termination_date : datetime.datetime
    
    # Price At Termination Date :: Sellingprice exchanged at PTD  PTDrepresents a clean price (includes premium/discount but not IPAC
    price_at_termination_date : float
    
    # Market Value Observed :: Value as observed in the market at SD per unit. Incase of fixed income instruments it is a fraction.
    market_value_observed : float
    
    # Settlement Currency :: The currency in which cash flows are settled. This currency can be different from the currency (CUR) in which cash flows or the contract, respectively, is denominated in which case the respective FX-rate applies at settlement time.If no settlement currency is defined the cash flows are settled in the currency in which they are denominated.
    settlement_currency : str
