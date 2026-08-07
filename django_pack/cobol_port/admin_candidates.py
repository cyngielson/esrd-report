"""
Django Admin registration — auto-generated from COBOL portfolio.
"""

from django.contrib import admin
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import MsaWageFactor2006
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import MsaWageFactor2006
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import MsaWageFactor2006
from .models import MsaWageFactor2007
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import MsaWageFactor2006
from .models import MsaWageFactor2007
from .models import MsaWageFactor2008
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldPpsComponents
from .models import DrugAddon
from .models import HospBasedPmtRate
from .models import IndpEsrdFacPmtRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import EtcHdpaPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import CalVersion
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import HoldCompRatePpsComponents
from .models import DrugAddon
from .models import BasePaymentRate
from .models import MsaBlendPct
from .models import CbsaBlendPct
from .models import NatLaborPct
from .models import NatNonlaborPct
from .models import EtcHdpaPct
from .models import A49CentPartDDrugAdj
from .models import HemoPeriCcpdAmt
from .models import CapdAmt
from .models import CapdOrCcpdFactor
from .models import CaseMixBdgtNeutFactor
from .models import CompositeRateMultipliers
from .models import HoldBundledPpsComponents
from .models import HoldOutlierPpsComponents
from .models import BundledBasePmtRate
from .models import ComCbsaBlendPct
from .models import BunCbsaBlendPct
from .models import WaiveCbsaBlendPct
from .models import BunNatLaborPct
from .models import BunNatNonlaborPct
from .models import TrainingAddOnPmtAmt
from .models import TransitionBdgtNeutFactor
from .models import BsaNationalAverage
from .models import PediatricMultipliers
from .models import AdultMultipliers
from .models import OutlierSbCalcAmounts
from .models import PaidReturnCodeTrackers
from .models import BillNewData
from .models import PpsDataAll
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import WStorageRef
from .models import DriverVersion
from .models import Escal056
from .models import Escal062
from .models import Escal070
from .models import Escal071
from .models import Escal080
from .models import Escal091
from .models import Escal100
from .models import Escal117
from .models import Escal122
from .models import Escal130
from .models import Escal140
from .models import Escal151
from .models import Escal160
from .models import Escal170
from .models import Escal171
from .models import Escal180
from .models import Escal191
from .models import Escal200
from .models import Escal202
from .models import Escal212
from .models import DisplayLineMeasurement
from .models import PrintLineMeasurement
from .models import WorkArea
from .models import BThruYearCode
from .models import HEsrdSuppWiRatio
from .models import MainframePcSwitch
from .models import DsControlBlock
from .models import WWartDateFills
from .models import WWartDateTable
from .models import WwdMax
from .models import WwdSub
from .models import WWartMsaFills
from .models import WWartMsaTable
from .models import WwmMax
from .models import WWartWartFills
from .models import WWartWartTable
from .models import ComDateFiller
from .models import ComDateTable
from .models import ComMaxDate
from .models import ComSub
from .models import ComCbsaFiller
from .models import ComCbsaTable
from .models import ComMax
from .models import ComWageIndexFiller
from .models import ComWageIndexTable
from .models import BunDateFiller
from .models import BunDateTable
from .models import BunMaxDate
from .models import BunSub
from .models import BunCbsaFiller
from .models import BunCbsaTable
from .models import BunMax
from .models import BunWageIndexFiller
from .models import BunWageIndexTable
from .models import Switches
from .models import Subscripts
from .models import ChildHospTableValues
from .models import ChildHospTable
from .models import TotalNumOfChildHosp
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import BillNewData
from .models import PpsDataAll
from .models import WWartDateFills
from .models import WWartDateTable
from .models import WwdMax
from .models import WwdSub
from .models import WWartMsaFills
from .models import WWartMsaTable
from .models import WwmMax
from .models import WWartWartFills
from .models import WWartWartTable
from .models import MainframePcSwitch
from .models import DsControlBlock
from .models import BunDateFiller
from .models import BunDateTable
from .models import BunMaxDate
from .models import BunSub
from .models import BunCbsaFiller
from .models import BunCbsaTable
from .models import BunMax
from .models import BunWageIndexFiller
from .models import BunWageIndexTable
from .models import Switches
from .models import Subscripts
from .models import ChildHospTableValues
from .models import ChildHospTable
from .models import TotalNumOfChildHosp
from .models import WageNewRateRecord
from .models import ComCbsaWageRecord
from .models import BunCbsaWageRecord
from .models import BillNewData
from .models import PpsDataAll
from .models import ComDateFiller
from .models import ComDateTable
from .models import ComMaxDate
from .models import ComSub
from .models import ComCbsaFiller
from .models import ComCbsaTable
from .models import ComMax
from .models import ComWageIndexFiller
from .models import ComWageIndexTable


