from enum import Enum

from pydantic import BaseModel


class FactorType(str, Enum):
    AtomicIndex = "AtomicIndex"
    DerivedIndex = "DerivedIndex"
    DerivativeIndicators = "DerivativeIndicators"


class Factor(BaseModel):
    factorId: str = None

    value: str = None,

    topicId: str = None
    # isQuantify: bool = None,
    # isResult: bool = None
    groupId: str = None

    type: FactorType = None

    # isDimension: bool = None

    timePeriodId: str = None

    # factorDimension: FactorDimension = None
    isTransactionalIndicators: bool = None,

    isStockIndex: bool = False,

    isWordFrequency: bool = False,

    codeTable: str = None

