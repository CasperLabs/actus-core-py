import dataclasses
import datetime

from pyactus.domain import enums
from pyactus.domain import primitives


@dataclasses.dataclass
class Guarantee():
    """CEG :: Guarantee.

    Guarantee creates a relationship between a guarantor, an obligee and a debtor, moving the exposure from the debtor to the guarantor.

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
    
    # Contract Structure :: A structure identifying individual or sets of underlying contracts. E.g. for FUTUR, this structure identifies the single underlying contract, for SWAPS, the FirstLeg and SecondLeg are identified, or for CEG, CEC the structure identifies Covered and Covering contracts.
    contract_structure : ContractReference[]
    
    # Counterparty Identifier :: CPID identifies the counterparty to the CRID in this contract.CPID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can also refer to a annonymous group in which case this information is not to be disclosed. CPID may also refer to a group taking a joint risk or more generally, CPID is the main counterparty, against which the contract has been settled.
    counterparty_id : str
    
    # Contract Performance :: Indicates the current contract performance status. Different states of the contract range from performing to default.
    contract_performance : enums.ContractPerformance
    
    # Non Performing Date :: The date of the (uncovered) payment event responsible for the current value of the Contract Performance attribute.
    non_performing_date : datetime.datetime
    
    # Grace Period :: If real payment happens after scheduled payment date plus GRP, then the payment is in delay.
    grace_period : primitives.Period
    
    # Delinquency Period :: If real payment happens after scheduled payment date plus DLP, then the counterparty is in technical default. This means that the creditor legally has the right to declare default of the debtor.
    delinquency_period : primitives.Period
    
    # Delinquency Rate :: Rate at which Delinquency Payments accrue on NT (in addition to the interest rate) during the DelinquencyPeriod
    delinquency_rate : float
    
    # Guaranteed Exposure :: Defines which value of the exposure is covered:- NO: Nominal Value- NI: Nominal plus Interest- MV: Market Value
    guaranteed_exposure : enums.GuaranteedExposure
    
    # Coverage Of Credit Enhancement :: Defines which percentage of the exposure is covered
    coverage_of_credit_enhancement : float
    
    # Credit Event Type Covered :: The type of credit events covered e.g. in credit enhancement or credit default swap contracts. Only the defined credit event types may trigger the protection.
    credit_event_type_covered : Enum[]
    
    # Cycle Anchor Date Of Fee :: Date from which the fee payment date schedule is calculated according to the cycle length. The first fee payment event takes place on this anchor.
    cycle_anchor_date_of_fee : datetime.datetime
    
    # Cycle Of Fee :: Defines in combination with FEANX the payment points of fees
    cycle_of_fee : primitives.Cycle
    
    # Fee Basis :: Basis, on which Fee is calculated. For FEB=???A???, FER is interpreted as an absolute amount to be paid at every FP event and for FEB=???N???, FER represents a rate at which FP amounts accrue on the basis of the contract???s NT.
    fee_basis : enums.FeeBasis
    
    # Fee Rate :: Rate of Fee which is a percentage of the underlying or FER is an absolute amount. For all contracts where FEB does not apply (cf. business rules), FER is interpreted as an absolute amount.
    fee_rate : float
    
    # Fee Accrued :: Accrued fees as per SD
    fee_accrued : float
    
    # Currency :: The currency of the cash flows.
    currency : str
    
    # Contract Deal Date :: This date signifies the origination of the contract where an agreement between the customer and the bank has been settled. From this date on, the institution will have a (market) risk position for financial contracts. This is even the case when IED is in future.
    contract_deal_date : datetime.datetime
    
    # Maturity Date :: Marks the contractual end of the lifecycle of a CT. Generally, date of the last cash flows. This includes normally a principal and an interest payment. Some Maturity CTs as perpetuals (PBN) do not have such a date. For variable amortizing contracts of the ANN CT, this date might be less than the scheduled end of the contract (which is deduced from the periodic payment amount PRNXT). In this case it balloons.
    maturity_date : datetime.datetime
    
    # Notional Principal :: Current nominal value of the contract. For debt instrument this is the current remaining notional outstanding. NT is generally the basis on which interest payments are calculated. If IPCBS is set, IPCBS may introduce a different basis for interest payment calculation.
    notional_principal : float
    
    # Purchase Date :: If a contract is bought after initiation (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PPRD) and transfer of the security happens. In other words, PRD - if set - takes the role otherwise IED has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    purchase_date : datetime.datetime
    
    # Price At Purchase Date :: Purchase price exchanged at PRD.  PPRD represents a clean price (includes premium/discount but not IPAC).
    price_at_purchase_date : float
    
    # Termination Date :: If a contract is sold before MD (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PTD) and transfer of the security happens. In other words, TD - if set - takes the role otherwise MD has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    termination_date : datetime.datetime
    
    # Price At Termination Date :: Sellingprice exchanged at PTD  PTDrepresents a clean price (includes premium/discount but not IPAC
    price_at_termination_date : float
    
    # Exercise Date :: Date of exercising a contingent event/obligation such as a forward condition, optionality etc. The Exercise date marks the observed timestamp of fixing the contingent event and respective payment obligation not necessarily the timestamp of settling the obligation.
    exercise_date : datetime.datetime
    
    # Exercise Amount :: The amount fixed at Exercise Date for a contingent event/obligation such as a forward condition, optionality etc. The Exercise Amount is fixed at Exercise Date but not settled yet.
    exercise_amount : float
    
    # Settlement Period :: Defines the period from fixing of a contingent event/obligation (Exercise Date) to settlement of the obligation.
    settlement_period : primitives.Period
    
    # Settlement Currency :: The currency in which cash flows are settled. This currency can be different from the currency (CUR) in which cash flows or the contract, respectively, is denominated in which case the respective FX-rate applies at settlement time.If no settlement currency is defined the cash flows are settled in the currency in which they are denominated.
    settlement_currency : str
