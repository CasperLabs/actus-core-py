import dataclasses
import datetime

from pyactus.domain import enums
from pyactus.domain import primitives


@dataclasses.dataclass
class Commodity():
    """COM :: Commodity.

    This is not a financial contract in its propper sense. However it traks movements of commodities such as oil, gas or even houses. Such commodities can serve as underlyings of commodity futures, guarantees or simply asset positions.

    """
    
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
    
    # Currency :: The currency of the cash flows.
    currency : str
    
    # Contract Deal Date :: This date signifies the origination of the contract where an agreement between the customer and the bank has been settled. From this date on, the institution will have a (market) risk position for financial contracts. This is even the case when IED is in future.
    contract_deal_date : datetime.datetime
    
    # Quantity :: This attribute relates either to physical contracts (COM) or underlyings of traded contracts. In case of physical contracts it holds the number of underlying units of the specific good (e.g. number of barrels of oil). In case of well defined traded contracts it holds the number of defined underlying instruments. Example: QT of STK CTs underlying a FUTUR indicates the number of those specific STK CTs which underlie the FUTUR.
    quantity : float
    
    # Unit :: The physical unit of the contract. Example: Barrels for an Oil COM CT.
    unit : enums.Unit
    
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
