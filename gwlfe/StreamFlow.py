from numpy import zeros

# from Timer import time_function
from Flow import Flow
from GroundWatLE_1 import GroundWatLE_1
from GroundWatLE_1 import GroundWatLE_1_f
from Memoization import memoize
from MultiUse_Fxns.PtSrcFlow import PtSrcFlow
from MultiUse_Fxns.PtSrcFlow import PtSrcFlow_f
from Runoff import Runoff
from Runoff import Runoff_f
from TileDrain import TileDrain
from TileDrain import TileDrain_f
from Withdrawal import Withdrawal
from Withdrawal import Withdrawal_f


@memoize
def StreamFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
               , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
               GroundWithdrawal):
    result = zeros((NYrs, 12))
    flow = Flow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    runoff = Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    groundwatle_f = GroundWatLE_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper,
                                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    ptsrcflow = PtSrcFlow(NYrs, PointFlow)
    tiledrain = TileDrain(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper,
                          ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                          SeepCoef, Landuse, TileDrainDensity)
    withdrawal = Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            # for j in range(DaysMonth[Y][i]):
            #     result[Y][i] = result[Y][i] + flow[Y][i][j]  # This is weird, it seems to be immediately overwritten
            result[Y][i] = (runoff[Y][i]
                            + groundwatle_f[Y][i]
                            + ptsrcflow[Y][i]
                            + tiledrain[Y][i]
                            - withdrawal[Y][i])
    return result

@memoize
def StreamFlow_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                 Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                 GroundWithdrawal):
    runoff = Runoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                      ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    groundwatle_f = GroundWatLE_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    ptsrcflow = PtSrcFlow_f(NYrs, PointFlow)
    tiledrain = TileDrain_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                            RecessionCoef,
                            SeepCoef, Landuse, TileDrainDensity)
    withdrawal = Withdrawal_f(NYrs, StreamWithdrawal, GroundWithdrawal)
    return runoff + groundwatle_f + ptsrcflow + tiledrain - withdrawal
