# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from StreamBank.bas
"""

import logging
from AreaTotal import AreaTotal_2
from TileDrain import TileDrain_2
from StreamBankEros_1 import StreamBankEros_1_2
from AGSTRM import AGSTRM_2
from StreamBankN_1 import StreamBankN_1_2
from StreamBankNSum import StreamBankNSum
from Outputs.AvAnimalNSum.AnimalN import AnimalN_2

log = logging.getLogger(__name__)


def CalculateStreamBankEros(z, Y):
    # CALCULATE THE STREAM BANK SEDIMENT AND N AND P
    for i in range(12):
        # CALCULATE ER FACTOR FOR STREAMBANK EROSION
        # z.LE[Y][i] = z.SedAFactor * (z.StreamFlowVolAdj * (z.StreamFlowVol[Y][i] ** 0.6))

        # z.StreamBankEros[Y][i] = z.LE[Y][i] * z.StreamLength * 1500 * 1.5

        # print("StreamBankEros orig = ", z.StreamBankEros[Y][i], "StreamBankEros new = ", z.StreamBankEros_temp[Y][i])
        # print(z.StreamBankEros[Y][i] == z.StreamBankEros_temp[Y][i])

        # CALCULATE STREAM ABANK N AND P
        # z.StreamBankN[Y][i] = \
        #     StreamBankEros_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
        #                      z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
        #                      z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
        #                      z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
        #                      z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
        #                      z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
        #                      z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
        #                      z.n42, z.n54, z.n85, z.UrbBankStab)[Y][i] * (z.SedNitr / 1000000) * z.BankNFrac
        z.StreamBankP[Y][i] = \
            StreamBankEros_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                               z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                               z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                               z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                               z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
                               z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                               z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
                               z.n42, z.n54, z.n85, z.UrbBankStab)[Y][i] * (z.SedPhos / 1000000) * z.BankPFrac

        # CALCULATIONS FOR STREAM BANK STABILIZATION AND FENCING
        # z.SURBBANK = 0
        # z.NURBBANK = 0
        z.PURBBANK = 0
        z.FCURBBANK = 0

        # z.SEDSTAB = 0
        # z.SURBBANK = 0 # TODO: Why is this in here twice ?

        # if z.n42b > 0:
        #     z.SEDSTAB = (z.n46c / z.n42b) * z.StreamBankEros[Y][i] * z.n85d
        #     z.SURBBANK = (z.UrbBankStab / z.n42b) * z.StreamBankEros[Y][i] * z.n85d

        # z.SEDFEN = 0
        # if z.n42 > 0:
        #     z.SEDFEN = (z.n45 / z.n42) * z.StreamBankEros[Y][i] * z.AGSTRM * z.n85

        # print("SURBBANK orig = ", z.SURBBANK, "SURBBANK new = ", z.SURBBANK_temp[Y][i])
        # print(z.SURBBANK == z.SURBBANK_temp[Y][i])

        # print("SEDSTAB orig = ", z.SEDSTAB, "SEDSTAB new = ", z.SURBBANK_temp[Y][i])
        # print(z.SEDSTAB == z.SURBBANK_temp[Y][i])

        # z.StreamBankEros[Y][i] = z.StreamBankEros[Y][i] - (z.SEDSTAB[Y][i] + z.SEDFEN[Y][i] + z.SURBBANK[Y][i])
        # if z.StreamBankEros[Y][i] < 0:
        #     z.StreamBankEros[Y][i] = 0

        # z.NSTAB = 0
        # z.NURBBANK = 0
        # if z.n42b > 0:
        # z.NSTAB = (z.n46c / z.n42b) * \
        #           StreamBankN(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
        #                       z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
        #                       z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
        #                       z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
        #                       z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
        #                       z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
        #                       z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
        #                       z.n42, z.n54, z.n85, z.UrbBankStab, z.SedNitr, z.BankNFrac)[Y][i] * z.n69c
        # z.NURBBANK = (z.UrbBankStab / z.n42b) * StreamBankN(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
        #                       z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
        #                       z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
        #                       z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
        #                       z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
        #                       z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
        #                       z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
        #                       z.n42, z.n54, z.n85, z.UrbBankStab, z.SedNitr, z.BankNFrac)[Y][i] * z.n69c

        # z.NFEN = 0
        # if z.n42 > 0:
        #     z.NFEN = (z.n45 / z.n42) * StreamBankN(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
        #                           z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
        #                           z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
        #                           z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
        #                           z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
        #                           z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
        #                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
        #                           z.n42, z.n54, z.n85, z.UrbBankStab, z.SedNitr, z.BankNFrac)[Y][i] * AGSTRM_2(z.AgLength, z.StreamLength) * z.n69

        # z.StreamBankN_1[Y][i] = StreamBankN(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
        #                           z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
        #                           z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
        #                           z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
        #                           z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
        #                           z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
        #                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.SedNitr, z.BankNFrac)[Y][i] - (z.NSTAB + z.NFEN + z.NURBBANK)
        # if z.StreamBankN_1[Y][i] < 0:
        #     z.StreamBankN_1[Y][i] = 0

        z.PSTAB = 0
        z.PURBBANK = 0
        if z.n42b > 0:
            z.PSTAB = (z.n46c / z.n42b) * z.StreamBankP[Y][i] * z.n77c
            z.PURBBANK = (z.UrbBankStab / z.n42b) * z.StreamBankP[Y][i] * z.n77c

        z.PFEN = 0
        if z.n42 > 0:
            z.PFEN = (z.n45 / z.n42) * z.StreamBankP[Y][i] * AGSTRM_2(z.AgLength, z.StreamLength) * z.n77

        z.StreamBankP[Y][i] = z.StreamBankP[Y][i] - (z.PSTAB + z.PFEN + z.PURBBANK)
        if z.StreamBankP[Y][i] < 0:
            z.StreamBankP[Y][i] = 0

        # CALCULATE ANNUAL STREAMBANK N AND P AND SEDIMENT
        # z.StreamBankNSum[Y] += z.StreamBankN_1[Y][i]
        z.StreamBankPSum[Y] += z.StreamBankP[Y][i]
        z.StreamBankErosSum[Y] += \
            StreamBankEros_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                               z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0,
                               z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                               , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow,
                               z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj,
                               z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d,
                               z.AgLength, z.n42, z.n45, z.n85, z.UrbBankStab)[Y][i]

        # GROUNDWATER N LOADS ARE REDUCED BASED ON SPECIFIC BMPS
        z.GWNRF = 0
        z.CHNGN1 = 0
        z.CHNGN2 = 0
        z.CHNGN3 = 0
        z.CHNGN4 = 0
        z.CHNGN5 = 0
        z.CHNGNTOT = 0
        z.PCTN1 = 0
        z.PCTN2 = 0
        z.PCTN3 = 0
        z.PCTN4 = 0
        z.PCBMPAC = 0
        z.HPBMPAC = 0
        z.BMPACRES = 0
        z.PCTAG = 0
        z.RCNMAC = 0
        z.HPNMAC = 0

        z.CHNGN1 = z.n25 / 100
        z.CHNGN2 = z.n26 / 100
        z.CHNGN3 = z.n27 / 100
        z.CHNGN4 = z.n27b / 100
        z.CHNGN5 = z.n28 / 100
        z.CHNGNTOT = z.CHNGN1 + z.CHNGN2 + z.CHNGN3 + z.CHNGN4 + z.CHNGN5

        if AreaTotal_2(z.Area) > 0 and z.n23 > 0 and z.n42 > 0 and z.n42b > 0:
            z.PCTAG = (z.n23 + z.n24) / AreaTotal_2(z.Area)
            z.GroundNitr[Y][i] -= z.GroundNitr[Y][i] * ((z.n28b / 100) * z.n23) / z.n23 * z.PCTAG * z.n70
            z.GroundNitr[Y][i] -= z.GroundNitr[Y][i] * (z.n43 / z.n42) * (z.n42 / z.n42b) * z.PCTAG * z.n64
            z.GroundNitr[Y][i] -= (z.GroundNitr[Y][i] * (
                    (((z.n29 / 100) * z.n23) + ((z.n37 / 100) * z.n24)) / (z.n23 + z.n24))) * z.PCTAG * z.n68

        # Groundwater P loads are reduced based on extent of nutrient management BMP
        z.RCNMAC = (z.n28b / 100) * z.n23
        z.HPNMAC = (z.n35b / 100) * z.n24

        if AreaTotal_2(z.Area) > 0:
            z.GroundPhos[Y][i] -= (((z.RCNMAC + z.HPNMAC) / AreaTotal_2(z.Area)) *
                                   z.GroundPhos[Y][i] * z.n78)

        z.GroundNitrSum[Y] += z.GroundNitr[Y][i]
        z.GroundPhosSum[Y] += z.GroundPhos[Y][i]

        z.TileDrainSum[Y] += \
            TileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                        z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                        z.RecessionCoef, z.SeepCoef, z.Landuse,
                        z.TileDrainDensity)[Y][i]
        z.TileDrainNSum[Y] += z.TileDrainN[Y][i]
        z.TileDrainPSum[Y] += z.TileDrainP[Y][i]
        z.TileDrainSedSum[Y] += z.TileDrainSed[Y][i]
        # z.AnimalNSum[Y] += z.AnimalN[Y][i]
        z.AnimalPSum[Y] += z.AnimalP[Y][i]
        z.AnimalFCSum[Y] += z.AnimalFC[Y][i]
        z.WWOrgsSum[Y] += z.WWOrgs[Y][i]
        z.SSOrgsSum[Y] += z.SSOrgs[Y][i]
        z.UrbOrgsSum[Y] += z.UrbOrgs[Y][i]
        z.TotalOrgsSum[Y] += z.TotalOrgs[Y][i]
        z.WildOrgsSum[Y] += z.WildOrgs[Y][i]

        # z.GRLostBarnNSum[Y] += z.GRLostBarnN[Y][i]
        z.GRLostBarnPSum[Y] += z.GRLostBarnP[Y][i]
        z.GRLostBarnFCSum[Y] += z.GRLostBarnFC[Y][i]
        # z.NGLostBarnNSum[Y] += z.NGLostBarnN[Y][i]
        z.NGLostBarnPSum[Y] += z.NGLostBarnP[Y][i]
        z.NGLostBarnFCSum[Y] += z.NGLostBarnFC[Y][i]
        z.NGLostManPSum[Y] += z.NGLostManP[Y][i]

        z.TotNitr[Y][i] += StreamBankN_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                           z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                           z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                                           z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
                                           z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.AgLength,
                                           z.UrbBankStab, z.SedNitr, z.BankNFrac, z.n69c, z.n45, z.n69, z.n46c, z.n42)[Y][i] + \
                           z.TileDrainN[Y][i] +  AnimalN_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
            z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN,
            z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.GrazingNRate)[Y][i]
        z.TotPhos[Y][i] += z.StreamBankP[Y][i] + z.TileDrainP[Y][i] + z.AnimalP[Y][i]

        z.TotNitrSum[Y] += StreamBankN_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                           z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                           z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                                           z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
                                           z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.AgLength,
                                           z.UrbBankStab, z.SedNitr, z.BankNFrac, z.n69c, z.n45, z.n69, z.n46c, z.n42)[Y][i] + \
                           z.TileDrainN[Y][i] + AnimalN_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
            z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN,
            z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.GrazingNRate)[Y][i]
        z.TotPhosSum[Y] += z.StreamBankP[Y][i] + z.TileDrainP[Y][i] + z.AnimalP[Y][i]
