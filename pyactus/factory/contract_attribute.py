import datetime

from pyactus.domain import ContractAttribute
from pyactus.domain import ContractAttributeSet
from pyactus.domain import ContractRole
from pyactus.domain import ContractType


def create_attribute(contract_type: ContractType, name: str, value: object) -> ContractAttribute:
    try:
        contract_parser = _PARSERS[contract_type]
    except KeyError:
        contract_parser = _PARSERS[ContractType.PAM]

    try:
        value_parser = contract_parser[name]
    except KeyError:
        value_parser = to_string

    return ContractAttribute(contract_type, name, value_parser(value))


def to_contract_role(val: str) -> ContractRole:
    return None if val is None else ContractRole[val]


def to_contract_type(val: str) -> ContractRole:
    return ContractType[val]


def to_rate(val: str) -> float:
    print(444, val)
    return float(val)


def to_iso_datetime(val: str):
    return datetime.datetime.fromisoformat(val)


def to_iso_datetime_T00(val: str):
    val = to_iso_datetime(val)

    return val.replace(hour=0, minute=0, second=0, microsecond=0)


def to_iso_datetime_T24(val: str):
    val = to_iso_datetime(val)

    return val.replace(hour=23, minute=59, second=59, microsecond=0)


def to_string(val: str) -> str:
    return val


def to_optional(val: str, convertor, null_value: object):
    pass


_PARSERS = {
    ContractType.PAM: {
        "contractRole": to_contract_role,
        "contractType": to_contract_type,
        "statusDate": to_iso_datetime_T24,
        "feeRate": to_rate
    }
}


_PARSERS1 = {
    ContractType.PAM: {
        "ContractRole": ("contractRole", to_contract_role, ValueError),
        "ContractType": ("contractType", to_contract_type, ValueError),
        "contractType": to_contract_type,
        "statusDate": to_iso_datetime_T24,
        "feeRate": to_optional("feeRate", to_rate, float())
    }
}