@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2006)
class MsaWageFactor2006Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2006._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2006._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2006)
class MsaWageFactor2006Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2006._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2006._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2006)
class MsaWageFactor2006Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2006._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2006._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2007)
class MsaWageFactor2007Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2007._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2007._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2006)
class MsaWageFactor2006Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2006._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2006._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2007)
class MsaWageFactor2007Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2007._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2007._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaWageFactor2008)
class MsaWageFactor2008Admin(admin.ModelAdmin):
    list_display = [f.name for f in MsaWageFactor2008._meta.fields]
    search_fields = [f.name for f in MsaWageFactor2008._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldPpsComponents)
class HoldPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HospBasedPmtRate)
class HospBasedPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HospBasedPmtRate._meta.fields]
    search_fields = [f.name for f in HospBasedPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(IndpEsrdFacPmtRate)
class IndpEsrdFacPmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndpEsrdFacPmtRate._meta.fields]
    search_fields = [f.name for f in IndpEsrdFacPmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(EtcHdpaPct)
class EtcHdpaPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EtcHdpaPct._meta.fields]
    search_fields = [f.name for f in EtcHdpaPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CalVersion)
class CalVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CalVersion._meta.fields]
    search_fields = [f.name for f in CalVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldCompRatePpsComponents)
class HoldCompRatePpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldCompRatePpsComponents._meta.fields]
    search_fields = [f.name for f in HoldCompRatePpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DrugAddon)
class DrugAddonAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DrugAddon._meta.fields]
    search_fields = [f.name for f in DrugAddon._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BasePaymentRate)
class BasePaymentRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BasePaymentRate._meta.fields]
    search_fields = [f.name for f in BasePaymentRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MsaBlendPct)
class MsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MsaBlendPct._meta.fields]
    search_fields = [f.name for f in MsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CbsaBlendPct)
class CbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CbsaBlendPct._meta.fields]
    search_fields = [f.name for f in CbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatLaborPct)
class NatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatLaborPct._meta.fields]
    search_fields = [f.name for f in NatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(NatNonlaborPct)
class NatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in NatNonlaborPct._meta.fields]
    search_fields = [f.name for f in NatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(EtcHdpaPct)
class EtcHdpaPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EtcHdpaPct._meta.fields]
    search_fields = [f.name for f in EtcHdpaPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(A49CentPartDDrugAdj)
class A49CentPartDDrugAdjAdmin(admin.ModelAdmin):
    list_display = [f.name for f in A49CentPartDDrugAdj._meta.fields]
    search_fields = [f.name for f in A49CentPartDDrugAdj._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HemoPeriCcpdAmt)
class HemoPeriCcpdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HemoPeriCcpdAmt._meta.fields]
    search_fields = [f.name for f in HemoPeriCcpdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdAmt)
class CapdAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdAmt._meta.fields]
    search_fields = [f.name for f in CapdAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CapdOrCcpdFactor)
class CapdOrCcpdFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CapdOrCcpdFactor._meta.fields]
    search_fields = [f.name for f in CapdOrCcpdFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CaseMixBdgtNeutFactor)
class CaseMixBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CaseMixBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in CaseMixBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(CompositeRateMultipliers)
class CompositeRateMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CompositeRateMultipliers._meta.fields]
    search_fields = [f.name for f in CompositeRateMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldBundledPpsComponents)
class HoldBundledPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldBundledPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldBundledPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HoldOutlierPpsComponents)
class HoldOutlierPpsComponentsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HoldOutlierPpsComponents._meta.fields]
    search_fields = [f.name for f in HoldOutlierPpsComponents._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BundledBasePmtRate)
class BundledBasePmtRateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BundledBasePmtRate._meta.fields]
    search_fields = [f.name for f in BundledBasePmtRate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaBlendPct)
class ComCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in ComCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaBlendPct)
class BunCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in BunCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WaiveCbsaBlendPct)
class WaiveCbsaBlendPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WaiveCbsaBlendPct._meta.fields]
    search_fields = [f.name for f in WaiveCbsaBlendPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatLaborPct)
class BunNatLaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatLaborPct._meta.fields]
    search_fields = [f.name for f in BunNatLaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunNatNonlaborPct)
class BunNatNonlaborPctAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunNatNonlaborPct._meta.fields]
    search_fields = [f.name for f in BunNatNonlaborPct._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TrainingAddOnPmtAmt)
class TrainingAddOnPmtAmtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TrainingAddOnPmtAmt._meta.fields]
    search_fields = [f.name for f in TrainingAddOnPmtAmt._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TransitionBdgtNeutFactor)
class TransitionBdgtNeutFactorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TransitionBdgtNeutFactor._meta.fields]
    search_fields = [f.name for f in TransitionBdgtNeutFactor._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BsaNationalAverage)
class BsaNationalAverageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BsaNationalAverage._meta.fields]
    search_fields = [f.name for f in BsaNationalAverage._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PediatricMultipliers)
class PediatricMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PediatricMultipliers._meta.fields]
    search_fields = [f.name for f in PediatricMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(AdultMultipliers)
class AdultMultipliersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AdultMultipliers._meta.fields]
    search_fields = [f.name for f in AdultMultipliers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(OutlierSbCalcAmounts)
class OutlierSbCalcAmountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OutlierSbCalcAmounts._meta.fields]
    search_fields = [f.name for f in OutlierSbCalcAmounts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PaidReturnCodeTrackers)
class PaidReturnCodeTrackersAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PaidReturnCodeTrackers._meta.fields]
    search_fields = [f.name for f in PaidReturnCodeTrackers._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WStorageRef)
class WStorageRefAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WStorageRef._meta.fields]
    search_fields = [f.name for f in WStorageRef._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DriverVersion)
class DriverVersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DriverVersion._meta.fields]
    search_fields = [f.name for f in DriverVersion._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal056)
class Escal056Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal056._meta.fields]
    search_fields = [f.name for f in Escal056._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal062)
class Escal062Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal062._meta.fields]
    search_fields = [f.name for f in Escal062._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal070)
class Escal070Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal070._meta.fields]
    search_fields = [f.name for f in Escal070._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal071)
class Escal071Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal071._meta.fields]
    search_fields = [f.name for f in Escal071._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal080)
class Escal080Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal080._meta.fields]
    search_fields = [f.name for f in Escal080._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal091)
class Escal091Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal091._meta.fields]
    search_fields = [f.name for f in Escal091._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal100)
class Escal100Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal100._meta.fields]
    search_fields = [f.name for f in Escal100._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal117)
class Escal117Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal117._meta.fields]
    search_fields = [f.name for f in Escal117._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal122)
class Escal122Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal122._meta.fields]
    search_fields = [f.name for f in Escal122._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal130)
class Escal130Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal130._meta.fields]
    search_fields = [f.name for f in Escal130._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal140)
class Escal140Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal140._meta.fields]
    search_fields = [f.name for f in Escal140._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal151)
class Escal151Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal151._meta.fields]
    search_fields = [f.name for f in Escal151._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal160)
class Escal160Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal160._meta.fields]
    search_fields = [f.name for f in Escal160._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal170)
class Escal170Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal170._meta.fields]
    search_fields = [f.name for f in Escal170._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal171)
class Escal171Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal171._meta.fields]
    search_fields = [f.name for f in Escal171._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal180)
class Escal180Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal180._meta.fields]
    search_fields = [f.name for f in Escal180._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal191)
class Escal191Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal191._meta.fields]
    search_fields = [f.name for f in Escal191._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal200)
class Escal200Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal200._meta.fields]
    search_fields = [f.name for f in Escal200._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal202)
class Escal202Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal202._meta.fields]
    search_fields = [f.name for f in Escal202._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Escal212)
class Escal212Admin(admin.ModelAdmin):
    list_display = [f.name for f in Escal212._meta.fields]
    search_fields = [f.name for f in Escal212._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DisplayLineMeasurement)
class DisplayLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DisplayLineMeasurement._meta.fields]
    search_fields = [f.name for f in DisplayLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PrintLineMeasurement)
class PrintLineMeasurementAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PrintLineMeasurement._meta.fields]
    search_fields = [f.name for f in PrintLineMeasurement._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WorkArea)
class WorkAreaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WorkArea._meta.fields]
    search_fields = [f.name for f in WorkArea._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BThruYearCode)
class BThruYearCodeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BThruYearCode._meta.fields]
    search_fields = [f.name for f in BThruYearCode._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(HEsrdSuppWiRatio)
class HEsrdSuppWiRatioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in HEsrdSuppWiRatio._meta.fields]
    search_fields = [f.name for f in HEsrdSuppWiRatio._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MainframePcSwitch)
class MainframePcSwitchAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MainframePcSwitch._meta.fields]
    search_fields = [f.name for f in MainframePcSwitch._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DsControlBlock)
class DsControlBlockAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DsControlBlock._meta.fields]
    search_fields = [f.name for f in DsControlBlock._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartDateFills)
class WWartDateFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartDateFills._meta.fields]
    search_fields = [f.name for f in WWartDateFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartDateTable)
class WWartDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartDateTable._meta.fields]
    search_fields = [f.name for f in WWartDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwdMax)
class WwdMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwdMax._meta.fields]
    search_fields = [f.name for f in WwdMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwdSub)
class WwdSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwdSub._meta.fields]
    search_fields = [f.name for f in WwdSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartMsaFills)
class WWartMsaFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartMsaFills._meta.fields]
    search_fields = [f.name for f in WWartMsaFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartMsaTable)
class WWartMsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartMsaTable._meta.fields]
    search_fields = [f.name for f in WWartMsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwmMax)
class WwmMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwmMax._meta.fields]
    search_fields = [f.name for f in WwmMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartWartFills)
class WWartWartFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartWartFills._meta.fields]
    search_fields = [f.name for f in WWartWartFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartWartTable)
class WWartWartTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartWartTable._meta.fields]
    search_fields = [f.name for f in WWartWartTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComDateFiller)
class ComDateFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComDateFiller._meta.fields]
    search_fields = [f.name for f in ComDateFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComDateTable)
class ComDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComDateTable._meta.fields]
    search_fields = [f.name for f in ComDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComMaxDate)
class ComMaxDateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComMaxDate._meta.fields]
    search_fields = [f.name for f in ComMaxDate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComSub)
class ComSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComSub._meta.fields]
    search_fields = [f.name for f in ComSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaFiller)
class ComCbsaFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaFiller._meta.fields]
    search_fields = [f.name for f in ComCbsaFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaTable)
class ComCbsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaTable._meta.fields]
    search_fields = [f.name for f in ComCbsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComMax)
class ComMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComMax._meta.fields]
    search_fields = [f.name for f in ComMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComWageIndexFiller)
class ComWageIndexFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComWageIndexFiller._meta.fields]
    search_fields = [f.name for f in ComWageIndexFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComWageIndexTable)
class ComWageIndexTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComWageIndexTable._meta.fields]
    search_fields = [f.name for f in ComWageIndexTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunDateFiller)
class BunDateFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunDateFiller._meta.fields]
    search_fields = [f.name for f in BunDateFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunDateTable)
class BunDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunDateTable._meta.fields]
    search_fields = [f.name for f in BunDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunMaxDate)
class BunMaxDateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunMaxDate._meta.fields]
    search_fields = [f.name for f in BunMaxDate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunSub)
class BunSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunSub._meta.fields]
    search_fields = [f.name for f in BunSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaFiller)
class BunCbsaFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaFiller._meta.fields]
    search_fields = [f.name for f in BunCbsaFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaTable)
class BunCbsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaTable._meta.fields]
    search_fields = [f.name for f in BunCbsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunMax)
class BunMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunMax._meta.fields]
    search_fields = [f.name for f in BunMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunWageIndexFiller)
class BunWageIndexFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunWageIndexFiller._meta.fields]
    search_fields = [f.name for f in BunWageIndexFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunWageIndexTable)
class BunWageIndexTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunWageIndexTable._meta.fields]
    search_fields = [f.name for f in BunWageIndexTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Switches)
class SwitchesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Switches._meta.fields]
    search_fields = [f.name for f in Switches._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Subscripts)
class SubscriptsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Subscripts._meta.fields]
    search_fields = [f.name for f in Subscripts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ChildHospTableValues)
class ChildHospTableValuesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ChildHospTableValues._meta.fields]
    search_fields = [f.name for f in ChildHospTableValues._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ChildHospTable)
class ChildHospTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ChildHospTable._meta.fields]
    search_fields = [f.name for f in ChildHospTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TotalNumOfChildHosp)
class TotalNumOfChildHospAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TotalNumOfChildHosp._meta.fields]
    search_fields = [f.name for f in TotalNumOfChildHosp._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartDateFills)
class WWartDateFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartDateFills._meta.fields]
    search_fields = [f.name for f in WWartDateFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartDateTable)
class WWartDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartDateTable._meta.fields]
    search_fields = [f.name for f in WWartDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwdMax)
class WwdMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwdMax._meta.fields]
    search_fields = [f.name for f in WwdMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwdSub)
class WwdSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwdSub._meta.fields]
    search_fields = [f.name for f in WwdSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartMsaFills)
class WWartMsaFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartMsaFills._meta.fields]
    search_fields = [f.name for f in WWartMsaFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartMsaTable)
class WWartMsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartMsaTable._meta.fields]
    search_fields = [f.name for f in WWartMsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WwmMax)
class WwmMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WwmMax._meta.fields]
    search_fields = [f.name for f in WwmMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartWartFills)
class WWartWartFillsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartWartFills._meta.fields]
    search_fields = [f.name for f in WWartWartFills._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WWartWartTable)
class WWartWartTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WWartWartTable._meta.fields]
    search_fields = [f.name for f in WWartWartTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(MainframePcSwitch)
class MainframePcSwitchAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MainframePcSwitch._meta.fields]
    search_fields = [f.name for f in MainframePcSwitch._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(DsControlBlock)
class DsControlBlockAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DsControlBlock._meta.fields]
    search_fields = [f.name for f in DsControlBlock._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunDateFiller)
class BunDateFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunDateFiller._meta.fields]
    search_fields = [f.name for f in BunDateFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunDateTable)
class BunDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunDateTable._meta.fields]
    search_fields = [f.name for f in BunDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunMaxDate)
class BunMaxDateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunMaxDate._meta.fields]
    search_fields = [f.name for f in BunMaxDate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunSub)
class BunSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunSub._meta.fields]
    search_fields = [f.name for f in BunSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaFiller)
class BunCbsaFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaFiller._meta.fields]
    search_fields = [f.name for f in BunCbsaFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaTable)
class BunCbsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaTable._meta.fields]
    search_fields = [f.name for f in BunCbsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunMax)
class BunMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunMax._meta.fields]
    search_fields = [f.name for f in BunMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunWageIndexFiller)
class BunWageIndexFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunWageIndexFiller._meta.fields]
    search_fields = [f.name for f in BunWageIndexFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunWageIndexTable)
class BunWageIndexTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunWageIndexTable._meta.fields]
    search_fields = [f.name for f in BunWageIndexTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Switches)
class SwitchesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Switches._meta.fields]
    search_fields = [f.name for f in Switches._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(Subscripts)
class SubscriptsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Subscripts._meta.fields]
    search_fields = [f.name for f in Subscripts._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ChildHospTableValues)
class ChildHospTableValuesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ChildHospTableValues._meta.fields]
    search_fields = [f.name for f in ChildHospTableValues._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ChildHospTable)
class ChildHospTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ChildHospTable._meta.fields]
    search_fields = [f.name for f in ChildHospTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(TotalNumOfChildHosp)
class TotalNumOfChildHospAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TotalNumOfChildHosp._meta.fields]
    search_fields = [f.name for f in TotalNumOfChildHosp._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(WageNewRateRecord)
class WageNewRateRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WageNewRateRecord._meta.fields]
    search_fields = [f.name for f in WageNewRateRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaWageRecord)
class ComCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in ComCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BunCbsaWageRecord)
class BunCbsaWageRecordAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BunCbsaWageRecord._meta.fields]
    search_fields = [f.name for f in BunCbsaWageRecord._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(BillNewData)
class BillNewDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BillNewData._meta.fields]
    search_fields = [f.name for f in BillNewData._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(PpsDataAll)
class PpsDataAllAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PpsDataAll._meta.fields]
    search_fields = [f.name for f in PpsDataAll._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComDateFiller)
class ComDateFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComDateFiller._meta.fields]
    search_fields = [f.name for f in ComDateFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComDateTable)
class ComDateTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComDateTable._meta.fields]
    search_fields = [f.name for f in ComDateTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComMaxDate)
class ComMaxDateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComMaxDate._meta.fields]
    search_fields = [f.name for f in ComMaxDate._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComSub)
class ComSubAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComSub._meta.fields]
    search_fields = [f.name for f in ComSub._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaFiller)
class ComCbsaFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaFiller._meta.fields]
    search_fields = [f.name for f in ComCbsaFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComCbsaTable)
class ComCbsaTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComCbsaTable._meta.fields]
    search_fields = [f.name for f in ComCbsaTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComMax)
class ComMaxAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComMax._meta.fields]
    search_fields = [f.name for f in ComMax._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComWageIndexFiller)
class ComWageIndexFillerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComWageIndexFiller._meta.fields]
    search_fields = [f.name for f in ComWageIndexFiller._meta.fields if 'char' in str(f.get_internal_type()).lower()]

@admin.register(ComWageIndexTable)
class ComWageIndexTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ComWageIndexTable._meta.fields]
    search_fields = [f.name for f in ComWageIndexTable._meta.fields if 'char' in str(f.get_internal_type()).lower()]

