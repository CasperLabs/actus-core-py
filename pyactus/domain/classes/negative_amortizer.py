import dataclasses
import datetime

from pyactus.domain import enums
from pyactus.domain import primitives


@dataclasses.dataclass
class NegativeAmortizer():
    """NAM :: Negative Amortizer.

    Similar as ANN. However when resetting rate, total amount (interest plus principal) stay constant. MD shifts. Only variable rates.

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
    
    # Seniority :: Refers to the order of repayment in the event of a sale or default of the issuer.??
    seniority : enums.Seniority
    
    # Non Performing Date :: The date of the (uncovered) payment event responsible for the current value of the Contract Performance attribute.
    non_performing_date : datetime.datetime
    
    # Prepayment Period :: If real payment happens before scheduled payment date minus PPP, then it is considered a prepayment. Effect of prepayments are further described in PPEF and related fields.
    prepayment_period : primitives.Period
    
    # Grace Period :: If real payment happens after scheduled payment date plus GRP, then the payment is in delay.
    grace_period : primitives.Period
    
    # Delinquency Period :: If real payment happens after scheduled payment date plus DLP, then the counterparty is in technical default. This means that the creditor legally has the right to declare default of the debtor.
    delinquency_period : primitives.Period
    
    # Delinquency Rate :: Rate at which Delinquency Payments accrue on NT (in addition to the interest rate) during the DelinquencyPeriod
    delinquency_rate : float
    
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
    
    # Cycle Anchor Date Of Interest Payment :: Date from which the interest payment date schedule is calculated according to the cycle length. The first interest payment event takes place on this anchor.
    cycle_anchor_date_of_interest_payment : datetime.datetime
    
    # Cycle Of Interest Payment :: Cycle according to which the interest payment date schedule will be calculated.In case IPCL is not set, then there will only be an interest payment event at MD (and possibly at IPANX if set).The interval will be adjusted yet by EOMC and BDC.
    cycle_of_interest_payment : primitives.Cycle
    
    # Nominal Interest Rate :: The nominal interest rate which will be used to calculate accruals and the next interest payment at the next IP date. NT multiplied with IPNR is the base for the interest payment calculation. The relevant time period is a function of IPDC. If the contract is variable (RRANX set) this field is periodically updated per SD. In the case of plan vanilla interest rate swaps (IRSPV) this defines the rate of fixed leg.
    nominal_interest_rate : float
    
    # Day Count Convention :: Method defining how days are counted between two dates. This finally defines the year fraction in accrual calculations.
    day_count_convention : enums.DayCountConvention
    
    # Accrued Interest :: Accrued interest as per SD. In case of NULL, this value will be recalculated using IPANX, IPCL and IPNR information. Can be used to represent irregular next IP payments.
    accrued_interest : float
    
    # Capitalization End Date :: If IPCED is set, then interest is not paid or received but added to the balance (NT) until IPCED. If IPCED does not coincide with an IP cycle, one additional interest payment gets calculated at IPCED and capitalized. Thereafter normal interest payments occur.
    capitalization_end_date : datetime.datetime
    
    # Cycle Anchor Date Of Interest Calculation Base :: Date from which the interest calculation base date schedule is calculated according to the cycle length. The first interest calculation base event takes place on this anchor.
    cycle_anchor_date_of_interest_calculation_base : datetime.datetime
    
    # Cycle Of Interest Calculation Base :: Concerning the format see PRCL. Defines the subsequent adjustment points to NT of the interest payment calculation base.
    cycle_of_interest_calculation_base : primitives.Cycle
    
    # Interest Calculation Base :: This is important for amortizing instruments. The basis of interest calculation is normally the notional outstanding amount as per SD. This is considered the fair basis and in many countries the only legal basis. If NULL or NTSD is selected, this is the case. Alternative bases (normally in order to favor the lending institution) are found. In the extreme case the original balance (PCDD=NT+PDCDD) never gets adjusted. In this case PCDD must be chosen. An intermediate case exist wherre balances do get adjusted, however with lags. In this case NTL mut be selected and anchor dates and cycles must be set.
    interest_calculation_base : enums.InterestCalculationBase
    
    # Interest Calculation Base Amount :: This is the amount used for the calculation of interest. Calculation base per SD.
    interest_calculation_base_amount : float
    
    # Currency :: The currency of the cash flows.
    currency : str
    
    # Contract Deal Date :: This date signifies the origination of the contract where an agreement between the customer and the bank has been settled. From this date on, the institution will have a (market) risk position for financial contracts. This is even the case when IED is in future.
    contract_deal_date : datetime.datetime
    
    # Initial Exchange Date :: Date of the initial cash flow for Maturity and Non-Maturity CT's. It also coincides with the beginning of interest accrual calculation.
    initial_exchange_date : datetime.datetime
    
    # Premium Discount At IED :: Total original premium or discount that has been set at CDD and will be added to the (notional) cash flow at IED (cash flow at IED = NT+PDIED, w.r.t. an RPA CT). Negative value for discount and positive for premium.Note, similar to interest the PDIED portion is part of P&L.
    premium_discount_at_ied : float
    
    # Maturity Date :: Marks the contractual end of the lifecycle of a CT. Generally, date of the last cash flows. This includes normally a principal and an interest payment. Some Maturity CTs as perpetuals (PBN) do not have such a date. For variable amortizing contracts of the ANN CT, this date might be less than the scheduled end of the contract (which is deduced from the periodic payment amount PRNXT). In this case it balloons.
    maturity_date : datetime.datetime
    
    # Notional Principal :: Current nominal value of the contract. For debt instrument this is the current remaining notional outstanding. NT is generally the basis on which interest payments are calculated. If IPCBS is set, IPCBS may introduce a different basis for interest payment calculation.
    notional_principal : float
    
    # Cycle Anchor Date Of Principal Redemption :: Date from which the principal payment date schedule is calculated according to the cycle length. The first principal payment event takes place on this anchor.
    cycle_anchor_date_of_principal_redemption : datetime.datetime
    
    # Cycle Of Principal Redemption :: Cycle according to which the interest payment date schedule will be calculated.In case PRCL is not set, then there will only be one principal payment event at MD (and possibly at PRANX if set).The interval will be adjusted yet by EOMC and BDC.
    cycle_of_principal_redemption : primitives.Cycle
    
    # Next Principal Redemption Payment :: Amount of principal that will be paid during the redemption cycle at the next payment date. For amortizing contracts like ANN, NAM, ANX, and NAX this is the total periodic payment amount (sum of interest and principal).
    next_principal_redemption_payment : float
    
    # Purchase Date :: If a contract is bought after initiation (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PPRD) and transfer of the security happens. In other words, PRD - if set - takes the role otherwise IED has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    purchase_date : datetime.datetime
    
    # Price At Purchase Date :: Purchase price exchanged at PRD.  PPRD represents a clean price (includes premium/discount but not IPAC).
    price_at_purchase_date : float
    
    # Termination Date :: If a contract is sold before MD (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PTD) and transfer of the security happens. In other words, TD - if set - takes the role otherwise MD has from a cash flow perspective. Note, CPID of the CT is not the counterparty of the transaction!
    termination_date : datetime.datetime
    
    # Price At Termination Date :: Sellingprice exchanged at PTD  PTDrepresents a clean price (includes premium/discount but not IPAC
    price_at_termination_date : float
    
    # Credit Line Amount :: If defined, gives the total amount that can be drawn from a credit line. The remaining amount that can still be drawn is given by CLA-NT.For ANN, NAM, the credit line can only be drawn prior to PRANX-1PRCL.For CRL, the remaining amount that can still be drawn is given by CLA-Sum(NT of attached contracts).
    credit_line_amount : float
    
    # Market Object Code Of Scaling Index :: Market Object Code Of Scaling Index
    market_object_code_of_scaling_index : str
    
    # Scaling Index At Contract Deal Date :: The value of the Scaling Index as per Contract Deal Date.
    scaling_index_at_contract_deal_date : float
    
    # Notional Scaling Multiplier :: The multiplier being applied to principal cash flows
    notional_scaling_multiplier : float
    
    # Interest Scaling Multiplier :: The multiplier being applied to interest cash flows
    interest_scaling_multiplier : float
    
    # Cycle Anchor Date Of Scaling Index :: Date from which the scaling date schedule is calculated according to the cycle length. The first scaling event takes place on this anchor.
    cycle_anchor_date_of_scaling_index : datetime.datetime
    
    # Cycle Of Scaling Index :: Cycle according to which the scaling date schedule will be calculated.In case SCCL is not set, then there will only be one scaling event at SCANX given SCANX is set.The interval will be adjusted yet by EOMC and BDC.
    cycle_of_scaling_index : primitives.Cycle
    
    # Scaling Effect :: Indicates which payments are scaled. I = Interest payments, N = Nominal payments and M = Maximum deferred interest amount. They can be scaled in any combination.
    scaling_effect : enums.ScalingEffect
    
    # Market Value Observed :: Value as observed in the market at SD per unit. Incase of fixed income instruments it is a fraction.
    market_value_observed : float
    
    # Option Exercise End Date :: Final exercise date for American and Bermudan options, expiry date for European options.
    option_exercise_end_date : datetime.datetime
    
    # Cycle Anchor Date Of Optionality :: Used for Basic Maturities (such as PAM, RGM, ANN, NGM and their Step-up versions) and American and Bermudan style options. - Basic Maturities: Within the group of these Maturities, it indicates the possibility of prepayments. Prepayment features are controlled by Behavior. - American and Bermudan style Options: Begin of exercise period.
    cycle_anchor_date_of_optionality : datetime.datetime
    
    # Cycle Of Optionality :: Cycle according to which the option exercise date schedule will be calculated.OPCL can be NULL for American Options or Prepayment Optionality in which case the optionality period starts at OPANX and ends at OPXED (for american options) or MD (in case of prepayment optionality).The interval will be adjusted yet by EOMC and BDC.
    cycle_of_optionality : primitives.Cycle
    
    # Penalty Type :: Defines whether prepayment is linked to a penalty and of which kind.
    penalty_type : enums.PenaltyType
    
    # Penalty Rate :: Either the rate or the absolute amount of the prepayment.
    penalty_rate : float
    
    # Prepayment Effect :: This attribute defines whether or not the right of prepayment exists and if yes, how prepayment affects the remaining principal redemption schedule of the contract
    prepayment_effect : enums.PrepaymentEffect
    
    # Cycle Anchor Date Of Rate Reset :: Date from which the rate reset date schedule is calculated according to the cycle length. The first rate reset event takes place on this anchor.
    cycle_anchor_date_of_rate_reset : datetime.datetime
    
    # Cycle Of Rate Reset :: Cycle according to which the rate reset date schedule will be calculated.In case RRCL is not set, then there will only be one rate reset event at RRANX given RRANX if set.The interval will be adjusted yet by EOMC and BDC.
    cycle_of_rate_reset : primitives.Cycle
    
    # Rate Spread :: Interest rate spread. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest rate spread.  The following equation can be taken if RRMLT is not set: IPNR after rate reset = Rate selected from the market object  + RRSP.
    rate_spread : float
    
    # Market Object Code Of Rate Reset :: Is pointing to the interest rate driver (MarketObject) used for rate reset uniquely.Unique codes for market objects must be used.
    market_object_code_of_rate_reset : str
    
    # Life Cap :: For variable rate basic CTs this represents a cap on the interest rate that applies during the entire lifetime of the contract.For CAPFL CTs this represents the cap strike rate.
    life_cap : float
    
    # Life Floor :: For variable rate basic CTs this represents a floor on the interest rate that applies during the entire lifetime of the contract.For CAPFL CTs this represents the floor strike rate.
    life_floor : float
    
    # Period Cap :: For variable rate basic CTs this represents the maximum positive rate change per rate reset cycle.
    period_cap : float
    
    # Period Floor :: For variable rate basic CTs this represents the maximum negative rate change per rate reset cycle.
    period_floor : float
    
    # Fixing Period :: Interest rate resets (adjustments) are usually fixed one or two days (usually Business Days) before the new rate applies (defined by the rate reset schedule). This field holds the period between fixing and application of a rate.
    fixing_period : primitives.Period
    
    # Next Reset Rate :: Holds the new rate that has been fixed already (cf. attribute FixingDays) but not applied. This new rate will be applied at the next rate reset event (after SD and according to the rate reset schedule). Attention, RRNXT must be set to NULL after it is applied!
    next_reset_rate : float
    
    # Rate Multiplier :: Interest rate multiplier. A typical rate resetting rule is LIBOR plus x basis point where x represents the interest rate spread.However, in some cases like reverse or super floater contracts an additional rate multiplier applies. In this case, the new rate is determined as: IPNR after rate reset = Rate selected from the market object * RRMLT + RRSP.
    rate_multiplier : float
    
    # Settlement Currency :: The currency in which cash flows are settled. This currency can be different from the currency (CUR) in which cash flows or the contract, respectively, is denominated in which case the respective FX-rate applies at settlement time.If no settlement currency is defined the cash flows are settled in the currency in which they are denominated.
    settlement_currency : str