# map.put("Calendar", (!CommonUtils.isNull(attributes.get("calendar")) && attributes.get("calendar").equals("MF")) ? new MondayToFridayCalendar() : new NoHolidaysCalendar());
# map.put("BusinessDayConvention", new BusinessDayAdjuster(CommonUtils.isNull(attributes.get("businessDayConvention")) ? null : BusinessDayConventionEnum.valueOf(attributes.get("businessDayConvention")), (BusinessDayCalendarProvider) map.get("Calendar")));
# map.put("EndOfMonthConvention", (CommonUtils.isNull(attributes.get("endOfMonthConvention"))) ? EndOfMonthConventionEnum.SD : EndOfMonthConventionEnum.valueOf(attributes.get("endOfMonthConvention")));
# --- map.put("ContractType", ContractTypeEnum.valueOf(attributes.get("contractType")));
# --- map.put("ContractID", attributes.get("contractID"));
# --- map.put("StatusDate", LocalDateTime.parse(attributes.get("statusDate")));
# --- map.put("ContractRole", (!CommonUtils.isNull(attributes.get("contractRole"))) ? ContractRole.valueOf(attributes.get("contractRole")) : null);
# map.put("CounterpartyID", attributes.get("counterpartyID"));
# map.put("MarketObjectCode", attributes.get("marketObjectCode"));
# map.put("CycleAnchorDateOfFee", (CommonUtils.isNull(attributes.get("cycleAnchorDateOfFee"))) ? ((CommonUtils.isNull(attributes.get("cycleOfFee"))) ? null : LocalDateTime.parse(attributes.get("initialExchangeDate"))) : LocalDateTime.parse(attributes.get("cycleAnchorDateOfFee")));
# map.put("CycleOfFee", attributes.get("cycleOfFee"));
# map.put("FeeBasis", (CommonUtils.isNull(attributes.get("feeBasis"))) ? null : FeeBasis.valueOf(attributes.get("feeBasis")));
# map.put("FeeRate", (CommonUtils.isNull(attributes.get("feeRate"))) ? 0.0 : Double.parseDouble(attributes.get("feeRate")));
# map.put("FeeAccrued", (CommonUtils.isNull(attributes.get("feeAccrued"))) ? 0.0 : Double.parseDouble(attributes.get("feeAccrued")));
# map.put("CycleAnchorDateOfInterestPayment", (CommonUtils.isNull(attributes.get("cycleAnchorDateOfInterestPayment"))) ? ((CommonUtils.isNull(attributes.get("cycleOfInterestPayment"))) ? null : LocalDateTime.parse(attributes.get("initialExchangeDate"))) : LocalDateTime.parse(attributes.get("cycleAnchorDateOfInterestPayment")));
# map.put("CycleOfInterestPayment", attributes.get("cycleOfInterestPayment"));
# map.put("NominalInterestRate", (CommonUtils.isNull(attributes.get("nominalInterestRate"))) ? 0.0 : Double.parseDouble(attributes.get("nominalInterestRate")));
# map.put("DayCountConvention", new DayCountCalculator(attributes.get("dayCountConvention"), (BusinessDayCalendarProvider) map.get("Calendar")));
# map.put("AccruedInterest", (CommonUtils.isNull(attributes.get("accruedInterest"))) ? 0.0 : Double.parseDouble(attributes.get("accruedInterest")));
# map.put("CapitalizationEndDate", (CommonUtils.isNull(attributes.get("capitalizationEndDate"))) ? null : LocalDateTime.parse(attributes.get("capitalizationEndDate")));
# map.put("CyclePointOfInterestPayment", CommonUtils.isNull(attributes.get("cyclePointOfInterestPayment")) ? null : CyclePointOfInterestPayment.valueOf(attributes.get("cyclePointOfInterestPayment")));
# map.put("Currency", attributes.get("currency"));
# map.put("InitialExchangeDate", LocalDateTime.parse(attributes.get("initialExchangeDate")));
# map.put("PremiumDiscountAtIED", (CommonUtils.isNull(attributes.get("premiumDiscountAtIED"))) ? 0.0 : Double.parseDouble(attributes.get("premiumDiscountAtIED")));
# map.put("NotionalPrincipal", Double.parseDouble(attributes.get("notionalPrincipal")));
# map.put("PurchaseDate", (CommonUtils.isNull(attributes.get("purchaseDate"))) ? null : LocalDateTime.parse(attributes.get("purchaseDate")));
# map.put("PriceAtPurchaseDate", (CommonUtils.isNull(attributes.get("priceAtPurchaseDate"))) ? 0.0 : Double.parseDouble(attributes.get("priceAtPurchaseDate")));
# map.put("TerminationDate", (CommonUtils.isNull(attributes.get("terminationDate"))) ? null : LocalDateTime.parse(attributes.get("terminationDate")));
# map.put("PriceAtTerminationDate", (CommonUtils.isNull(attributes.get("priceAtTerminationDate"))) ? 0.0 : Double.parseDouble(attributes.get("priceAtTerminationDate")));
# map.put("MarketObjectCodeOfScalingIndex", attributes.get("marketObjectCodeOfScalingIndex"));
# map.put("ScalingIndexAtContractDealDate", (CommonUtils.isNull(attributes.get("scalingIndexAtContractDealDate"))) ? 0.0 : Double.parseDouble(attributes.get("scalingIndexAtContractDealDate")));
# map.put("NotionalScalingMultiplier", (CommonUtils.isNull(attributes.get("notionalScalingMultiplier"))) ? 1.0 : Double.parseDouble(attributes.get("notionalScalingMultiplier")));
# map.put("InterestScalingMultiplier", (CommonUtils.isNull(attributes.get("interestScalingMultiplier"))) ? 1.0 : Double.parseDouble(attributes.get("interestScalingMultiplier")));
# map.put("CycleAnchorDateOfScalingIndex", (CommonUtils.isNull(attributes.get("cycleAnchorDateOfScalingIndex"))) ? ((CommonUtils.isNull(attributes.get("cycleOfScalingIndex"))) ? null : LocalDateTime.parse(attributes.get("initialExchangeDate"))) : LocalDateTime.parse(attributes.get("cycleAnchorDateOfScalingIndex")));
# map.put("CycleOfScalingIndex", attributes.get("cycleOfScalingIndex"));
# map.put("ScalingEffect", CommonUtils.isNull(attributes.get("scalingEffect")) ? ScalingEffect.OOO : ScalingEffect.valueOf(attributes.get("scalingEffect")));
# // TODO: review prepayment mechanism and attributes
# map.put("CycleAnchorDateOfOptionality", (CommonUtils.isNull(attributes.get("cycleAnchorDateOfOptionality"))) ? ((CommonUtils.isNull(attributes.get("cycleOfOptionality"))) ? null : LocalDateTime.parse(attributes.get("initialExchangeDate"))) : LocalDateTime.parse(attributes.get("cycleAnchorDateOfOptionality")));
# map.put("CycleOfOptionality", attributes.get("cycleOfOptionality"));
# map.put("PenaltyType", (CommonUtils.isNull(attributes.get("penaltyType"))) ? PenaltyType.valueOf("N") : PenaltyType.valueOf(attributes.get("penaltyType")));
# map.put("PenaltyRate", (CommonUtils.isNull(attributes.get("penaltyRate"))) ? 0.0 : Double.parseDouble(attributes.get("penaltyRate")));
# map.put("ObjectCodeOfPrepaymentModel", attributes.get("objectCodeOfPrepaymentModel"));
# map.put("CycleAnchorDateOfRateReset", (CommonUtils.isNull(attributes.get("cycleAnchorDateOfRateReset"))) ? ((CommonUtils.isNull(attributes.get("cycleOfRateReset"))) ? null : LocalDateTime.parse(attributes.get("initialExchangeDate"))) : LocalDateTime.parse(attributes.get("cycleAnchorDateOfRateReset")));
# map.put("CycleOfRateReset", attributes.get("cycleOfRateReset"));
# map.put("RateSpread", (CommonUtils.isNull(attributes.get("rateSpread"))) ? 0.0 : Double.parseDouble(attributes.get("rateSpread")));
# map.put("MarketObjectCodeOfRateReset", attributes.get("marketObjectCodeOfRateReset"));
# map.put("LifeCap", (CommonUtils.isNull(attributes.get("lifeCap"))) ? Double.POSITIVE_INFINITY : Double.parseDouble(attributes.get("lifeCap")));
# map.put("LifeFloor", (CommonUtils.isNull(attributes.get("lifeFloor"))) ? Double.NEGATIVE_INFINITY : Double.parseDouble(attributes.get("lifeFloor")));
# map.put("PeriodCap", (CommonUtils.isNull(attributes.get("periodCap"))) ? Double.POSITIVE_INFINITY : Double.parseDouble(attributes.get("periodCap")));
# map.put("PeriodFloor", (CommonUtils.isNull(attributes.get("periodFloor"))) ? Double.NEGATIVE_INFINITY : Double.parseDouble(attributes.get("periodFloor")));
# map.put("CyclePointOfRateReset", CommonUtils.isNull(attributes.get("cyclePointOfRateReset")) ? null : CyclePointOfRateReset.valueOf(attributes.get("cyclePointOfRateReset")));
# map.put("FixingPeriod", attributes.get("fixingPeriod"));
# map.put("NextResetRate", (CommonUtils.isNull(attributes.get("nextResetRate"))) ? null : Double.parseDouble(attributes.get("nextResetRate")));
# map.put("RateMultiplier", (CommonUtils.isNull(attributes.get("rateMultiplier"))) ? 1.0 : Double.parseDouble(attributes.get("rateMultiplier")));
# map.put("MaturityDate", LocalDateTime.parse(attributes.get("maturityDate")));
